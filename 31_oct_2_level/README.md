# 31_oct_2_level - Converted Format

This directory contains the same 5 problems from `31_oct_level_2`, but converted to match the format used in `30_oct_level_2` and `31_oct_level_3`.

## Structure

```
31_oct_2_level/
├── merge_overlapping_intervals/
│   ├── problem_description.json
│   ├── testcase.json
│   ├── templates/
│   │   ├── python.py
│   │   └── cpp.cpp
│   └── wrappers/
│       ├── wrapper.py
│       └── wrapper.cpp
├── number_of_islands/
│   └── (same structure)
├── product_of_array_except_self/
│   └── (same structure)
├── top_k_frequent_elements/
│   └── (same structure)
└── elevator_control_system/
    └── (same structure)
```

## Problems

| ID | Name | Difficulty | Category |
|----|------|------------|----------|
| 14 | Merge Overlapping Intervals | Easy | Sorting |
| 15 | Number of Islands | Medium | DSA/Graph |
| 16 | Product of Array Except Self | Medium | Logic/Arrays |
| 17 | Top K Frequent Elements | Medium | DSA/Heap |
| 18 | Elevator Control System | Hard | OOP/Design |

## File Descriptions

### problem_description.json
Contains metadata about the problem:
- `external_id`: Unique problem identifier
- `title`: Problem title
- `difficulty`: Easy/Medium/Hard
- `description`: Full problem description with input/output format
- `constraints`: Problem constraints
- `tags`: Problem categories
- `templates`: Paths to template files
- `wrappers`: Paths to wrapper files

### testcase.json
Combined test cases for both Python and C++:
- Separate metadata for each language
- Test cases with stdin/expected_output
- Visibility flags (visible/hidden)
- Input size information

### templates/
Contains starter code for contestants:
- `python.py`: Python Solution class template with TODO comment
- `cpp.cpp`: C++ Solution class declaration (header only)

### wrappers/
Contains I/O handling code:
- `wrapper.py`: Python wrapper with injection point
- `wrapper.cpp`: C++ wrapper with injection point

## Differences from 31_oct_level_2

### Original Format (31_oct_level_2)
- Folder names: `problem_14_merge_overlapping_intervals`
- Multiple files: `description.txt`, `config.json`, `examples.json`, `generator.py`, `solution.py`, `solution.cpp`
- Separate testcase files: `problem_14_merge_overlapping_intervals_python_testcases.json`, `*_cpp_testcases.json`
- Templates in root: `template.py`, `template.cpp`
- Wrappers in root: `wrapper.py`, `wrapper.cpp`

### New Format (31_oct_2_level)
- Folder names: `merge_overlapping_intervals` (clean, no prefix)
- Consolidated files:
  - `problem_description.json` (combines description.txt info)
  - `testcase.json` (combines both language testcases)
- Organized structure:
  - `templates/` subfolder
  - `wrappers/` subfolder
- Simpler template style with TODO comments

## Conversion Details

The conversion script (`convert_to_31_oct_2_level.py`):
1. Extracts description from `description.txt` format
2. Combines Python and C++ testcases into single `testcase.json`
3. Moves templates to `templates/` subfolder
4. Moves wrappers to `wrappers/` subfolder
5. Creates `problem_description.json` with metadata
6. Simplifies folder naming (removes `problem_XX_` prefix)

## Test Case Statistics

| Problem | Python Cases | C++ Cases | Visible | Hidden |
|---------|--------------|-----------|---------|--------|
| Merge Intervals | 34 | 34 | 4 | 30 |
| Number of Islands | 34 | 35 | 4 | 30+ |
| Product Except Self | 34 | 34 | 4 | 30 |
| Top K Frequent | 34 | 34 | 4 | 30 |
| Elevator System | 35 | 33 | 3 | 30+ |

## Usage

This format is designed for:
- Platform database import
- Cleaner problem organization
- Easier navigation
- Consistent structure across problem sets

All problems maintain the same:
- Injection point comments
- Method names and signatures
- I/O formats
- Test case validation

## Source

Converted from: `31_oct_level_2/`
Conversion date: 28 October 2025
Format matches: `30_oct_level_2/` and `31_oct_level_3/`
