#!/usr/bin/env python3
"""
Database export generator for 30_oct problems (problem_01 to problem_05)
Creates the full folder structure with templates, wrappers, and database files
"""

import json
import os
import shutil
from pathlib import Path
import re

def create_output_structure():
    """Create the output directory structure"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def clean_problem_name(problem_name):
    """Convert problem_01_balanced_brackets to balanced_brackets"""
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

def generate_problem_description(source_dir, dest_dir, problem_name, problem_number):
    """Generate problem_description.json"""
    
    # Read description.txt
    desc_file = source_dir / "description.txt"
    with open(desc_file, 'r') as f:
        description_text = f.read()
    
    # Extract title from first line (no # heading in 30_oct format)
    lines = description_text.strip().split('\n')
    title = lines[0].strip()
    
    # Extract sections
    problem_match = re.search(r'(.*?)(?=## Input Format|\Z)', description_text, re.DOTALL)
    problem_statement = problem_match.group(1).strip() if problem_match else ""
    # Remove the title from problem statement
    problem_statement = '\n'.join(problem_statement.split('\n')[1:]).strip()
    
    input_match = re.search(r'## Input Format\s*\n(.*?)(?=\n## |\Z)', description_text, re.DOTALL)
    input_format = input_match.group(1).strip() if input_match else ""
    
    output_match = re.search(r'## Output Format\s*\n(.*?)(?=\n## |\Z)', description_text, re.DOTALL)
    output_format = output_match.group(1).strip() if output_match else ""
    
    constraints_match = re.search(r'## Constraints\s*\n(.*?)(?=\n## |\Z)', description_text, re.DOTALL)
    constraints = constraints_match.group(1).strip() if constraints_match else ""
    
    # Combine description
    description_parts = []
    if problem_statement:
        description_parts.append(problem_statement)
    if input_format:
        description_parts.append(f"## Input Format\n{input_format}")
    if output_format:
        description_parts.append(f"## Output Format\n{output_format}")
    description = "\n\n".join(description_parts)
    
    # Determine difficulty based on problem number
    difficulty = "Easy" if problem_number <= 3 else "Medium"
    
    # Create problem description
    problem_desc = {
        "external_id": str(problem_number),
        "title": title,
        "difficulty": difficulty, 
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
    
    # Write to file
    with open(dest_dir / "problem_description.json", 'w') as f:
        json.dump(problem_desc, f, indent=2, ensure_ascii=False)

def generate_combined_testcase(source_dir, dest_dir, problem_name, problem_number):
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
                    "problem_id": problem_number,
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
                    "problem_id": problem_number,
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
    """Main function to generate complete database export for 30_oct problems"""
    
    print("🚀 Generating Database Export for 30_oct Problems (01-05)")
    
    # Problem list
    problems = [
        ("problem_01_balanced_brackets", 1),
        ("problem_02_directory_tree_lister", 2),
        ("problem_03_matrix_spiral_traversal", 3),
        ("problem_04_minimum_sum_of_products", 4),
        ("problem_05_multi_class_library_system", 5)
    ]
    
    # Create output directory
    output_dir = create_output_structure()
    print(f"📁 Created output directory: {output_dir}")
    
    # Process each problem
    for problem_name, problem_number in problems:
        print(f"\n📋 Processing {problem_name}...")
        
        clean_name = clean_problem_name(problem_name)
        source_dir = Path("30_oct") / problem_name
        dest_dir = output_dir / clean_name
        
        if not source_dir.exists():
            print(f"❌ Source directory not found: {source_dir}")
            continue
            
        # Create destination directory
        dest_dir.mkdir(exist_ok=True)
        
        try:
            # Generate problem description
            generate_problem_description(source_dir, dest_dir, problem_name, problem_number)
            print(f"   ✅ Generated problem_description.json")
            
            # Copy templates and wrappers
            copy_templates_and_wrappers(source_dir, dest_dir)
            print(f"   ✅ Copied templates and wrappers")
            
            # Generate testcases
            generate_combined_testcase(source_dir, dest_dir, problem_name, problem_number)
            print(f"   ✅ Generated testcase.json")
            
            print(f"   🎉 {clean_name} complete!")
            
        except Exception as e:
            print(f"   ❌ Error processing {problem_name}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n🎉 Database export generation complete!")
    print(f"📂 Output structure created in: {output_dir.absolute()}")
    print(f"\n📁 Generated folders:")
    for problem_name, _ in problems:
        clean_name = clean_problem_name(problem_name)
        print(f"   - output/{clean_name}/")

if __name__ == "__main__":
    main()
