#!/usr/bin/env python3
"""
Platform Code Injection - Working Example

This script demonstrates injection with a completed solution to show
the full end-to-end process.
"""

import os
import tempfile
import subprocess

def create_working_solution():
    """Create a working solution for hello_user problem"""
    return '''class Solution:
    def greetUser(self, name):
        """
        :type name: str
        :rtype: str
        """
        return f"Hello, {name}!"'''

def create_working_cpp_solution():
    """Create a working C++ solution for hello_user problem"""
    return '''class Solution {
public:
    string greetUser(string name) {
        return "Hello, " + name + "!";
    }
};'''

def inject_and_test():
    """
    Inject working solution and test it
    """
    print("=== INJECTION WITH WORKING SOLUTION ===\n")
    
    # Read the wrapper
    with open("output/hello_user/wrappers/wrapper.py", 'r') as f:
        wrapper_content = f.read()
    
    # Create working solution
    working_solution = create_working_solution()
    
    print("1. WORKING SOLUTION CODE:")
    print("-" * 40)
    print(working_solution)
    print()
    
    # Inject solution
    placeholder = "# Contestant's solution will be inserted/imported here by the platform\n# from solution import Solution"
    injection = f"# Contestant's solution injected by platform\n{working_solution}"
    complete_code = wrapper_content.replace(placeholder, injection)
    
    print("2. COMPLETE INJECTED FILE:")
    print("-" * 40)
    print(complete_code)
    print()
    
    # Test with multiple inputs
    test_cases = [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("Charlie Brown", "Hello, Charlie Brown!")
    ]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save injected file
        injected_file = os.path.join(temp_dir, "complete_solution.py")
        with open(injected_file, 'w') as f:
            f.write(complete_code)
        
        print("3. TESTING WITH MULTIPLE INPUTS:")
        print("-" * 40)
        
        for test_input, expected in test_cases:
            try:
                result = subprocess.run(
                    ['python', injected_file],
                    input=test_input,
                    text=True,
                    capture_output=True,
                    cwd=temp_dir
                )
                
                if result.returncode == 0:
                    actual_output = result.stdout.strip()
                    status = "✅ PASS" if actual_output == expected else "❌ FAIL"
                    print(f"{status} | Input: '{test_input}' | Expected: '{expected}' | Got: '{actual_output}'")
                else:
                    print(f"❌ ERROR | Input: '{test_input}' | stderr: {result.stderr}")
                    
            except Exception as e:
                print(f"❌ EXCEPTION | Input: '{test_input}' | {e}")

def show_judge0_submission_format():
    """
    Show the exact format that would be sent to Judge0
    """
    print("\n=== JUDGE0 SUBMISSION FORMAT ===\n")
    
    # Read wrapper and inject solution
    with open("output/hello_user/wrappers/wrapper.py", 'r') as f:
        wrapper_content = f.read()
    
    working_solution = create_working_solution()
    placeholder = "# Contestant's solution will be inserted/imported here by the platform\n# from solution import Solution"
    injection = f"# Contestant's solution injected by platform\n{working_solution}"
    complete_code = wrapper_content.replace(placeholder, injection)
    
    # Sample Judge0 submission
    judge0_submission = {
        "language_id": 71,  # Python
        "source_code": complete_code,
        "stdin": "Alice",
        "expected_output": "Hello, Alice!"
    }
    
    print("JUDGE0 API REQUEST FORMAT:")
    print("-" * 30)
    print(f"Language ID: {judge0_submission['language_id']} (Python)")
    print(f"Input: {judge0_submission['stdin']}")
    print(f"Expected: {judge0_submission['expected_output']}")
    print(f"Source Code Length: {len(judge0_submission['source_code'])} characters")
    print()
    print("Source Code Preview:")
    print("```python")
    print(complete_code[:200] + "..." if len(complete_code) > 200 else complete_code)
    print("```")

def show_platform_integration():
    """
    Show how this integrates with the platform
    """
    print("\n=== PLATFORM INTEGRATION ===\n")
    
    integration_flow = """
    ┌─────────────────┐
    │   CONTESTANT    │
    │   Fills Template│
    └─────────┬───────┘
              │
              ▼
    ┌─────────────────┐
    │    PLATFORM     │
    │ • Reads Template│
    │ • Reads Wrapper │
    │ • Injects Code  │
    └─────────┬───────┘
              │
              ▼
    ┌─────────────────┐
    │     JUDGE0      │
    │ • Compiles Code │
    │ • Runs Tests    │
    │ • Returns Result│
    └─────────┬───────┘
              │
              ▼
    ┌─────────────────┐
    │    PLATFORM     │
    │ • Processes     │
    │   Results       │
    │ • Shows Verdict │
    └─────────────────┘
    """
    
    print(integration_flow)
    
    print("\nKEY BENEFITS OF THIS APPROACH:")
    print("=" * 40)
    print("1. ✅ Separation of Concerns:")
    print("   - Contestants focus on algorithm logic")
    print("   - Platform handles I/O and execution")
    print()
    print("2. ✅ Consistent I/O Handling:")
    print("   - All problems use standardized wrappers")
    print("   - No I/O mistakes by contestants")
    print()
    print("3. ✅ Security:")
    print("   - Contestants can't access system functions")
    print("   - Controlled execution environment")
    print()
    print("4. ✅ Easy Testing:")
    print("   - Platform can test solutions automatically")
    print("   - Consistent output format")

if __name__ == "__main__":
    os.chdir("/home/rishabh/coding_questions/normal")
    inject_and_test()
    show_judge0_submission_format()
    show_platform_integration()