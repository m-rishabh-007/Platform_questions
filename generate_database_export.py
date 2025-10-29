#!/usr/bin/env python3
"""
Complete database export generator for medium problems 26-30
Creates the full folder structure with templates, wrappers, and database files
"""

import json
import os
import shutil
from pathlib import Path

def create_output_structure():
    """Create the output directory structure"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def clean_problem_name(problem_name):
    """Convert medium_26_analysis_of_sorting... to analysis_of_sorting..."""
    parts = problem_name.split('_')
    return '_'.join(parts[2:])

def copy_templates_and_wrappers(source_dir, dest_dir):
    """Copy template and wrapper files to destination"""
    
    # Create subdirectories
    templates_dir = dest_dir / "templates"
    wrappers_dir = dest_dir / "wrappers" 
    templates_dir.mkdir(exist_ok=True)
    wrappers_dir.mkdir(exist_ok=True)
    
    # Copy Python template
    shutil.copy2(source_dir / "template.py", templates_dir / "python.py")
    
    # Copy C++ template  
    shutil.copy2(source_dir / "template.cpp", templates_dir / "cpp.cpp")
    
    # Copy Python wrapper
    shutil.copy2(source_dir / "wrapper.py", wrappers_dir / "wrapper.py")
    
    # Copy C++ wrapper
    shutil.copy2(source_dir / "wrapper.cpp", wrappers_dir / "wrapper.cpp")

def generate_problem_description(source_dir, dest_dir, problem_name):
    """Generate problem_description.json"""
    
    # Read description.txt
    desc_file = source_dir / "description.txt"
    with open(desc_file, 'r') as f:
        description_text = f.read()
    
    # Extract title from first # heading
    import re
    title_match = re.search(r'^# (.+)$', description_text, re.MULTILINE)
    title = title_match.group(1) if title_match else problem_name.replace('_', ' ').title()
    
    # Extract sections
    problem_match = re.search(r'## Problem Statement\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    problem_statement = problem_match.group(1).strip() if problem_match else ""
    
    input_match = re.search(r'## Input Format\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    input_format = input_match.group(1).strip() if input_match else ""
    
    output_match = re.search(r'## Output Format\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    output_format = output_match.group(1).strip() if output_match else ""
    
    constraints_match = re.search(r'## Constraints\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    constraints = constraints_match.group(1).strip() if constraints_match else ""
    
    # Combine description
    description_parts = []
    if problem_statement:
        description_parts.append(f"## Problem Statement\n{problem_statement}")
    if input_format:
        description_parts.append(f"## Input Format\n{input_format}")
    if output_format:
        description_parts.append(f"## Output Format\n{output_format}")
    description = "\n\n".join(description_parts)
    
    # Extract problem ID
    problem_id = int(problem_name.split('_')[1])
    
    # Create problem description
    problem_desc = {
        "external_id": str(problem_id),
        "title": title,
        "difficulty": "Medium", 
        "description": description,
        "constraints": constraints,
        "tags": ["Algorithm", "Data Structures", "Problem Solving"],
        "templates": {
            "python_path": "templates/python.py",
            "cpp_path": "templates/cpp.cpp"
        },
        "wrappers": {
            "python_path": "wrappers/wrapper.py",
            "cpp_path": "wrappers/wrapper.cpp"
        }
    }
    
    # Write to file
    with open(dest_dir / "problem_description.json", 'w') as f:
        json.dump(problem_desc, f, indent=2, ensure_ascii=False)

def generate_combined_testcase(source_dir, dest_dir, problem_name):
    """Generate combined testcase.json"""
    
    # Find testcase files
    python_file = source_dir / f"{problem_name}_python_testcases.json"
    cpp_file = source_dir / f"{problem_name}_cpp_testcases.json"
    
    if not (python_file.exists() and cpp_file.exists()):
        print(f"❌ Missing testcase files for {problem_name}")
        return
    
    # Load testcase data
    with open(python_file, 'r') as f:
        py_data = json.load(f)
    with open(cpp_file, 'r') as f:
        cpp_data = json.load(f)
    
    problem_id = int(problem_name.split('_')[1])
    
    # Filter to first 10 test cases
    py_filtered_cases = [tc for tc in py_data["test_cases"] if tc["test_case_no"] <= 10]
    cpp_filtered_cases = [tc for tc in cpp_data["test_cases"] if tc["test_case_no"] <= 10]
    
    # Count visible cases
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
    
    # Add test cases
    for tc in py_filtered_cases:
        combined["languages"][0]["test_cases"].append({
            "test_case_no": tc["test_case_no"],
            "stdin": tc["stdin"],
            "expected_output": tc["expected_output"],
            "is_visible": tc["is_visible"],
            "input_size": tc.get("input_size", 1)
        })
    
    for tc in cpp_filtered_cases:
        combined["languages"][1]["test_cases"].append({
            "test_case_no": tc["test_case_no"],
            "stdin": tc["stdin"],
            "expected_output": tc["expected_output"],
            "is_visible": tc["is_visible"],
            "input_size": tc.get("input_size", 1)
        })
    
    # Write to file
    with open(dest_dir / "testcase.json", 'w') as f:
        json.dump(combined, f, indent=2)

def main():
    """Main function to generate complete database export"""
    
    print("🚀 Generating Database Export for Medium Problems 26-30")
    
    # Problem list
    problems = [
        "medium_26_analysis_of_sorting_algorithm_performance_metrics",
        "medium_27_emirp_number_generation_within_a_range", 
        "medium_28_generalized_k_nacci_sequence_summation",
        "medium_29_uniform_data_partitioning_strategy",
        "medium_30_class_based_vending_machine_model"
    ]
    
    # Create output directory
    output_dir = create_output_structure()
    print(f"📁 Created output directory: {output_dir}")
    
    # Process each problem
    for problem in problems:
        print(f"\n📋 Processing {problem}...")
        
        clean_name = clean_problem_name(problem)
        source_dir = Path(problem)
        dest_dir = output_dir / clean_name
        
        if not source_dir.exists():
            print(f"❌ Source directory not found: {source_dir}")
            continue
            
        # Create destination directory
        dest_dir.mkdir(exist_ok=True)
        
        try:
            # Generate problem description
            generate_problem_description(source_dir, dest_dir, problem)
            print(f"   ✅ Generated problem_description.json")
            
            # Copy templates and wrappers
            copy_templates_and_wrappers(source_dir, dest_dir)
            print(f"   ✅ Copied templates and wrappers")
            
            # Generate testcases
            generate_combined_testcase(source_dir, dest_dir, problem)
            print(f"   ✅ Generated testcase.json")
            
            print(f"   🎉 {clean_name} complete!")
            
        except Exception as e:
            print(f"   ❌ Error processing {problem}: {e}")
    
    print(f"\n🎉 Database export generation complete!")
    print(f"📂 Output structure created in: {output_dir.absolute()}")

if __name__ == "__main__":
    main()