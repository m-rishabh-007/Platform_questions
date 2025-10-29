# Templates Directory - Complete Development Guide

> Start here
- Platform context and patterns: ../templates/PLATFORM_CONTEXT.md
- Quick checklist (pattern rubric + OOP design): ../templates/QUICK_CHECKLIST.md

The templates directory contains scaffolding files shared across every problem and complete platform context for AI agents and developers. Use this as your single source of truth for problem generation and platform understanding.

## 🚀 Quick Start for New Chats/Sessions

**Essential Workflow:**
1. **Read `./templates/PLATFORM_CONTEXT.md`** - Complete platform architecture and patterns
2. **Use `./templates/QUICK_START.md`** - Minimal prompt template for new AI sessions  
3. **Follow this README** - Detailed implementation guidelines
4. **Validate with `./templates/smoke_test.md`** - Ensure production quality

**Input:** Problem description (natural language) + This templates folder
**Output:** Complete problem folder (8 files) with perfect Judge0 compatibility

## 📁 Template Files Overview

### Core Templates
- **`config_template.json`** – Test generation logic buckets (edge/small/medium/large/extra-large)
- **`description_template.txt`** – Problem statement skeleton with natural method integration
- **`examples_template.json`** – Judge0-ready sample cases with `stdin`/`expected_output`
- **`generator_template.py`** – CLI test case generator consuming config arguments

### Solution Templates  
- **`solution_template.py`** / **`.cpp`** – Reference solutions with dependency-injectable I/O streams
- **`template_template.py`** / **`.cpp`** – Clean contestant starting points with Solution class pattern

### Documentation & Validation
- **`./templates/smoke_test.md`** – Comprehensive 8-phase validation methodology
- **`./templates/PLATFORM_CONTEXT.md`** – Complete platform architecture and Judge0 integration details
- **`./templates/QUICK_START.md`** – Streamlined onboarding for new AI agents

## 🛠️ Implementation Guidelines

### 1. Configuration First Approach
Start with `config.json` design:
- Define all rule buckets (edge_cases, small, medium, large, extra_large)
- Set appropriate `count` values for comprehensive test coverage
- Design argument payloads (ranges, predefined values, constraints)

### 2. Generator Development
Copy `generator_template.py` and customize:
- Implement `generate_case` logic respecting JSON arguments
- Handle all rule types from config.json
- Return exactly one test case per invocation
- Support optional `seed` for reproducible debugging

### 3. Solution Architecture  
**Python & C++ Solutions:**
- Use Solution class pattern consistently
- Implement dependency-injectable I/O (`solve(infile, outfile)`)
- Match parsing logic between solution and wrapper files
- Follow method signatures exactly as described

### 4. Template Consistency
**Critical Requirements:**
- **Python:** Clean method signatures with appropriate default returns (`[]`, `""`, `False`, `0.0`)
- **C++:** No `std::` prefixes (wrapper.cpp uses `using namespace std;`)
- **No error statements:** Remove `NotImplementedError`/`logic_error` - let contestants implement
- **Method signatures:** Must match exactly across solution/template/wrapper files

### 5. Description Quality
- **Natural method integration:** Methods mentioned in problem flow, not as explicit requirements
- **Clear I/O format:** Match generator output format exactly
- **Comprehensive examples:** Cover standard and edge cases
- **Explicit constraints:** Help contestants understand boundaries

### 6. Cross-File Harmony
**Essential Consistency Checks:**
- Method names and signatures identical across all files
- Input/output format matching between examples and solutions
- Config.json rules supported by generator
- C++ namespace consistency (no std:: in solution/template files)

## 🧪 Quality Assurance Process

### Mandatory Smoke Testing
1. **File Structure:** All 10 required files present
2. **JSON Validation:** config.json and examples.json syntactically valid
3. **Method Consistency:** Signatures match across Python/C++ files
4. **Solution Correctness:** Examples pass for both languages
5. **Config/Generator Alignment:** All rule types work with generator
6. **Compilation:** C++ files compile without errors
7. **Template Cleanliness:** No error statements, proper return values
8. **Cross-Platform Compatibility:** Judge0 ready outputs

### Critical Testing Methodology
**⚠️ MANDATORY: Fix-and-Retest Cycle**
1. Run complete smoke test
2. Fix ALL issues found
3. **Re-run COMPLETE smoke test** (never skip this!)
4. Repeat until ZERO errors
5. Only then declare production-ready

## 🎯 Success Criteria

**Production Ready Standards:**
- ✅ All 8 phases of smoke test pass
- ✅ 100% examples work for Python and C++ 
- ✅ Perfect method signature consistency
- ✅ Clean templates with no error statements
- ✅ Judge0 compatible I/O formatting
- ✅ Solution class pattern implemented correctly

## 🔄 Platform Integration

**The platform supports:**
- **Judge0 Integration:** All templates designed for automated testing
- **Database Export:** Structured output for platform database
- **Multi-Language Support:** Python and C++ with cross-platform consistency
- **Scalable Testing:** Orchestrator-driven comprehensive test suite generation
- **Quality Assurance:** Built-in validation preventing production issues

---

**For new AI agents:** Start with `./templates/PLATFORM_CONTEXT.md` → Use `./templates/QUICK_START.md` → Follow comprehensive guide in `./.github/README.md` → Validate with `./templates/smoke_test.md`
