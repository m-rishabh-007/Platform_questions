# Templates Directory

This directory contains template files for creating new competitive programming problems. All templates are based on the **30_oct/ canonical examples** which are production-ready, orchestrator-validated problems.

## Template Files (10 total)

### Core Configuration
- **config_template.json** - Generation rules for orchestrator (edge_cases, small, medium, large, stress)
- **examples_template.json** - Sample test cases in stdin/expected_output/visibility format

### Code Templates
- **generator_template.py** - Command-line test case generator (outputs INPUT only)
- **solution_template.py** - Reference solution with Solution class and solve() function
- **solution_template.cpp** - C++ reference solution with main() function
- **template_template.py** - Contestant starting code (Python, minimal)
- **template_template.cpp** - Contestant starting code (C++, NO includes)
- **wrapper_template.py** - I/O handler with platform injection point (Python)
- **wrapper_template.cpp** - I/O handler with platform injection point (C++)

### Documentation
- **description_template.txt** - Problem description format with natural method integration

## Canonical Reference: 30_oct/ Directory

**Always use these 5 problems as templates when creating new problems:**

1. **problem_01_balanced_brackets** - String validation pattern
   - Single line input, boolean output converted to "true"/"false"
   - Stack-based algorithm
   - Use for: validation problems, string parsing

2. **problem_02_directory_tree_lister** - JSON/complex input pattern
   - JSON dictionary input, multi-line formatted output
   - Recursive tree traversal
   - Use for: hierarchical data, structured input, formatted output

3. **problem_03_matrix_spiral_traversal** - Matrix/2D array pattern
   - Dimensions + matrix rows input, space-separated output
   - Spiral traversal algorithm
   - Use for: 2D arrays, grid problems, spatial transformations

4. **problem_04_minimum_sum_of_products** - Array optimization pattern
   - Two space-separated arrays input, single integer output
   - Sorting and pairing strategy
   - Use for: array operations, sorting, optimization problems

5. **problem_05_multi_class_library_system** - Multi-command OOP pattern
   - Command sequence with EXIT terminator, multi-line results
   - State management, command parsing
   - Use for: simulation systems (library, vending machine, bank, etc.)

## Key Conventions (30_oct/ Standard)

### File Structure
- Every problem needs **exactly 10 files**: description, solution (py/cpp), template (py/cpp), wrapper (py/cpp), generator, config, examples
- Method names must match **exactly** across all files
- C++ files use `using namespace std;` at top, no `std::` prefixes
- Templates have neutral returns (NO `NotImplementedError` or `logic_error`)

### Orchestrator Integration
- **config.json**: Simple generation_logic array with 5 rule types
- **generator.py**: Command-line tool outputting INPUT only
- **solution.py/cpp**: Standalone programs with solve()/main() functions
- **examples.json**: stdin/expected_output/visibility format (4-5 examples)

### Pattern Selection Quick Guide
- Multiple commands with state? → Use problem_05
- JSON/hierarchical input? → Use problem_02
- 2D array/matrix? → Use problem_03
- String validation? → Use problem_01
- Array operations/sorting? → Use problem_04

## Usage

When creating a new problem:
1. Choose closest pattern from 30_oct/ problems above
2. Copy all 10 files from that problem as starting point
3. Update method names across all files (keep them synchronized!)
4. Modify logic in generator, solution, templates
5. Update description and examples to match
6. Run smoke test validation (see templates/smoke_test.md)
7. Generate test suites with orchestrator.py

## Documentation

- **PLATFORM_CONTEXT.md** - Complete architecture and patterns
- **QUICK_CHECKLIST.md** - Fast reference for file requirements
- **smoke_test.md** - 8-phase validation workflow
- **.github/copilot-instructions.md** - AI agent guidance with 30_oct/ references

All documentation has been updated to reference the 30_oct/ problems as canonical examples.

## For ANY Problem Type (Linked Lists, Trees, Graphs, etc.)

The 30_oct/ problems provide **architecture templates**, not algorithm-specific code. Here's what works for ANY problem type:

### What Transfers 100% (Architecture)
These elements are **identical** regardless of problem type:
1. **File Structure** - All 10 files (description, solution×2, template×2, wrapper×2, generator, config, examples)
2. **Wrapper Pattern** - Injection point, execute_solution(), exception handling
3. **Generator Pattern** - Command-line tool with argparse, rule_type, --rng-seed
4. **Config Format** - generation_logic array (always 5 rule types)
5. **Examples Format** - stdin/expected_output/visibility JSON
6. **Orchestrator Integration** - solve()/main() functions, stdin/stdout only
7. **Template Style** - Minimal Solution class with neutral returns

### What Changes (Algorithm & I/O Only)
Only these parts are problem-specific:
1. **Input Parsing** - How to read your data structure (array, tree, graph, etc.)
2. **Solution Logic** - Your algorithm implementation
3. **Method Signature** - Parameter types and return type
4. **Generator Logic** - How to create test cases for your data structure

### Quick Mapping for New Problem Types

| Problem Type | Base Pattern | What to Keep (100%) | What to Change (20%) |
|-------------|--------------|---------------------|---------------------|
| **Linked Lists** | problem_01/04 | Wrapper, Generator CLI, Config | Input parsing (array→list), Algorithm |
| **Binary Trees** | problem_02 | JSON parsing, Wrapper structure | Tree construction, Traversal logic |
| **Graphs** | problem_03 or 02 | Multi-line/JSON input, Wrapper | Graph representation, Search algorithms |
| **Dynamic Programming** | problem_04 | Array I/O, Wrapper, Config | DP recurrence, State definition |
| **String Algorithms** | problem_01 | String I/O, Wrapper | String algorithm (KMP, etc.) |
| **Heaps/Priority Queue** | problem_04 | Array input, Wrapper | Heap operations logic |
| **Tries** | problem_05 | Command pattern, Wrapper | Trie INSERT/SEARCH operations |
| **Backtracking** | problem_03 | Matrix input, Wrapper | Recursive exploration logic |

### Example: Linked List Problem from problem_01

If you need to create a "Reverse Linked List" problem:

1. **Copy** all 10 files from `problem_01_balanced_brackets/`
2. **Keep unchanged**:
   - config.json (100% identical)
   - wrapper.py structure (only change method name + parsing)
   - generator.py CLI interface (only change data generation)
   - examples.json format (only change test data)

3. **Change only**:
   - Method name: `areBracketsBalanced` → `reverseList`
   - Input parsing: `input().strip()` → `list(map(int, input().split()))`
   - Algorithm: stack validation → linked list reversal
   - Generator: bracket strings → integer arrays

**Result**: 80% of code copied, 20% modified for your specific algorithm!

### The Golden Rule

**Copy the STRUCTURE, Replace the LOGIC**

From any 30_oct/ problem you get:
- ✅ Perfect wrapper with injection point (works immediately)
- ✅ Working generator CLI (works immediately)
- ✅ Correct config.json (works immediately)
- ✅ Proper examples.json structure (works immediately)
- ✅ Orchestrator-compatible solution structure (works immediately)

You only change:
- 🔄 The algorithm in Solution class
- 🔄 Input/output parsing
- 🔄 Test data generation logic

**The platform architecture remains 100% the same!**
