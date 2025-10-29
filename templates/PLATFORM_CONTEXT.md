# Platform Context: Judge0-Based Competitive Programming System

## Quick Reference: Canonical Examples in 30_oct/
All templates and patterns described in this document are based on **actual working problems** in the `30_oct/` directory. When in doubt, refer to these 5 production-ready problems:

1. **problem_01_balanced_brackets** - String validation with stack algorithm
2. **problem_02_directory_tree_lister** - JSON parsing and tree traversal
3. **problem_03_matrix_spiral_traversal** - 2D array manipulation
4. **problem_04_minimum_sum_of_products** - Array sorting and pairing optimization
5. **problem_05_multi_class_library_system** - Multi-command OOP simulation with EXIT terminator

Use these as templates when creating new problems. They contain validated, tested, and orchestrator-compatible implementations.

## 🎯 Purpose
The PLATFORM_CONTEXT.md file contains ALL context needed for AI agents to generate complete problem folders from just a problem description. Point new chats to this file + provide problem description = complete problem generation.

Quick decision helper: See `./QUICK_CHECKLIST.md` for a fast pattern selection rubric (easy_33 vs easy_34) and a concise multiclass OOP design checklist.

## 📁 Platform Architecture

### Problem Folder Structure (EXACTLY 8 files required)
```
{difficulty}_{number}_{problem_title}/
├── description.txt     # Problem statement with natural method integration
├── solution.py         # Master solution (Python) with Solution class
├── solution.cpp        # Master solution (C++) with Solution class  
├── template.py         # Contestant starting code (Python)
├── template.cpp        # Contestant starting code (C++)
├── wrapper.py          # I/O handler for Judge0 (Python)
├── wrapper.cpp         # I/O handler for Judge0 (C++)
├── generator.py        # Random test case generator
├── config.json         # Generation buckets for orchestrator
└── examples.json       # Sample test cases in Judge0 format
```

### Naming Convention
- Format: `{difficulty}_{number:02d}_{snake_case_title}`
- Title: snake_case (e.g., `filter_positive_numbers_from_a_list`)
- Examples: `easy_01_hello_world`, `medium_15_binary_search`, `hard_42_graph_traversal`

## 🔧 Critical Design Patterns

### 1. Solution Class Pattern (MANDATORY)
**Every problem MUST follow this exact pattern:**

**Python Solutions:**
```python
class Solution:
    def methodName(self, params):
        """
        :type param1: type
        :rtype: return_type
        """
        # Implementation here
        return result

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    # Parse input
    # Create solution instance
    solution = Solution()
    result = solution.methodName(parsed_params)
    # Write output
```

**C++ Solutions:**
```cpp
class Solution {
public:
    returnType methodName(const paramType& param) {
        // Implementation here
        return result;
    }
};

void solve(std::istream& in = std::cin, std::ostream& out = std::cout) {
    // Parse input
    // Create solution instance
    Solution solution;
    auto result = solution.methodName(parsed_params);
    // Write output
}
```

### 2. Description Style (Natural Integration)
**DO THIS:**
```markdown
## Problem Statement
Write a function `methodName` that takes X and returns Y...
```

**NOT THIS:**
```markdown
**Required Method**: `methodName(params)` - This method must be implemented...
```

### 3. Template Simplification
- Templates should have clean Solution class with method signature
- Use `raise NotImplementedError` (Python) or `throw std::logic_error("Not implemented")` (C++)
- NO implementation hints or helper code

### 4. Cross-File Method Consistency
**Critical**: The SAME method name must appear in:
- `description.txt` (naturally integrated)
- `template.py` and `template.cpp` (method signatures)
- `solution.py` and `solution.cpp` (implementations)
- `wrapper.py` and `wrapper.cpp` (method calls)

## 🔍 Judge0 Integration Requirements

### Language Settings
- Python: Language ID 71
- C++: Language ID 54

### Orchestrator-Compatible Formats (30_oct/ Standard)

**config.json** (EXACT format - no args unless needed):
```json
{
  "generation_logic": [
    {"type": "edge_cases", "count": 5, "args": {}},
    {"type": "small", "count": 10, "args": {}},
    {"type": "medium", "count": 15, "args": {}},
    {"type": "large", "count": 15, "args": {}},
    {"type": "stress", "count": 10, "args": {}}
  ]
}
```

**examples.json** (stdin/expected_output/visibility):
```json
[
  {
    "stdin": "input_data\n",
    "expected_output": "output_data\n",
    "visibility": "visible"
  }
]
```

**generator.py** (command-line tool, outputs INPUT only):
```python
import random
import json

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        # Return edge case input
        return "edge_input\n"
    elif rule_type == "small":
        # Return small test input
        return "small_input\n"
    # ... handle other rule types
    
    raise ValueError(f"Unhandled rule_type: {rule_type}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_type")
    parser.add_argument("--args", type=json.loads, default="{}")
    parser.add_argument("--rng-seed", type=int, default=None)
    ns = parser.parse_args()
    if ns.rng_seed is not None:
        ns.args["seed"] = ns.rng_seed
    print(generate_case(ns.rule_type, ns.args), end="")
```

**solution.py** (standalone program with solve() function):
```python
from typing import TextIO
import sys

class Solution:
    def methodName(self, param):
        """
        :type param: type
        :rtype: return_type
        """
        # Implementation
        return result

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Called by orchestrator via Judge0"""
    data = infile.read().strip()
    solution = Solution()
    result = solution.methodName(data)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
```

**wrapper.py** (injection point + execute_solution):
```python
import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        data = input().strip()
        solution = Solution()
        result = solution.methodName(data)
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
```

**template.py** (minimal LeetCode-style):
```python
class Solution:
    def methodName(self, param):
        """
        :type param: type
        :rtype: return_type
        """
        # TODO: Implement the solution logic here
        return None
```

**solution.cpp** (standalone with using namespace std at top):
```cpp
using namespace std;
#include <iostream>
#include <vector>

class Solution {
public:
    returnType methodName(const paramType& param) {
        // Implementation
        return result;
    }
};

int main() {
    // Parse input
    Solution sol;
    auto result = sol.methodName(data);
    cout << result << endl;
    return 0;
}
```

**wrapper.cpp** (injection point + main):
```cpp
#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    // Parse input
    Solution sol;
    auto result = sol.methodName(data);
    cout << result << endl;
    return 0;
}
```

**template.cpp** (minimal, NO includes):
```cpp
class Solution {
public:
    // TODO: Add method signature and implementation
    returnType methodName(const paramType& param) {
        return defaultValue;
    }
};
```
- ONLY stdin/stdout (no file I/O)

### I/O Pattern
- Solutions use dependency injection: `solve(infile, outfile)`
- Wrappers handle platform integration and call Solution methods
- All test execution through Judge0 API

## 📋 File Generation Checklist

When generating a new problem:

### ✅ Phase 1: Core Analysis
1. **Extract method name** from problem description
2. **Identify input/output patterns** (single value, list, multiple inputs, etc.)
3. **Determine parameter types** for Solution class method

### ✅ Phase 2: File Generation (use templates as base)
1. **description.txt** - Natural method integration, clear examples
2. **solution.py/cpp** - Working implementations with Solution class
3. **template.py/cpp** - Clean starting code for contestants
4. **wrapper.py/cpp** - I/O handling calling Solution methods
5. **generator.py** - Test case generation matching config buckets
6. **config.json** - Generation rules (edge/small/medium/large buckets)
7. **examples.json** - Sample cases matching description

### ✅ Phase 3: Validation
1. **Method name consistency** across all files
2. **Basic functionality test** with example inputs
3. **Cross-language compatibility** (Python and C++)

## 🎨 Example Reference Problems (30_oct/ Canonical Examples)
Use these **production-ready, orchestrator-validated** problems as templates:

### problem_01_balanced_brackets
- **Pattern**: String validation with stack algorithm
- **Input**: Single line string
- **Output**: "true" or "false"
- **Key Learning**: Simple boolean return, wrapper converts to string output

### problem_02_directory_tree_lister  
- **Pattern**: JSON parsing and recursive tree traversal
- **Input**: JSON dictionary on single line
- **Output**: Multi-line tree with indentation
- **Key Learning**: Complex input parsing, formatted multi-line output

### problem_03_matrix_spiral_traversal
- **Pattern**: 2D array manipulation
- **Input**: Dimensions + matrix rows
- **Output**: Space-separated spiral order
- **Key Learning**: Multi-line input parsing, array transformation

### problem_04_minimum_sum_of_products
- **Pattern**: Array sorting and optimization
- **Input**: Two space-separated arrays
- **Output**: Single integer
- **Key Learning**: Multiple array inputs, sorting strategy

### problem_05_multi_class_library_system
- **Pattern**: Multi-command OOP simulation
- **Input**: Commands until "EXIT" terminator
- **Output**: Multiple result lines
- **Key Learning**: Command parsing, state management, EXIT terminator, multi-line output

**When creating new problems**: Pick the closest pattern from above and adapt it!

## 🚀 Generation Workflow for New Chat

### Input Required:
1. **This context file**: `./templates/PLATFORM_CONTEXT.md`
2. **Templates folder**: `./templates/` (all template files)
3. **Project documentation**: `./.github/README.md`
3. **Problem description**: Natural language description of the problem

### Expected Output:
Complete problem folder with all 8 files, ready for Judge0 testing.

### Quality Standards:
- All files compile/run without errors
- Method names consistent across all files
- Examples work correctly
- Generator produces valid test cases
- Ready for orchestrator.py execution

## 🔧 Common Patterns by Problem Type

### Single Input → Single Output
- Method: `methodName(input) -> output`
- Examples: sum of digits, factorial, prime check

### Single Input → List Output  
- Method: `methodName(input) -> List[type]`
- Examples: fibonacci sequence, prime factors

### List Input → List Output
- Method: `methodName(List[type]) -> List[type]`  
- Examples: filter positive, sort array

### Multiple Inputs → Single Output
- Method: `methodName(input1, input2) -> output`
- Examples: string contains substring, GCD

### String Processing
- Method: `methodName(string) -> result`
- Examples: longest word, palindrome check

## 💡 Pro Tips
1. **Start with templates** - modify rather than create from scratch
2. **Method name extraction** is critical - look for verbs in problem description
3. **Test immediately** - verify basic functionality before declaring complete
4. **Judge0 ready** - all solutions must work with stdin/stdout only
5. **Competitive style** - follow LeetCode/HackerRank conventions

---
*The PLATFORM_CONTEXT.md file contains everything needed to generate perfect competitive programming problems. Update it as patterns evolve.*
