# Competitive Programming Platform

This repository contains a problem-generation and testing framework integrated with Judge0 for Python and C++ solutions.

## Start here
- Platform context and patterns: `templates/PLATFORM_CONTEXT.md`
- Quick checklist (pattern rubric + OOP design): `templates/QUICK_CHECKLIST.md`
- Validation workflow: `templates/smoke_test.md`
- AI agent guide: `.github/copilot-instructions.md`

## Key components
- **30_oct/ canonical problems**: 5 production-ready examples for all problem patterns (string validation, JSON parsing, matrix operations, array optimization, multi-command OOP)
- **Problem folders**: `{difficulty}_{number}_{snake_case_title}/` with standardized files (`description.txt`, `solution.{py|cpp}`, `template.{py|cpp}`, `wrapper.{py|cpp}`, `generator.py`, `config.json`, `examples.json`)
- **Orchestrator**: `orchestrator.py` generates Judge0 test suites per problem and language (Python ID 71, C++ ID 54) targeting `http://localhost:3000`
- **Injection demo**: `platform_injection_working_demo.py` shows how wrappers inject contestant code at the `# ===== PLATFORM INJECTION POINT =====`
- **Tools**: `tools/normalize_cpp_namespace.py` for batch migration of legacy problems (use 30_oct/ templates for new problems)

## Canonical patterns (30_oct/ examples)
- **problem_01** (string validation): `isBalanced(s: str) -> bool` - Single string input, boolean output
- **problem_02** (JSON/complex input): `listTree(json_str: str) -> str` - Hierarchical data, formatted output
- **problem_03** (matrix/2D array): `spiralOrder(matrix: List[List[int]]) -> List[int]` - 2D array operations
- **problem_04** (array optimization): `minSumOfProducts(arr1, arr2: List[int]) -> int` - Multiple arrays, numeric result
- **problem_05** (multi-command OOP): `processCommands(commands: List[str]) -> List[str]` - Stateful simulation with EXIT terminator

## Tips
- Keep method names/signatures identical across description/templates/solutions/wrappers.
- Templates should be clean: no error throws; use neutral returns.
- C++ consistency: `using namespace std;` and avoid `std::` prefixes in templates/solutions to match wrappers.
- Judge0 uses stdin/stdout only; no file I/O.
