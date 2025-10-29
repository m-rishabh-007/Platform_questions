# AI Agent Guide: Competitive Programming Platform (Concise)

## Read First
- `templates/PLATFORM_CONTEXT.md` – authoritative specs and patterns
- `templates/smoke_test.md` – 8-phase validation workflow
- `.github/README.md` – templates overview and onboarding
- Quick decision: see the [Pattern selection rubric](../templates/QUICK_CHECKLIST.md)

## Canonical Reference: 30_oct/ Directory
**ALWAYS use these 5 production-ready, orchestrator-validated problems as templates:**
- `30_oct/problem_01_balanced_brackets` - String validation (single line in/out)
- `30_oct/problem_02_directory_tree_lister` - JSON parsing (complex input/multi-line output)
- `30_oct/problem_03_matrix_spiral_traversal` - 2D array (multi-line input)
- `30_oct/problem_04_minimum_sum_of_products` - Array optimization (two arrays in)
- `30_oct/problem_05_multi_class_library_system` - OOP simulation (EXIT terminator, multi-command)

These problems contain **validated file structures, correct I/O patterns, and working orchestrator integration**.

## Architecture at a Glance
- Each problem folder contains 8 core files: `description.txt`, `solution.py`, `solution.cpp`, `template.py`, `template.cpp`, `wrapper.py`, `wrapper.cpp`, `generator.py` plus `config.json` and `examples.json` used by tooling.
- Solutions follow a single Solution class method invoked by wrappers; wrappers handle stdin/stdout and inject contestant code at `# ===== PLATFORM INJECTION POINT =====`.
- Test suites are generated via `orchestrator.py` using Judge0 at `http://localhost:3000` (Python ID 71, C++ ID 54) and saved as `{problem_name}_{language}_testcases.json`.

## Canonical Patterns (with 30_oct/ examples)
- **Numeric list pattern** (problem_01, problem_04): Single or multiple arrays/lists, numeric operations
  - Python `class Solution: def methodName(self, arr: List[int]) -> int`
  - C++ `class Solution { int methodName(const vector<int>& arr); }`
  
- **String/validation pattern** (problem_01): Single string input, boolean or string output
  - See `30_oct/problem_01_balanced_brackets/{template.py, wrapper.py, template.cpp, wrapper.cpp}`
  
- **JSON/complex input pattern** (problem_02): JSON or structured input, formatted output
  - See `30_oct/problem_02_directory_tree_lister/{template.py, wrapper.py, template.cpp, wrapper.cpp}`
  
- **Matrix pattern** (problem_03): 2D array input, array/list output
  - See `30_oct/problem_03_matrix_spiral_traversal/{template.py, wrapper.py, template.cpp, wrapper.cpp}`
  
- **Multi-command OOP pattern** (problem_05): Command sequence with terminator, stateful processing
  - See `30_oct/problem_05_multi_class_library_system/{template.py, wrapper.py, template.cpp, wrapper.cpp}`
  - Use for: library systems, vending machines, bank transactions, any stateful simulation
  - Key: EXIT terminator, command parsing, multi-line output

## Pattern selection guide (what to use when)
- **Use problem_05 (multi-command OOP)** when the task:
  - Models a system with commands (library, vending machine, bank, etc.)
  - Requires state management across multiple operations
  - Has command terminator (EXIT, QUIT, etc.)
  - Returns multiple result lines
  
- **Use problem_02 (JSON/complex input)** when the task:
  - Requires parsing structured/hierarchical data
  - Needs recursive traversal
  - Has complex formatted output
  
- **Use problem_03 (matrix/2D)** when the task:
  - Works with 2D arrays/grids
  - Requires multi-line matrix input
  - Performs spatial transformations
  
- **Use problem_01/04 (standard DSA)** for:
  - Array/list operations
  - String transformations
  - Math calculations
  - Sorting/searching algorithms
  - Prefix sums, sliding windows, stacks, queues

## Pattern selection rubric (quick - 30_oct/ based)
- Does the task require processing multiple commands with state? → Use problem_05 (multi-command OOP)
- Does input need JSON/hierarchical parsing? → Use problem_02 (JSON pattern)
- Is it a 2D array/matrix problem? → Use problem_03 (matrix pattern)
- Is it string validation with boolean result? → Use problem_01 (validation pattern)
- Is it array optimization/sorting? → Use problem_04 (array optimization)
- Standard algorithmic task on simple data structures? → Use problem_01 or problem_04 (DSA pattern)

See also: the full platform patterns in `templates/PLATFORM_CONTEXT.md`.

## Project Conventions (30_oct/ Standard)
- **10 files per problem**: description.txt, solution.py/cpp, template.py/cpp, wrapper.py/cpp, config.json, examples.json, generator.py
- **Method names** must match exactly across all files (description, templates, solutions, wrappers)
- **Templates** must be clean with neutral returns (`[]`, `""`, `0`, `False`), NO `NotImplementedError` or `logic_error`
- **C++ files** use `using namespace std;` at top, no `std::` prefixes
- **Wrappers** handle all I/O; Solution class contains only logic
- **Generators** output INPUT only (orchestrator gets output from Judge0)
- **config.json** uses simple `generation_logic` array format
- **examples.json** uses `stdin`/`expected_output`/`visibility` format
- **Judge0** execution is stdin/stdout only (no file I/O, no external dependencies)

## Developer Workflows
1) Create a new problem
   - Start from templates in `templates/` and follow `PLATFORM_CONTEXT.md`.
   - Extract a natural method name from the description; propagate the exact signature to both languages and wrappers.
   - Write `examples.json` that matches solution output exactly (whitespace matters).
   - Implement `generator.py` to support all rule types declared in `config.json`.
   - Run the full smoke test from `templates/smoke_test.md` and iterate until zero issues.

2) Generate Judge0 test suites
   - Use `orchestrator.py` from the problem directory to produce `{problem_name}_{language}_testcases.json` for Python and C++; ensure Judge0 is reachable at `localhost:3000`.
   - Orchestrator auto-measures baseline time/memory and annotates each case with `admin_time`, `admin_memory`, and size.

## Gotchas
- Keep method names synchronized everywhere; mismatches cause wrapper failures.
- Ensure `examples.json` aligns with actual solution output; regenerate if logic changes.
- Maintain C++ namespace consistency (no `std::`) to match wrappers.
- Don’t add or change I/O semantics in templates/solutions; wrappers define the contract.

## Quick Checklist
- Method signature identical across description/templates/solutions/wrappers (both languages)
- Templates clean (no error throws), correct neutral returns
- `config.json` rule types are implemented by `generator.py`
- Smoke test (all phases) passes; then run `orchestrator.py` for final suites

Questions or gaps? Tell us where the guidance felt thin (e.g., generator rule examples, wrapper parsing patterns), and we’ll refine this file.

## Try it (optional)
- Judge0 precheck:
   - Linux/macOS: `curl -s http://localhost:3000 | head -c 120`
- Generate suites for a problem (from repo root):
   - `cd easy_33_sum_of_array_of_5_integers`
   - Python: `python3 ../orchestrator.py python -p .`
   - C++: `python3 ../orchestrator.py cpp -p .`
   - Expect files: `easy_33_sum_of_array_of_5_integers_python_testcases.json` and `_cpp_testcases.json`
- If anything fails, map symptoms to `templates/smoke_test.md` phases (e.g., parsing/signature mismatches) and iterate until all phases pass.

### Try it (optional: multiclass OOP via easy_34)
- From repo root:
   - `cd easy_34_student_class_display_details`
   - Python: `python3 ../orchestrator.py python -p .`
   - C++: `python3 ../orchestrator.py cpp -p .`
   - Expect: `easy_34_student_class_display_details_{python|cpp}_testcases.json`
- I/O shape enforced by wrappers:
   - Input: a single line with `name roll marks` (e.g., `Alice 42 88.5`)
   - Output: the exact string returned by `Solution.getStudentDetails(name, roll, marks)`

## Designing multiclass OOP problems (easy_34 checklist)
- Entities/fields: list fields up front and choose a method name like `getXDetails`/`generateReceipt` matching the summary to print.
- Signature: use primitive args (str/int/float) in a fixed order; avoid passing objects. Mirror exactly in Python/C++ templates and wrappers.
- Input parsing: prefer one line, deterministic token order (e.g., `name roll marks`). If names may contain spaces, explicitly define quoting; otherwise, restrict names to no spaces.
- Output format: define exact formatting (no extra spaces/newlines). Ensure `examples.json` matches precisely; update if formatting changes.
- Stateless solution: keep I/O in wrappers only; `Solution` method builds and returns the final string.
- Cross-file sync: keep method names/signatures identical in `description.txt`, templates, solutions, and wrappers; regenerate suites after changes.

## Tools Directory (Legacy Migration Only)
The `tools/` folder contains utilities for maintaining existing code, NOT for new problem creation:
- **tools/normalize_cpp_namespace.py**: Batch migration tool for legacy problems (easy_21-35) to match 30_oct/ namespace standards
  - Adds `using namespace std;` after includes
  - Removes `std::` prefixes from code
  - Creates .bak backups before changes
  - **DO NOT use for new problems** - always start from 30_oct/ templates instead
- For details: See `tools/README.md`
- When to mention: Only if user asks about migrating old problems or namespace issues in legacy code