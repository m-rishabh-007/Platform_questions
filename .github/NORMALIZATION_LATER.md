# Normalization Later

This repository uses a loose C++ style where wrappers include `using namespace std;`.
Some templates/solutions use explicit `std::` prefixes which is valid but inconsistent.

We deferred automatic normalization to avoid accidental regressions. When you are ready to
normalize templates/solutions (safe, one-shot operation) follow these steps:

1. Run a dry-run to see changes:

   ```bash
   python3 tools/normalize_cpp_namespace.py
   ```

   This prints unified diffs for files that would change. No files are modified.

2. If diffs look reasonable, run the apply step (creates `.bak` backups):

   ```bash
   python3 tools/normalize_cpp_namespace.py --apply
   ```

3. Immediately run the orchestrator smoke checks (requires Judge0 at http://localhost:3000):

   ```bash
   cd easy_33_sum_of_array_of_5_integers
   python3 ../orchestrator.py cpp -p .
   python3 ../orchestrator.py python -p .
   ```

4. Revert easily if something unexpected happens:

   ```bash
   git checkout -- **/*.cpp.bak
   ```

Notes:
- The script only touches `template.cpp` and `solution.cpp` files and skips `wrapper.cpp`.
- The script masks string literals and comments before removing `std::` to avoid breaking text.
- Still review diffs before applying and run the orchestrator to validate behavior.

If you want, I can apply the normalization now and run checks, but that requires Judge0 to be running locally.
