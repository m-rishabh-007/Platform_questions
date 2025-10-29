# 31_oct_level_2 Problems

This directory contains 5 intermediate-level competitive programming problems generated from `problems.txt` and `problems_details.txt`, following the 30_oct/ canonical format.

## Problems Overview

| # | Name | Category | Difficulty | Key Concepts |
|---|------|----------|-----------|--------------|
| 14 | Merge Overlapping Intervals | Sorting | Easy | Sorting, Interval Merging |
| 15 | Number of Islands | DSA | Medium | DFS/BFS, Graph Traversal |
| 16 | Product of Array Except Self | Logic | Medium | Prefix/Suffix Products, No Division |
| 17 | Top K Frequent Elements | DSA | Medium | Hash Map, Min-Heap, Priority Queue |
| 18 | Elevator Control System | OOP | Hard | Object-Oriented Design, State Management |

## File Structure

Each problem contains 10 files following the 30_oct/ canonical format:

```
problem_XX_name/
├── description.txt          # Problem statement with samples
├── template.py             # Clean Python template (neutral returns)
├── template.cpp            # Clean C++ template (no includes)
├── solution.py             # Reference Python solution with solve()
├── solution.cpp            # Reference C++ solution with solve()
├── wrapper.py              # Python wrapper with injection point
├── wrapper.cpp             # C++ wrapper with injection point
├── generator.py            # Test case generator
├── config.json             # Generation rules (5 types)
├── examples.json           # 4 visible examples
```

## Pattern Mapping (from copilot-instructions.md)

- **Problem 14 (Merge Intervals)**: Uses problem_04 pattern (array optimization)
  - Sorting-based array problem
  - Two-line input: count + intervals
  - Multi-line output
  
- **Problem 15 (Number of Islands)**: Uses problem_03 pattern (matrix/2D)
  - 2D grid input
  - DFS/BFS traversal
  - Single numeric output
  
- **Problem 16 (Product Except Self)**: Uses problem_04 pattern (array optimization)
  - Single array input
  - Array output (space-separated)
  - Prefix/suffix technique
  
- **Problem 17 (Top K Frequent)**: Uses problem_04 pattern (array optimization)
  - Array + parameter input
  - Array output (any order)
  - Hash map + heap
  
- **Problem 18 (Elevator System)**: Uses problem_05 pattern (multi-command OOP)
  - Multi-command input with state
  - Multi-line formatted output
  - OOP design with dispatcher

## Testing

### Quick Test (Individual Problem)
```bash
cd problem_14_merge_overlapping_intervals

# Test generator
python3 generator.py edge_cases --rng-seed 42

# Test Python solution
echo -e "4\n1 3\n2 6\n8 10\n15 18" | python3 solution.py

# Test C++ solution
g++ -o solution solution.cpp
echo -e "4\n1 3\n2 6\n8 10\n15 18" | ./solution
```

### Generate Test Suites with Orchestrator
```bash
# From repo root, for each problem:
cd 31_oct_level_2/problem_14_merge_overlapping_intervals
python3 ../../orchestrator.py python -p .
python3 ../../orchestrator.py cpp -p .

# Expected output files:
# - problem_14_merge_overlapping_intervals_python_testcases.json
# - problem_14_merge_overlapping_intervals_cpp_testcases.json
```

### Smoke Test
Follow the 8-phase validation workflow from `templates/smoke_test.md`:
1. Phase 1: File presence & parsing
2. Phase 2: Generator execution
3. Phase 3: Solution execution
4. Phase 4: Wrapper execution
5. Phase 5: Examples validation
6. Phase 6: Cross-language consistency
7. Phase 7: Orchestrator integration
8. Phase 8: Final verification

## Key Conventions (from 30_oct/)

✅ **Method Names**: Identical across description, templates, solutions, wrappers
✅ **Templates**: Neutral returns (no NotImplementedError)
✅ **C++ Namespace**: `using namespace std;` in solutions/wrappers, NO `std::` prefixes
✅ **Injection Points**: Exact comment blocks in wrappers
✅ **Generators**: Output INPUT only (orchestrator gets output from Judge0)
✅ **config.json**: 5 rule types (edge_cases, small, medium, large, stress)
✅ **examples.json**: Uses stdin/expected_output/visibility format

## Problem-Specific Notes

### Problem 14: Merge Overlapping Intervals
- Method: `merge(intervals: List[List[int]]) -> List[List[int]]`
- Input: n + n lines of interval pairs
- Output: Merged intervals, one per line
- Key insight: Sort by start time first

### Problem 15: Number of Islands
- Method: `numIslands(grid: List[List[str]]) -> int`
- Input: m n + m lines of grid rows
- Output: Single integer count
- Key insight: DFS marks visited cells as '0'

### Problem 16: Product of Array Except Self
- Method: `productExceptSelf(nums: List[int]) -> List[int]`
- Input: n + array
- Output: Space-separated products
- Key insight: Two-pass prefix/suffix without division

### Problem 17: Top K Frequent Elements
- Method: `topKFrequent(nums: List[int], k: int) -> List[int]`
- Input: n k + array
- Output: k space-separated integers (any order)
- Key insight: Hash map + min-heap

### Problem 18: Elevator Control System
- Method: `simulateElevatorSystem(numFloors: int, numElevators: int, requests: List[str]) -> List[str]`
- Input: N M T + T request lines
- Output: T lines of "Step X: ..." messages
- Key insight: Simple nearest-elevator dispatching

## Validation Checklist

Before running orchestrator, verify:
- [ ] Method signatures match across all files (description/templates/solutions/wrappers)
- [ ] Templates have neutral returns (no exceptions)
- [ ] C++ files use consistent namespace (no std::)
- [ ] Wrappers have correct injection point comments
- [ ] examples.json matches actual solution output (exact whitespace)
- [ ] generator.py handles all 5 rule types from config.json
- [ ] Solutions are standalone (can run with stdin/stdout)

## Next Steps

1. **Review Generated Files**: Check method names, I/O formats, examples
2. **Run Smoke Tests**: Follow `templates/smoke_test.md` for each problem
3. **Generate Test Suites**: Use `orchestrator.py` to create Judge0 test cases
4. **Iterate**: Fix any issues found during validation
5. **Document**: Update this README with any special notes or patterns discovered

## References

- **Canonical Format**: See `30_oct/` directory for production-ready examples
- **Platform Context**: `templates/PLATFORM_CONTEXT.md`
- **Quick Checklist**: `templates/QUICK_CHECKLIST.md`
- **AI Guidelines**: `.github/copilot-instructions.md`
- **Smoke Test**: `templates/smoke_test.md`

## Generation Metadata

- **Generated**: 28 October 2025
- **Source**: `problems.txt` and `problems_details.txt`
- **Generator Script**: `create_31_oct_level_2_problems.py`
- **Format Version**: 30_oct canonical (10 files per problem)
- **Judge0 Endpoint**: http://localhost:3000
- **Language IDs**: Python 71, C++ 54
