# Quick Checklist for New Problems

Use this stub when creating or reviewing problems. It complements `templates/PLATFORM_CONTEXT.md` and `.github/copilot-instructions.md`.

See also: `./smoke_test.md` for the validation workflow (run Phase 1 after scaffolding with this checklist).

## Pattern selection rubric (quick - 30_oct/ based)
- Does the task require processing multiple commands with state? → Use problem_05 (multi-command OOP)
- Does input need JSON/hierarchical parsing? → Use problem_02 (JSON pattern)
- Is it a 2D array/matrix problem? → Use problem_03 (matrix pattern)
- Is it string validation with boolean result? → Use problem_01 (validation pattern)
- Is it array optimization/sorting? → Use problem_04 (array optimization)
- Standard algorithmic task on simple data structures? → Use problem_01 or problem_04 (DSA pattern)

## Core File Checklist (30_oct/ Format)

### config.json
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

### examples.json
- Use `stdin`/`expected_output`/`visibility` format
- Include 4-5 examples matching description samples
- Ensure exact whitespace/newline matching

### generator.py
- Command-line tool: `python3 generator.py rule_type --args '{}' --rng-seed N`
- Outputs INPUT only (single test case)
- Handles all rule types from config.json

### solution.py
- Contains `Solution` class with method
- Contains `solve(infile, outfile)` function for orchestrator
- Standalone program: `python3 solution.py < input.txt`

### wrapper.py
- Contains injection point comment block
- Reads from stdin, calls Solution method, prints to stdout
- Exception handling with stderr

### template.py
- Clean Solution class with method signature
- Type hints in docstring (`:type param: type`, `:rtype: type`)
- Neutral return value (NO NotImplementedError)

### C++ files follow same pattern
- `using namespace std;` at top of solution.cpp and wrapper.cpp
- NO includes in template.cpp (wrapper provides them)
- Same method names as Python version

## Description Format (30_oct/ Style)
````plaintext
{Problem Title}

{Natural problem description - explain what needs to be done}

## Input Format
{Describe input - lines, types, separators}

## Output Format
{Describe output - format, newlines}

## Constraints
- {constraint_1}
- {constraint_2}

## Sample Input 1
```
{input}
```
## Sample Output 1
```
{output}
```

{Repeat for 3-4 more samples}
````

## Cross-File Validation Checklist
- [ ] Method name identical in description.txt, template.py/cpp, solution.py/cpp, wrapper.py/cpp
- [ ] Input format matches between description, generator output, and wrapper parsing
- [ ] Output format matches between description, solution output, and examples.json
- [ ] examples.json has 4-5 cases with exact whitespace matching
- [ ] config.json has all 5 rule types
- [ ] generator.py handles all rule types
- [ ] Templates have neutral returns (no NotImplementedError)
- [ ] C++ template has NO includes
- [ ] Both solutions are standalone programs
- [ ] Both wrappers have injection point comments
