# Problem Migration Script

This script automates the migration of Judge0 problems from **any source folder to any target folder**. Works with any folder structure regardless of naming conventions.

## Features

- ✅ **Flexible paths**: Migrate from any source to any target folder
- ✅ Migrates problem descriptions to `problem_description.json`
- ✅ Combines Python/C++ test suites into single `testcase.json`
- ✅ **Smart sampling: ALL visible cases included + random hidden cases**
- ✅ Copies templates to `templates/` subdirectory
- ✅ Copies wrappers to `wrappers/` subdirectory
- ✅ Supports single problem or batch migration
- ✅ Auto-extracts title and difficulty from description
- ✅ Reproducible sampling with configurable random seed

## Quick Start

### Single Problem Migration

**Basic syntax:**
```bash
python3 migration.py SOURCE_FOLDER TARGET_FOLDER --external-id ID [OPTIONS]
```

**Real-world examples:**

```bash
# Example 1: From development to production folder
python3 migration.py \
  dev_folder/problem_bubble_sort \
  prod_folder/bubble_sort \
  --external-id 7 \
  --sample 10

# Example 2: From one structure to another
python3 migration.py \
  source_folder/problem_balanced_brackets \
  target_folder/balanced_brackets \
  --external-id 100 \
  --sample 15

# Example 3: Between different organizational structures
python3 migration.py \
  problems_v1/sum_of_array \
  problems_v2/sum_of_array \
  --external-id 201 \
  --sample 20

# Example 4: With custom metadata
python3 migration.py \
  source/problem_xyz \
  destination/problem_xyz \
  --external-id 999 \
  --title "Custom Problem XYZ" \
  --difficulty Hard \
  --sample 12
```

### Batch Migration from Config

```bash
python3 migration.py --config migration_config.json
```

## Command-Line Options

| Option | Description | Required | Default |
|--------|-------------|----------|---------|
| `source` | Source problem directory (any folder) | Yes (single mode) | - |
| `target` | Target directory (any folder) | Yes (single mode) | - |
| `--external-id` | External ID for problem | Yes (single mode) | - |
| `--title` | Problem title | No | Extracted from description.txt |
| `--difficulty` | Easy/Medium/Hard | No | Inferred from folder name |
| `--sample` | Test cases per language | No | 10 |
| `--seed` | Random seed | No | 42 |
| `--config` | JSON config file for batch | No | - |

## Smart Test Case Sampling

The migration script uses **intelligent sampling** to ensure quality test coverage:

### How It Works
1. **All visible test cases** (`is_visible=true`) are **ALWAYS included**
2. Remaining slots filled with **random hidden test cases**
3. Random selection is reproducible (uses configurable seed)

### Example
If you have:
- 4 visible test cases
- 30 hidden test cases
- `--sample 10` setting

Result: **4 visible + 6 random hidden = 10 total test cases**

### Why This Matters
- **Visible cases** are typically the examples from `examples.json`
- These are what contestants see as sample inputs/outputs
- Ensures contestants always get the expected examples
- Provides additional hidden cases for thorough testing

## Configuration File Format

Create a JSON file with migration specifications:

```json
{
  "migrations": [
    {
      "source": "source_folder/problem_bubble_sort",
      "target": "target_folder/bubble_sort",
      "external_id": "7",
      "title": "Bubble Sort Comparison Counter",
      "difficulty": "Medium",
      "sample_size": 10,
      "random_seed": 42
    },
    {
      "source": "dev/problem_balanced_brackets",
      "target": "production/balanced_brackets",
      "external_id": "8",
      "sample_size": 15
    },
    {
      "source": "problems/sum_of_array",
      "target": "output/sum_of_array",
      "external_id": "9"
    }
  ]
}
```

### Config Fields

- **source** (required): Source directory path (any folder structure)
- **target** (required): Target directory path (any folder structure)
- **external_id** (required): Unique problem ID
- **title** (optional): Problem title (auto-extracted if omitted)
- **difficulty** (optional): Easy/Medium/Hard (auto-inferred if omitted)
- **sample_size** (optional): Test cases per language (default: 10). **Note:** ALL visible cases are always included first, then random hidden cases fill remaining slots.
- **random_seed** (optional): For reproducible sampling (default: 42)

## Source Directory Requirements

The source directory must contain:

- ✅ `description.txt` - Problem description
- ✅ `template.py` - Python template
- ✅ `template.cpp` - C++ template
- ✅ `wrapper.py` - Python wrapper
- ✅ `wrapper.cpp` - C++ wrapper
- ✅ `*_python_testcases.json` - Python test suite (from orchestrator)
- ✅ `*_cpp_testcases.json` - C++ test suite (from orchestrator)

## Output Structure

The target directory will contain:

```
target_folder/
├── problem_description.json    # Metadata and description
├── testcase.json               # Combined Python/C++ test cases (smart sampled)
├── templates/
│   ├── python.py
│   └── cpp.cpp
└── wrappers/
    ├── wrapper.py
    └── wrapper.cpp
```

## Examples with Output

### Example: Migrate with custom sampling
```bash
python3 migration.py \
  source_folder/problem_emirp_numbers \
  output_folder/emirp \
  --external-id TEST-1 \
  --sample 5
```

**Output:**
```
======================================================================
Migrating: problem_emirp_numbers → emirp
======================================================================
  📄 Creating problem_description.json...
     ✅ Created with external_id=TEST-1, title='The Enigma of Mirrored Primes (Emirp)'
  🧪 Creating testcase.json...
     Original: 34 Python, 34 C++ test cases
     Sampled: 5 Python, 5 C++ test cases
     ✅ Created testcase.json (3.8KB)
  📝 Copying templates...
     ✅ Copied template.py → templates/python.py
     ✅ Copied template.cpp → templates/cpp.cpp
  🔄 Copying wrappers...
     ✅ Copied wrapper.py → wrappers/wrapper.py
     ✅ Copied wrapper.cpp → wrappers/wrapper.cpp
✅ Migration complete for emirp!
```

## Troubleshooting

### Error: "description.txt not found"
- Ensure source directory contains `description.txt`
- Check the source path is correct

### Error: "Testcase files not found"
- Run orchestrator first to generate test suites:
  ```bash
  python3 orchestrator.py python -p SOURCE_DIR
  python3 orchestrator.py cpp -p SOURCE_DIR
  ```
- Ensure files match pattern: `*_python_testcases.json` and `*_cpp_testcases.json`

### Error: "external-id is required"
- Add `--external-id N` flag for single migrations
- Or use config file with `external_id` field

## Integration with Workflow

Typical workflow:

```bash
# 1. Create problem in development folder
cd source_folder/problem_new_problem

# 2. Run orchestrator to generate test suites
cd ../..
python3 orchestrator.py python -p source_folder/problem_new_problem
python3 orchestrator.py cpp -p source_folder/problem_new_problem

# 3. Migrate to desired output folder
python3 migration.py \
  source_folder/problem_new_problem \
  target_folder/new_problem \
  --external-id 11 \
  --difficulty Medium
```

## See Also

- `migration_config_example.json` - Example configuration file
- `.github/copilot-instructions.md` - Platform conventions
- `templates/PLATFORM_CONTEXT.md` - File structure details
- `TEST_CASE_SAMPLING_FIX.md` - Details on smart sampling implementation
