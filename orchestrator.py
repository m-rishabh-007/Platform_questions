"""
Orchestrator for Competitive Programming Test Suite Generation
"""

import argparse
import subprocess
import os
import random
import json
import sys
import requests
import time
from pathlib import Path


class Config:
    PROBLEMS_DIR = "."
    JUDGE0_URL = "http://localhost:3000"
    LANGUAGE_CONFIGS = {
        "python": {"id": 71, "file_ext": "py"},
        "cpp": {"id": 54, "file_ext": "cpp"}
    }
    TIME_THRESHOLD = 0.005
    MIN_MEANINGFUL_CASES = 10


class SystemUtils:
    @staticmethod
    def run_script(command, input_data=None):
        try:
            result = subprocess.run(
                command,
                input=input_data,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout or ""
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Subprocess error: {e}")
            print(f"Command: {' '.join(command)}")
            print(f"Stderr: {e.stderr}")
            raise
        except Exception as e:
            print(f"⚠️ Unexpected error in run_script: {e}")
            raise


class BaselineManager:
    def __init__(self, judge0_url):
        self.judge0_url = judge0_url

    def measure_baseline_overhead(self, master_source_code, language_id):
        print(f"🔧 Measuring baseline overhead for language {language_id}...")
        
        baseline_inputs = [
            "1 2 3\n1 1"
        ]
        
        time_samples = []
        memory_samples = []
        for i, baseline_input in enumerate(baseline_inputs):
            try:
                response = requests.post(
                    f"{self.judge0_url}/submissions?base64_encoded=false&wait=true&fields=time,memory,stdout,stderr,status",
                    json={
                        "source_code": master_source_code,
                        "language_id": language_id,
                        "stdin": baseline_input
                    }
                )
                response.raise_for_status()
                result = response.json()
                if result.get("status", {}).get("id") == 3:
                    raw_time = float(result.get("time", 0) or 0)
                    raw_memory = int(result.get("memory", 0) or 0)
                    time_samples.append(raw_time)
                    memory_samples.append(raw_memory)
                    print(f"  Sample {i+1}: {raw_time}s, {raw_memory}KB")
                else:
                    print(f"⚠️ Baseline sample {i+1} failed: {result.get('status', {})}")
            except Exception as e:
                print(f"⚠️ Error in baseline sample {i+1}: {e}")
                continue
        if not time_samples or not memory_samples:
            print("⚠️ Could not measure baseline - using default values")
            if language_id == 71:
                return 0.040, 4200
            else:
                return 0.005, 1500
        baseline_time = min(time_samples)
        baseline_memory = min(memory_samples)
        print(f"✅ Baseline overhead - Time: {baseline_time}s, Memory: {baseline_memory}KB")
        return baseline_time, baseline_memory


class InputAnalyzer:
    @staticmethod
    def estimate_input_size(stdin_data):
        try:
            lines = stdin_data.strip().split('\n')
            g_len = len(lines[0].split(' ')) if lines[0] else 0
            s_len = len(lines[1].split(' ')) if len(lines) > 1 and lines[1] else 0
            return g_len + s_len
        except Exception:
            return len(stdin_data)


class Judge0Executor:
    def __init__(self, judge0_url):
        self.judge0_url = judge0_url
        self.input_analyzer = InputAnalyzer()

    def execute_with_judge0(self, source_code, test_input, language_id, baseline_time=0.0, baseline_memory=0):
        try:
            response = requests.post(
                f"{self.judge0_url}/submissions?base64_encoded=false&wait=true&fields=time,memory,stdout,stderr,status",
                json={
                    "source_code": source_code,
                    "language_id": language_id,
                    "stdin": test_input
                }
            )
            response.raise_for_status()
            result = response.json()
            stdout_payload = result.get("stdout") or ""
            stderr_payload = result.get("stderr") or ""
            if result.get("status", {}).get("id") != 3:
                return None, f"Status: {result.get('status', {})} | Stderr: {stderr_payload or 'N/A'}"
            raw_time = float(result.get("time", 0) or 0)
            raw_memory = int(result.get("memory", 0) or 0)
            algo_time = max(0.0, raw_time - baseline_time)
            algo_memory = max(baseline_memory * 0.05, raw_memory - baseline_memory)
            input_size = self.input_analyzer.estimate_input_size(test_input)
            execution_result = {
                "stdout": stdout_payload.strip(),
                "admin_time": algo_time,
                "admin_memory": algo_memory,
                "raw_time": raw_time,
                "raw_memory": raw_memory,
                "input_size": input_size,
                "baseline_time": baseline_time,
                "baseline_memory": baseline_memory,
                "stderr": stderr_payload.strip()
            }
            return execution_result, None
        except requests.exceptions.RequestException as e:
            return None, f"Judge0 request failed: {e}"


class TestCaseGenerator:
    def __init__(self, config, system_utils, judge0_executor):
        self.config = config
        self.system_utils = system_utils
        self.judge0_executor = judge0_executor

    def generate_test_case_batch(self, generator_script, rule, count, master_source_code, language_id, baseline_time, baseline_memory):
        successful_cases = []
        for _ in range(count * 3):
            try:
                args = rule.get("args", {})
                # Backwards-compatible path for legacy generators that expect positional numeric args
                if {"g_len", "s_len", "min_val", "max_val"}.issubset(args.keys()):
                    g_len = random.randint(*args["g_len"])
                    s_len = random.randint(*args["s_len"])
                    min_val = args["min_val"]
                    max_val = args["max_val"]
                    gen_cmd = [
                        "python", generator_script,
                        str(g_len), str(s_len), str(min_val), str(max_val)
                    ]
                else:
                    # Primary path: pass rule metadata as JSON payload to the generator
                    payload = json.dumps(args)  # Just pass args directly as JSON
                    gen_cmd = [
                        "python3", generator_script,
                        rule.get("type", ""),  # rule_type as positional argument
                        "--args", payload
                    ]
                generated_input = self.system_utils.run_script(gen_cmd)
                if not generated_input or not generated_input.strip():
                    continue
                execution_result, error = self.judge0_executor.execute_with_judge0(
                    master_source_code,
                    generated_input.strip(),
                    language_id,
                    baseline_time,
                    baseline_memory
                )
                if error:
                    continue
                test_case = {
                    "stdin": generated_input.strip(),
                    "expected_output": execution_result["stdout"],
                    "is_visible": False,
                    "admin_time": execution_result["admin_time"],
                    "admin_memory": execution_result["admin_memory"],
                    "input_size": execution_result["input_size"],
                    "raw_time": execution_result["raw_time"],
                    "raw_memory": execution_result["raw_memory"]
                }
                successful_cases.append(test_case)
                if len(successful_cases) >= count:
                    break
            except Exception as e:
                continue
        return successful_cases[:count]


class TestSuiteOrchestrator:
    def __init__(self, config=None):
        self.config = config or Config()
        self.system_utils = SystemUtils()
        self.baseline_manager = BaselineManager(self.config.JUDGE0_URL)
        self.judge0_executor = Judge0Executor(self.config.JUDGE0_URL)
        self.test_case_generator = TestCaseGenerator(self.config, self.system_utils, self.judge0_executor)

    def create_json_test_suite(self, problem_name, language="python"):
        if language not in self.config.LANGUAGE_CONFIGS:
            print(f"⚠️ Unsupported language: {language}")
            return

        lang_config = self.config.LANGUAGE_CONFIGS[language]
        problem_path = self.config.PROBLEMS_DIR
        output_json_file = os.path.join(problem_path, f"{problem_name}_{language}_testcases.json")
        master_solution_script = os.path.join(problem_path, f"solution.{lang_config['file_ext']}")
        generator_script = os.path.join(problem_path, "generator.py")
        config_file = os.path.join(problem_path, "config.json")
        examples_file = os.path.join(problem_path, "examples.json")

        try:
            with open(master_solution_script, 'r') as f:
                master_source_code = f.read()
            with open(config_file, 'r') as f:
                config = json.load(f)
            with open(examples_file, 'r') as f:
                examples = json.load(f)
        except FileNotFoundError as e:
            print(f"⚠️ Error: Missing file in problem directory: {e.filename}")
            return
        baseline_time, baseline_memory = self.baseline_manager.measure_baseline_overhead(master_source_code, lang_config["id"])
        all_test_cases = []
        print(f"\n📋 Processing {len(examples)} visible test cases for {language.upper()}...")
        for i, example in enumerate(examples):
            execution_result, error = self.judge0_executor.execute_with_judge0(
                master_source_code,
                example["stdin"],
                lang_config["id"],
                baseline_time,
                baseline_memory
            )
            if error:
                print(f"⚠️ Failed visible test case {i + 1}: {error}")
                test_case = {
                    "test_case_no": i + 1,
                    "stdin": example["stdin"],
                    "expected_output": example["expected_output"],
                    "is_visible": True,
                    "error": error
                }
            else:
                test_case = {
                    "test_case_no": i + 1,
                    "stdin": example["stdin"],
                    "expected_output": execution_result["stdout"],
                    "is_visible": True,
                    "admin_time": execution_result["admin_time"],
                    "admin_memory": execution_result["admin_memory"],
                    "input_size": execution_result["input_size"],
                    "raw_time": execution_result["raw_time"],
                    "raw_memory": execution_result["raw_memory"]
                }
                print(f"✅ Case #{i + 1}: {execution_result['admin_time']:.4f}s, {execution_result['admin_memory']}KB, size={execution_result['input_size']}")
            all_test_cases.append(test_case)
        if language == "cpp":
            target_counts = {
                "edge_cases": 5, "small": 5, "medium": 5, "large": 5, "extra_large": 5
            }
        else:
            target_counts = {
                "edge_cases": 5, "small": 5, "medium": 5, "large": 5, "extra_large": 5
            }
        test_case_counter = len(all_test_cases) + 1
        for rule in config["generation_logic"]:
            rule_type = rule["type"]
            target_count = target_counts.get(rule_type, rule["count"])
            print(f"--- Rule: {rule_type} ({target_count} cases) ---")
            batch_cases = self.test_case_generator.generate_test_case_batch(
                generator_script, rule, target_count,
                master_source_code, lang_config["id"], baseline_time, baseline_memory
            )
            for test_case in batch_cases:
                test_case["test_case_no"] = test_case_counter
                all_test_cases.append(test_case)
                test_case_counter += 1
            print(f"✅ Generated {len(batch_cases)}/{target_count} cases for '{rule_type}'")
        meaningful_cases = [tc for tc in all_test_cases if tc.get("admin_time", 0) >= self.config.TIME_THRESHOLD]
        meaningful_count = len(meaningful_cases)
        print(f"\n📊 Meaningful cases (≥{self.config.TIME_THRESHOLD}s): {meaningful_count}")
        additional_needed = max(0, self.config.MIN_MEANINGFUL_CASES - meaningful_count)
        if additional_needed > 0:
            print(f"🚀 Generating {additional_needed} additional cases for meaningful threshold...")
            large_rule = next((rule for rule in config["generation_logic"] if rule["type"] == "large"), None)
            extra_large_rule = next((rule for rule in config["generation_logic"] if rule["type"] == "extra_large"), None)

            fallback_rules = [
                next((rule for rule in config["generation_logic"] if rule["type"] == "long"), None),
                next((rule for rule in config["generation_logic"] if rule["type"] == "medium"), None)
            ]
            candidate_rules = [large_rule, extra_large_rule] + fallback_rules
            candidate_rules = [rule for rule in candidate_rules if rule is not None]

            if not candidate_rules:
                print("⚠️ No suitable rules available to generate additional meaningful cases.")
            else:
                per_rule = max(1, additional_needed // len(candidate_rules))
                remaining = additional_needed
                for rule in candidate_rules:
                    count = min(per_rule, remaining)
                    if rule is candidate_rules[-1]:
                        count = remaining
                    if count <= 0:
                        continue
                    additional_batch = self.test_case_generator.generate_test_case_batch(
                        generator_script, rule, count * 3,
                        master_source_code, lang_config["id"], baseline_time, baseline_memory
                    )
                    meaningful_batch = [tc for tc in additional_batch if tc.get("admin_time", 0) >= self.config.TIME_THRESHOLD]
                    meaningful_batch = meaningful_batch[:count]
                    for test_case in meaningful_batch:
                        test_case["test_case_no"] = test_case_counter
                        all_test_cases.append(test_case)
                        test_case_counter += 1
                    remaining -= len(meaningful_batch)
                    print(f"✅ Added {len(meaningful_batch)} meaningful {rule['type']} cases")
                    if remaining <= 0:
                        break
        total_cases = len(all_test_cases)
        visible_cases = sum(1 for tc in all_test_cases if tc.get("is_visible", False))
        hidden_cases = total_cases - visible_cases
        final_meaningful = [tc for tc in all_test_cases if tc.get("admin_time", 0) >= self.config.TIME_THRESHOLD]
        meaningful_count = len(final_meaningful)
        zero_time_cases = sum(1 for tc in all_test_cases if tc.get("admin_time", 0) == 0)
        zero_memory_cases = sum(1 for tc in all_test_cases if tc.get("admin_memory", 0) <= baseline_memory * 0.05)
        admin_times = [tc.get("admin_time", 0) for tc in all_test_cases if tc.get("admin_time") is not None]
        max_admin_time = max(admin_times) if admin_times else 0
        tle_limit = max(1.0, max_admin_time * 3)
        admin_memories = [tc.get("admin_memory", 0) for tc in all_test_cases if tc.get("admin_memory") is not None]
        max_admin_memory = max(admin_memories) if admin_memories else 0
        mle_limit = max(64000, max_admin_memory * 2)
        test_suite_data = {
            "metadata": {
                "problem_name": problem_name,
                "language": language,
                "language_id": lang_config["id"],
                "total_test_cases": total_cases,
                "visible_cases": visible_cases,
                "hidden_cases": hidden_cases,
                "meaningful_cases_for_cm": meaningful_count,
                "time_threshold": self.config.TIME_THRESHOLD,
                "baseline_time": baseline_time,
                "baseline_memory": baseline_memory,
                "zero_time_cases": zero_time_cases,
                "zero_memory_cases": zero_memory_cases,
                "max_admin_time": max_admin_time,
                "max_admin_memory": max_admin_memory,
                "tle_limit": tle_limit,
                "mle_limit": mle_limit,
                "generation_timestamp": time.time()
            },
            "test_cases": all_test_cases
        }
        with open(output_json_file, 'w') as f:
            json.dump(test_suite_data, f, indent=2)
        print(f"\n🎉 {language.upper()} Test suite complete!")
        print(f"📊 Summary:")
        print(f"   Total: {total_cases} cases ({visible_cases} visible, {hidden_cases} hidden)")
        print(f"   Meaningful cases: {meaningful_count} (≥{self.config.TIME_THRESHOLD}s)")
        print(f"   Zero time cases: {zero_time_cases}")
        print(f"   Zero memory cases: {zero_memory_cases}")
        print(f"   Baseline: {baseline_time:.3f}s, {baseline_memory}KB")
        print(f"   Max admin time: {max_admin_time:.3f}s")
        print(f"   Max admin memory: {max_admin_memory}KB")
        print(f"   TLE limit: {tle_limit:.3f}s")
        print(f"   MLE limit: {mle_limit}KB ({mle_limit/1024:.1f}MB)")
        print(f"   Output: '{output_json_file}'")

    def generate_all_languages(self, problem_name):
        for language in self.config.LANGUAGE_CONFIGS.keys():
            print(f"\n{'='*50}")
            print(f"GENERATING FOR {language.upper()}")
            print(f"{'='*50}")
            self.create_json_test_suite(problem_name, language)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Judge0-compatible test suites for a specific problem folder."
    )
    parser.add_argument(
        "language",
        nargs="?",
        default="all",
        help="Language to generate (python, cpp, or 'all'). Defaults to 'all'.",
    )
    parser.add_argument(
        "-p",
        "--problem",
        default=".",
        help="Path to the problem directory (relative to repo root or absolute). Defaults to current working directory.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    repo_root = Path(__file__).resolve().parent
    problem_path = Path(args.problem).expanduser()
    if not problem_path.is_absolute():
        problem_path = (repo_root / problem_path).resolve()
    else:
        problem_path = problem_path.resolve()

    if not problem_path.is_dir():
        print(f"⚠️ Problem directory not found: {problem_path}")
        sys.exit(1)

    problem_name = problem_path.name
    config = Config()
    config.PROBLEMS_DIR = str(problem_path)

    orchestrator = TestSuiteOrchestrator(config=config)
    language = args.language
    if language == "all":
        orchestrator.generate_all_languages(problem_name)
    else:
        orchestrator.create_json_test_suite(problem_name, language)


if __name__ == "__main__":
    main()