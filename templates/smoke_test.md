# Smoke Test Guide for Competitive Programming Problems

## Overview
This comprehensive smoke test validates all problem components before Judge0 testing. It ensures cross-file consistency, method signature alignment, and complete ecosystem integrity.

**All validations are based on the 30_oct/ canonical format** - the production-ready, orchestrator-validated standard used by problems 01-05.

## Prerequisites
- All 10 required files must exist in the problem directory
- Judge0 server should be accessible (for final validation)
- Python 3.x and g++ compiler installed
- Files should follow 30_oct/ format (see templates/README_TEMPLATES.md)

## Required Files Checklist
```
✅ config.json          - Test generation configuration
✅ description.txt       - Minimal competition-style problem statement
✅ examples.json         - Sample test cases in Judge0 format  
✅ generator.py          - Test case generator with CLI support
✅ solution.py           - Reference Python solution with Solution class
✅ solution.cpp          - Reference C++ solution with Solution class
✅ template.py           - Clean Python contestant starter
✅ template.cpp          - Clean C++ contestant starter (minimal includes)
✅ wrapper.py            - Python I/O wrapper with injection points
✅ wrapper.cpp           - C++ I/O wrapper with injection points
```

## Phase 1: File Existence & Structure

Tip (for new problems): Before running Phase 1, use `./QUICK_CHECKLIST.md` to quickly choose the base pattern from 30_oct/ (problem_01 through problem_05) and confirm the design checklist, then copy files from the closest matching problem.
```bash
# Verify all files exist
for file in config.json description.txt examples.json generator.py solution.py solution.cpp template.py template.cpp wrapper.py wrapper.cpp; do
    if [ -f "$file" ]; then 
        echo "✅ $file exists"
    else 
        echo "❌ $file missing"
    fi
done
```

## Phase 2: JSON Validation
```bash
# Test JSON files are valid
python -c "import json; json.load(open('config.json')); print('✅ config.json valid')"
python -c "import json; json.load(open('examples.json')); print('✅ examples.json valid')"
```

## Phase 3: Method Signature Consistency
**Critical Check**: All files must have matching method signatures.

### Python Method Validation:
```python
import re

py_files = ['solution.py', 'template.py', 'wrapper.py']
method_name = 'YOUR_METHOD_NAME'  # Replace with actual method

for file in py_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if method_name in content:
        pattern = rf'def {method_name}\([^)]*\)'
        matches = re.findall(pattern, content)
        if matches:
            print(f'✅ {file}: {matches[0]}')
        else:
            print(f'⚠️  {file}: Method name found but no clear definition')
    else:
        print(f'❌ {file}: Method {method_name} not found')
```

### C++ Method Validation:
```python
import re

cpp_files = ['solution.cpp', 'template.cpp', 'wrapper.cpp']
method_name = 'YOUR_METHOD_NAME'  # Replace with actual method

for file in cpp_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if method_name in content:
        pattern = rf'[a-zA-Z0-9_:<>&*\s]+{method_name}\s*\([^)]*\)'
        matches = re.findall(pattern, content)
        if matches:
            print(f'✅ {file}: {matches[0].strip()}')
        else:
            print(f'⚠️  {file}: Method name found but no clear definition')
    else:
        print(f'❌ {file}: Method {method_name} not found')
```

### C++ Template Include Validation:
```python
template_cpp_files = ['template.cpp']

for file in template_cpp_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Check for minimal includes only
    includes = [line.strip() for line in content.split('\n') if line.strip().startswith('#include')]
    
    if len(includes) <= 3:  # Should only have essential includes like iostream, vector
        print(f'✅ {file}: Minimal includes ({len(includes)} total)')
    else:
        print(f'⚠️  {file}: Too many includes ({len(includes)} total) - should only have essential ones')
        print(f'   Includes: {includes}')
    
    # Check for using namespace std
    if 'using namespace std;' in content:
        print(f'✅ {file}: Has "using namespace std;"')
    else:
        print(f'❌ {file}: Missing "using namespace std;" - needed for consistency with wrapper.cpp')
```

### C++ Namespace Consistency Check:
```python
cpp_files = ['solution.cpp', 'template.cpp']

for file in cpp_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if 'std::' in content and 'using namespace std;' in content:
        print(f'⚠️  {file}: Contains both "using namespace std;" and std:: prefixes - should remove std::')
    elif 'std::' in content:
        print(f'⚠️  {file}: Uses std:: prefixes without "using namespace std;" - inconsistent with wrapper.cpp')
    else:
        print(f'✅ {file}: Proper namespace usage')
```

## Phase 4: Solution Testing
```bash
# Test Python solution
echo "Testing Python solution..."
python solution.py < test_input.txt

# Test C++ solution  
echo "Testing C++ solution..."
g++ -o cpp_test solution.cpp && ./cpp_test < test_input.txt
```

## Phase 5: Template File Validation
```python
# Validate Python template
with open('template.py', 'r') as f:
    py_content = f.read()

py_checks = [
    ('class Solution', 'class Solution:' in py_content),
    ('method signature', 'def ' in py_content),
    ('proper return', 'return' in py_content and 'NotImplementedError' not in py_content),
    ('no errors', 'raise NotImplementedError' not in py_content),
    ('docstring', '"""' in py_content or "'''" in py_content),
    ('clean template', py_content.count('TODO') > 0 or py_content.count('implement') > 0)
]

for check_name, passed in py_checks:
    status = '✅' if passed else '❌'
    print(f'{status} Python template {check_name}')

# Enhanced C++ template validation
with open('template.cpp', 'r') as f:
    cpp_content = f.read()

cpp_checks = [
    ('class Solution', 'class Solution' in cpp_content),
    ('public methods', 'public:' in cpp_content),
    ('no std prefixes', 'std::' not in cpp_content),
    ('using namespace', 'using namespace std;' in cpp_content),
    ('proper return', 'return' in cpp_content and 'logic_error' not in cpp_content),
    ('no errors', 'throw logic_error' not in cpp_content),
    ('minimal includes', cpp_content.count('#include') <= 3),
    ('competition ready', all(inc in cpp_content for inc in ['#include <iostream>', '#include <vector>']))
]

for check_name, passed in cpp_checks:
    status = '✅' if passed else '❌'
    print(f'{status} C++ template {check_name}')

# Additional include analysis
include_lines = [line.strip() for line in cpp_content.split('\n') if line.strip().startswith('#include')]
print(f'📊 C++ includes found: {len(include_lines)}')
for inc in include_lines:
    print(f'   {inc}')
```

## Phase 6: Examples Validation
**Critical**: examples.json must match solution outputs exactly.

```python
import json
import subprocess

with open('examples.json', 'r') as f:
    examples = json.load(f)

print('Testing examples against Python solution:')
for i, example in enumerate(examples, 1):
    result = subprocess.run(['python', 'solution.py'], 
                          input=example['stdin'], 
                          text=True, 
                          capture_output=True)
    
    expected = example['expected_output'].strip()
    actual = result.stdout.strip()
    
    status = '✅' if actual == expected else '❌'
    print(f'{status} Example {i}: Expected="{expected}" Got="{actual}"')
```

## Phase 7: Config/Generator Alignment
**Critical**: Generator must support all config.json rule types.

```python
import json
import subprocess

with open('config.json', 'r') as f:
    config = json.load(f)

rule_types = [bucket['type'] for bucket in config['generation_logic']]
print('Config rule types:', rule_types)

for rule_type in rule_types:
    bucket = next(b for b in config['generation_logic'] if b['type'] == rule_type)
    args = json.dumps(bucket['args'])
    
    try:
        result = subprocess.run(['python', 'generator.py', rule_type, '--args', args], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            print(f'✅ Generator works with {rule_type}')
        else:
            print(f'❌ Generator failed with {rule_type}: {result.stderr.strip()}')
    except Exception as e:
        print(f'❌ Generator error with {rule_type}: {e}')
```

## Phase 8: Wrapper Injection Testing
**Critical**: Platform injection must work correctly.

```python
# Test Python wrapper injection
with open('wrapper.py', 'r') as f:
    wrapper = f.read()
with open('template.py', 'r') as f:  # Use template as example contestant code
    solution = f.read()

placeholder = '# ===== PLATFORM INJECTION POINT ====='
# Find the full placeholder block and replace it
# Create injected test file and verify it works

# Similar process for C++ wrapper
```

## Phase 9: Description Quality Check (Updated Standards)
```python
with open('description.txt', 'r') as f:
    content = f.read()

# Updated checks for minimal competition format
checks = [
    ('problem title', content.startswith('#') and len(content.split('\n')[0].strip()) > 10),
    ('problem statement section', '## Problem Statement' in content),
    ('input format section', '## Input Format' in content),
    ('output format section', '## Output Format' in content),
    ('constraints section', '## Constraints' in content),
    ('no sample examples', 'Sample Input' not in content and 'Sample Output' not in content),
    ('no verbose explanations', len(content.split('\n')) < 25),  # Should be concise
    ('no implementation details', 'Algorithm' not in content and 'Implementation' not in content),
    ('method name mentioned', any(method in content for method in ['function', 'method', '_'])),
    ('competition style', 'Write a function' in content or 'implement' in content.lower())
]

for check_name, passed in checks:
    status = '✅' if passed else '❌'
    print(f'{status} Description {check_name}')

# Check line count for conciseness
line_count = len([line for line in content.split('\n') if line.strip()])
if line_count <= 20:
    print(f'✅ Description is concise ({line_count} lines)')
else:
    print(f'⚠️  Description may be too verbose ({line_count} lines) - consider simplifying')
```

## Success Criteria
All phases must pass with ✅ status:

- **File Existence**: All 10 files present
- **JSON Validity**: No syntax errors in JSON files  
- **Method Consistency**: Same method signatures across all files
- **Solution Correctness**: Both Python/C++ produce expected outputs
- **Examples Alignment**: All examples pass solution tests
- **Config/Generator**: All rule types work with generator
- **Wrapper Injection**: Platform injection works for both languages
- **Description Quality**: Clear problem specification with explicit methods

## Critical Testing Methodology

**⚠️ IMPORTANT: Iterative Fix-and-Retest Cycle**

1. **Run complete smoke test** - Execute all 8 phases
2. **If ANY issues found** - Fix them immediately
3. **Re-run COMPLETE smoke test** - Don't assume fixes work
4. **Repeat until ZERO errors** - Every phase must show ✅ status
5. **Only then declare problem ready** for Judge0 testing

**Never skip the re-verification step!** Fixes can introduce new issues or reveal hidden dependencies. A problem is only production-ready when it passes a complete smoke test with zero errors after all modifications.

## Troubleshooting Common Issues

### Method Signature Mismatch
**Problem**: Different method names/signatures across files
**Solution**: Update all files to use consistent method signature

### C++ Namespace Inconsistency
**Problem**: template.cpp or solution.cpp uses std:: prefixes when wrapper.cpp has "using namespace std;"
**Solution**: Remove all std:: prefixes from template.cpp and solution.cpp files for consistency

### Examples Don't Match Solutions  
**Problem**: examples.json outputs don't match solution outputs
**Solution**: Either fix solution logic or update examples.json

### Generator Fails with Config Rules
**Problem**: Generator doesn't support rule types from config.json
**Solution**: Update generator.py to handle all configured rule types

### Wrapper Injection Fails
**Problem**: Injected code doesn't execute properly
**Solution**: Check injection placeholder format and Solution class instantiation

### Description Missing Method Names
**Problem**: Contestants unclear what methods to implement
**Solution**: Add explicit "Required Methods" section with signatures

## Final Validation
After all phases pass, the problem is ready for:
1. Judge0 comprehensive testing (`python orchestrator.py`)
2. Production deployment
3. Database export

**Final Validation Checklist:**
- [ ] Complete smoke test passes with 0 errors
- [ ] All fixes verified with full re-test
- [ ] No regressions introduced during fix process
- [ ] All examples work for both Python and C++
- [ ] Cross-file consistency maintained throughout

## Notes for GitHub Copilot
- Always run this complete smoke test before Judge0 testing
- **CRITICAL:** Fix issues incrementally and RE-TEST after each fix
- **NEVER skip re-verification** after making modifications
- Continue fix → re-test cycle until achieving ZERO errors
- Update templates folder with any improvements discovered
- Method signature consistency is critical - check this first
- Examples must exactly match solution outputs (including whitespace)
- Don't skip any phases - all must pass for quality assurance
- **Production readiness requires perfect smoke test results**