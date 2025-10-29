#!/usr/bin/env python3
"""
Convert 31_oct_level_2 problems to 31_oct_2_level format
Matches the structure of 30_oct_level_2 and 31_oct_level_3
"""

import os
import json
import shutil

SOURCE_DIR = "31_oct_level_2"
TARGET_DIR = "31_oct_2_level"

# Mapping of problem folders to their IDs and clean names
PROBLEMS = [
    {
        "source": "problem_14_merge_overlapping_intervals",
        "target": "merge_overlapping_intervals",
        "external_id": "14",
        "title": "Merge Overlapping Intervals",
        "difficulty": "Easy"
    },
    {
        "source": "problem_15_number_of_islands",
        "target": "number_of_islands",
        "external_id": "15",
        "title": "Number of Islands",
        "difficulty": "Medium"
    },
    {
        "source": "problem_16_product_of_array_except_self",
        "target": "product_of_array_except_self",
        "external_id": "16",
        "title": "Product of Array Except Self",
        "difficulty": "Medium"
    },
    {
        "source": "problem_17_top_k_frequent_elements",
        "target": "top_k_frequent_elements",
        "external_id": "17",
        "title": "Top K Frequent Elements",
        "difficulty": "Medium"
    },
    {
        "source": "problem_18_elevator_control_system",
        "target": "elevator_control_system",
        "external_id": "18",
        "title": "Elevator Control System",
        "difficulty": "Hard"
    }
]

def extract_description_from_txt(desc_file):
    """Extract description from description.txt format"""
    with open(desc_file, 'r') as f:
        content = f.read()
    
    # Extract title (first line)
    lines = content.strip().split('\n')
    title = lines[0].strip()
    
    # Find the main description (before ## Input Format)
    parts = content.split('## Input Format')
    main_desc = parts[0].strip()
    # Remove the title from main_desc
    main_desc = '\n'.join(main_desc.split('\n')[1:]).strip()
    
    # Extract Input Format
    input_format = ""
    if len(parts) > 1:
        input_parts = parts[1].split('## Output Format')
        if input_parts[0].strip():
            input_format = input_parts[0].strip()
    
    # Extract Output Format
    output_format = ""
    if '## Output Format' in content:
        output_parts = content.split('## Output Format')[1].split('## Constraints')
        if output_parts[0].strip():
            output_format = output_parts[0].strip()
    
    # Extract Constraints
    constraints = ""
    if '## Constraints' in content:
        const_parts = content.split('## Constraints')[1].split('## Sample')[0]
        constraints = const_parts.strip()
    
    # Build full description
    full_desc = main_desc
    if input_format:
        full_desc += "\n\n## Input Format\n" + input_format
    if output_format:
        full_desc += "\n\n## Output Format\n" + output_format
    
    return full_desc, constraints

def convert_testcases(python_testcase_file, cpp_testcase_file, external_id):
    """Convert testcase JSONs to combined format"""
    with open(python_testcase_file, 'r') as f:
        python_data = json.load(f)
    
    with open(cpp_testcase_file, 'r') as f:
        cpp_data = json.load(f)
    
    # Build combined testcase.json
    combined = {
        "languages": [
            {
                "language": "python",
                "metadata": {
                    "problem_name": python_data["metadata"]["problem_name"],
                    "problem_id": int(external_id),
                    "language_id": python_data["metadata"]["language_id"],
                    "total_test_cases": python_data["metadata"]["total_test_cases"],
                    "visible_cases": python_data["metadata"]["visible_cases"],
                    "hidden_cases": python_data["metadata"]["hidden_cases"],
                    "tle_limit": python_data["metadata"]["tle_limit"],
                    "mle_limit": python_data["metadata"]["mle_limit"]
                },
                "test_cases": []
            },
            {
                "language": "cpp",
                "metadata": {
                    "problem_name": cpp_data["metadata"]["problem_name"],
                    "problem_id": int(external_id),
                    "language_id": cpp_data["metadata"]["language_id"],
                    "total_test_cases": cpp_data["metadata"]["total_test_cases"],
                    "visible_cases": cpp_data["metadata"]["visible_cases"],
                    "hidden_cases": cpp_data["metadata"]["hidden_cases"],
                    "tle_limit": cpp_data["metadata"]["tle_limit"],
                    "mle_limit": cpp_data["metadata"]["mle_limit"]
                },
                "test_cases": []
            }
        ]
    }
    
    # Add Python test cases
    for tc in python_data["test_cases"]:
        combined["languages"][0]["test_cases"].append({
            "test_case_no": tc["test_case_no"],
            "stdin": tc["stdin"],
            "expected_output": tc["expected_output"],
            "is_visible": tc["is_visible"],
            "input_size": tc.get("input_size", 1)
        })
    
    # Add C++ test cases
    for tc in cpp_data["test_cases"]:
        combined["languages"][1]["test_cases"].append({
            "test_case_no": tc["test_case_no"],
            "stdin": tc["stdin"],
            "expected_output": tc["expected_output"],
            "is_visible": tc["is_visible"],
            "input_size": tc.get("input_size", 1)
        })
    
    return combined

def convert_template(template_file, comment_style="python"):
    """Convert template to simplified format"""
    with open(template_file, 'r') as f:
        content = f.read()
    
    # For Python, add TODO comment
    if comment_style == "python":
        # Find the return statement and add TODO before it
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if 'return' in line and '"""' not in line:
                indent = len(line) - len(line.lstrip())
                new_lines.append(' ' * indent + '# TODO: Implement solution logic')
            new_lines.append(line)
        return '\n'.join(new_lines)
    else:
        # For C++, keep as is (declaration only)
        return content

def convert_problem(problem_info):
    """Convert a single problem"""
    source_path = os.path.join(SOURCE_DIR, problem_info["source"])
    target_path = os.path.join(TARGET_DIR, problem_info["target"])
    
    print(f"Converting {problem_info['source']} -> {problem_info['target']}")
    
    # Create target directory structure
    os.makedirs(target_path, exist_ok=True)
    os.makedirs(os.path.join(target_path, "templates"), exist_ok=True)
    os.makedirs(os.path.join(target_path, "wrappers"), exist_ok=True)
    
    # 1. Create problem_description.json
    desc_file = os.path.join(source_path, "description.txt")
    description, constraints = extract_description_from_txt(desc_file)
    
    problem_desc = {
        "external_id": problem_info["external_id"],
        "title": problem_info["title"],
        "difficulty": problem_info["difficulty"],
        "description": description,
        "constraints": constraints,
        "tags": ["Problem Solving", "Algorithm"],
        "templates": {
            "python_path": "templates/python.py",
            "cpp_path": "templates/cpp.cpp"
        },
        "wrappers": {
            "python_path": "wrappers/wrapper.py",
            "cpp_path": "wrappers/wrapper.cpp"
        }
    }
    
    with open(os.path.join(target_path, "problem_description.json"), 'w') as f:
        json.dump(problem_desc, f, indent=2)
    
    # 2. Convert and combine testcases
    python_tc = os.path.join(source_path, f"{problem_info['source']}_python_testcases.json")
    cpp_tc = os.path.join(source_path, f"{problem_info['source']}_cpp_testcases.json")
    
    testcases = convert_testcases(python_tc, cpp_tc, problem_info["external_id"])
    
    with open(os.path.join(target_path, "testcase.json"), 'w') as f:
        json.dump(testcases, f, indent=2)
    
    # 3. Copy and convert templates
    py_template_src = os.path.join(source_path, "template.py")
    py_template_dst = os.path.join(target_path, "templates", "python.py")
    with open(py_template_src, 'r') as f:
        template_content = f.read()
    template_content = convert_template(py_template_src, "python")
    with open(py_template_dst, 'w') as f:
        f.write(template_content)
    
    cpp_template_src = os.path.join(source_path, "template.cpp")
    cpp_template_dst = os.path.join(target_path, "templates", "cpp.cpp")
    shutil.copy2(cpp_template_src, cpp_template_dst)
    
    # 4. Copy wrappers (they should already be correct)
    py_wrapper_src = os.path.join(source_path, "wrapper.py")
    py_wrapper_dst = os.path.join(target_path, "wrappers", "wrapper.py")
    shutil.copy2(py_wrapper_src, py_wrapper_dst)
    
    cpp_wrapper_src = os.path.join(source_path, "wrapper.cpp")
    cpp_wrapper_dst = os.path.join(target_path, "wrappers", "wrapper.cpp")
    shutil.copy2(cpp_wrapper_src, cpp_wrapper_dst)
    
    print(f"  ✓ Created {target_path}")

def main():
    """Main conversion process"""
    print("="*60)
    print("Converting 31_oct_level_2 to 31_oct_2_level format")
    print("="*60)
    print()
    
    # Create target directory
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # Convert each problem
    for problem in PROBLEMS:
        convert_problem(problem)
        print()
    
    print("="*60)
    print("✓ Conversion complete!")
    print("="*60)
    print()
    print(f"Created {TARGET_DIR}/ with structure:")
    print("├── merge_overlapping_intervals/")
    print("├── number_of_islands/")
    print("├── product_of_array_except_self/")
    print("├── top_k_frequent_elements/")
    print("└── elevator_control_system/")
    print()
    print("Each contains:")
    print("  ├── problem_description.json")
    print("  ├── testcase.json")
    print("  ├── templates/")
    print("  │   ├── python.py")
    print("  │   └── cpp.cpp")
    print("  └── wrappers/")
    print("      ├── wrapper.py")
    print("      └── wrapper.cpp")

if __name__ == "__main__":
    main()
