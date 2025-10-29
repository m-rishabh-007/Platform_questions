#!/usr/bin/env python3
"""
Quick verification script for 31_oct_level_2 problems
Tests that all generators, solutions, and examples work correctly
"""

import os
import subprocess
import sys
import json

PROBLEMS = [
    "problem_14_merge_overlapping_intervals",
    "problem_15_number_of_islands",
    "problem_16_product_of_array_except_self",
    "problem_17_top_k_frequent_elements",
    "problem_18_elevator_control_system",
]

BASE_DIR = "31_oct_level_2"

def test_problem(problem_name):
    """Test a single problem"""
    print(f"\n{'='*60}")
    print(f"Testing: {problem_name}")
    print('='*60)
    
    problem_dir = os.path.join(BASE_DIR, problem_name)
    os.chdir(problem_dir)
    
    # 1. Test generator
    print("\n1. Testing generator...")
    try:
        result = subprocess.run(
            ["python3", "generator.py", "edge_cases", "--rng-seed", "42"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode != 0:
            print(f"   ❌ Generator failed: {result.stderr}")
            return False
        print(f"   ✓ Generator works (produced {len(result.stdout)} bytes)")
    except Exception as e:
        print(f"   ❌ Generator error: {e}")
        return False
    
    # 2. Test examples
    print("\n2. Testing examples...")
    try:
        with open("examples.json", 'r') as f:
            examples = json.load(f)
        
        for i, example in enumerate(examples[:2], 1):  # Test first 2 examples
            stdin = example["stdin"].replace("\\n", "\n")
            expected = example["expected_output"].replace("\\n", "\n")
            
            # Test Python
            result = subprocess.run(
                ["python3", "solution.py"],
                input=stdin,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.stdout != expected:
                print(f"   ❌ Python example {i} failed")
                print(f"      Expected: {repr(expected)}")
                print(f"      Got:      {repr(result.stdout)}")
                return False
            
            print(f"   ✓ Python example {i} passed")
            
            # Compile and test C++
            compile_result = subprocess.run(
                ["g++", "-o", "solution_test", "solution.cpp"],
                capture_output=True,
                timeout=10
            )
            
            if compile_result.returncode != 0:
                print(f"   ❌ C++ compilation failed: {compile_result.stderr.decode()}")
                return False
            
            result = subprocess.run(
                ["./solution_test"],
                input=stdin,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.stdout != expected:
                print(f"   ❌ C++ example {i} failed")
                print(f"      Expected: {repr(expected)}")
                print(f"      Got:      {repr(result.stdout)}")
                return False
            
            print(f"   ✓ C++ example {i} passed")
            
            # Cleanup
            if os.path.exists("solution_test"):
                os.remove("solution_test")
        
    except Exception as e:
        print(f"   ❌ Example test error: {e}")
        return False
    
    # 3. Check file structure
    print("\n3. Checking file structure...")
    required_files = [
        "description.txt", "template.py", "template.cpp",
        "solution.py", "solution.cpp", "wrapper.py", "wrapper.cpp",
        "generator.py", "config.json", "examples.json"
    ]
    
    missing = []
    for filename in required_files:
        if not os.path.exists(filename):
            missing.append(filename)
    
    if missing:
        print(f"   ❌ Missing files: {', '.join(missing)}")
        return False
    
    print(f"   ✓ All 10 required files present")
    
    return True

def main():
    """Run all tests"""
    original_dir = os.getcwd()
    
    print("\n" + "="*60)
    print("31_oct_level_2 Problems Verification")
    print("="*60)
    
    results = {}
    
    for problem in PROBLEMS:
        os.chdir(original_dir)
        results[problem] = test_problem(problem)
    
    # Summary
    os.chdir(original_dir)
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for problem, result in results.items():
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {problem}")
    
    print(f"\nTotal: {passed}/{total} problems passed")
    
    if passed == total:
        print("\n🎉 All problems verified successfully!")
        print("\nNext steps:")
        print("  1. Run smoke tests from templates/smoke_test.md")
        print("  2. Generate test suites with orchestrator.py")
        return 0
    else:
        print("\n⚠️  Some problems need attention")
        return 1

if __name__ == "__main__":
    sys.exit(main())
