#!/usr/bin/env python3
"""
Script to generate problem_description.json files from description.txt files
"""

import json
import os
import re
from pathlib import Path

def extract_problem_info(description_text, problem_name):
    """Extract problem information from description.txt content"""
    
    # Extract title (first # heading)
    title_match = re.search(r'^# (.+)$', description_text, re.MULTILINE)
    title = title_match.group(1) if title_match else problem_name.replace('_', ' ').title()
    
    # Extract problem statement
    problem_match = re.search(r'## Problem Statement\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    problem_statement = problem_match.group(1).strip() if problem_match else ""
    
    # Extract input format
    input_match = re.search(r'## Input Format\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    input_format = input_match.group(1).strip() if input_match else ""
    
    # Extract output format
    output_match = re.search(r'## Output Format\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    output_format = output_match.group(1).strip() if output_match else ""
    
    # Extract constraints
    constraints_match = re.search(r'## Constraints\s*\n(.*?)(?=\n## |\n```|\Z)', description_text, re.DOTALL)
    constraints = constraints_match.group(1).strip() if constraints_match else ""
    
    # Extract tags (if present)
    # tags = ["Algorithm", "Data Structures", "Problem Solving"]  # Default tags for medium problems
    tags = ["Problem Solving"]
    # Combine description parts
    description_parts = []
    if problem_statement:
        description_parts.append(f"## Problem Statement\n{problem_statement}")
    if input_format:
        description_parts.append(f"## Input Format\n{input_format}")
    if output_format:
        description_parts.append(f"## Output Format\n{output_format}")
    description = "\n\n".join(description_parts)
    
    return title, description, constraints, tags

def extract_problem_id(problem_name):
    """Extract problem ID from problem name like easy_01_hello_user -> 1"""
    return int(problem_name.split('_')[1])

def clean_problem_name(problem_name):
    """Convert easy_01_hello_user to hello_user"""
    parts = problem_name.split('_')
    return '_'.join(parts[2:])

def create_problem_description(description_file, output_dir, problem_name):
    """Create problem_description.json from description.txt"""
    
    with open(description_file, 'r', encoding='utf-8') as f:
        description_text = f.read()
    
    # MODIFIED: Unpack the new 'constraints' variable
    title, description, constraints, tags = extract_problem_info(description_text, problem_name)
    problem_id = extract_problem_id(problem_name)
    clean_name = clean_problem_name(problem_name)
    
    # Create problem description structure
    problem_desc = {
        "external_id": str(problem_id),
        "title": title,
        "difficulty": "Easy",
        "description": description,
        "constraints": constraints,
        "tags": tags,
        "templates": {
            "python_path": "templates/python.py",
            "cpp_path": "templates/cpp.cpp"
        },
        "wrappers": {
            "python_path": "wrappers/wrapper.py",
            "cpp_path": "wrappers/wrapper.cpp"
        }
    }
    
    # Write to output directory
    output_file = os.path.join(output_dir, clean_name, "problem_description.json")
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(problem_desc, f, indent=2, ensure_ascii=False)
    print(f"Generated: {output_file}")

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
        description_file = base_dir / problem / "description.txt"
        
        if description_file.exists():
            create_problem_description(description_file, output_dir, problem)
        else:
            print(f"Missing description.txt for {problem}")

if __name__ == "__main__":
    main()
