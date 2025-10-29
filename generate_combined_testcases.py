#!/usr/bin/env python3
"""
Script to generate combined testcase.json files from Python and C++ testcase files
"""

import json
import os
from pathlib import Path

def load_testcase_file(filepath):
    """Load and parse a testcase JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_problem_id(problem_name):
    """Extract problem ID from problem name like easy_01_hello_user -> 1"""
    return int(problem_name.split('_')[1])

def clean_problem_name(problem_name):
    """Convert easy_01_hello_user to hello_user"""
    parts = problem_name.split('_')
    return '_'.join(parts[2:])

def create_combined_testcase(python_file, cpp_file, output_dir, problem_name):
    """Create combined testcase.json from Python and C++ files"""
    
    # Load both files
    py_data = load_testcase_file(python_file)
    cpp_data = load_testcase_file(cpp_file)
    
    problem_id = extract_problem_id(problem_name)
    
    # Filter test cases to only include up to test_case_no 10
    py_filtered_cases = [tc for tc in py_data["test_cases"] if tc["test_case_no"] <= 10]
    cpp_filtered_cases = [tc for tc in cpp_data["test_cases"] if tc["test_case_no"] <= 10]
    
    # Count visible cases in filtered data
    py_visible_count = sum(1 for tc in py_filtered_cases if tc["is_visible"])
    cpp_visible_count = sum(1 for tc in cpp_filtered_cases if tc["is_visible"])
    
    # Create combined structure
    combined = {
        "languages": [
            {
                "language": "python", 
                "metadata": {
                    "problem_name": problem_name,
                    "problem_id": problem_id,
                    "language_id": py_data["metadata"]["language_id"],
                    "total_test_cases": len(py_filtered_cases),
                    "visible_cases": py_visible_count,
                    "hidden_cases": len(py_filtered_cases) - py_visible_count,
                    "tle_limit": py_data["metadata"]["tle_limit"],
                    "mle_limit": py_data["metadata"]["mle_limit"]
                },
                "test_cases": []
            },
            {
                "language": "cpp",
                "metadata": {
                    "problem_name": problem_name,
                    "problem_id": problem_id,
                    "language_id": cpp_data["metadata"]["language_id"],
                    "total_test_cases": len(cpp_filtered_cases),
                    "visible_cases": cpp_visible_count,
                    "hidden_cases": len(cpp_filtered_cases) - cpp_visible_count,
                    "tle_limit": cpp_data["metadata"]["tle_limit"],
                    "mle_limit": cpp_data["metadata"]["mle_limit"]
                },
                "test_cases": []
            }
        ]
    }
    
    # Add Python test cases (limited to 10)
    for tc in py_filtered_cases:
        combined["languages"][0]["test_cases"].append({
            "test_case_no": tc["test_case_no"],
            "stdin": tc["stdin"],
            "expected_output": tc["expected_output"],
            "is_visible": tc["is_visible"],
            "input_size": tc.get("input_size", 1)
        })
    
    # Add C++ test cases (limited to 10)
    for tc in cpp_filtered_cases:
        combined["languages"][1]["test_cases"].append({
            "test_case_no": tc["test_case_no"],
            "stdin": tc["stdin"],
            "expected_output": tc["expected_output"],
            "is_visible": tc["is_visible"],
            "input_size": tc.get("input_size", 1)
        })
    
    # Write to output directory
    clean_name = clean_problem_name(problem_name)
    output_file = os.path.join(output_dir, clean_name, "testcase.json")
    
    with open(output_file, 'w') as f:
        json.dump(combined, f, indent=2)
    
    print(f"Generated: {output_file} (Python: {len(py_filtered_cases)} cases, C++: {len(cpp_filtered_cases)} cases)")

def main():
    """Main function to process all problems 1-15"""
    base_dir = Path(".")
    output_dir = Path("output")
    
    # Problem mapping
    problems = [
        "easy_31_largest_of_three_numbers",
        "easy_32_factorial_using_loop",
        "easy_33_sum_of_array_of_5_integers",
        "easy_34_student_class_display_details",
        "easy_35_swap_two_numbers_by_reference"
    ]
    
    for problem in problems:
        python_file = base_dir / problem / f"{problem}_python_testcases.json"
        cpp_file = base_dir / problem / f"{problem}_cpp_testcases.json"

        if python_file.exists() and cpp_file.exists():
            create_combined_testcase(python_file, cpp_file, output_dir, problem)
        else:
            missing = []
            if not python_file.exists():
                missing.append("Python")
            if not cpp_file.exists():
                missing.append("C++")
            print(f"Missing {', '.join(missing)} testcase file(s) for {problem}")

if __name__ == "__main__":
    main()