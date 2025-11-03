#!/usr/bin/env python3
"""
Generalized Migration Script for Judge0 Problems
Migrates problems from any source folder to any target folder.

Usage:
    python3 migration.py SOURCE_FOLDER TARGET_FOLDER [OPTIONS]

Examples:
    # Migrate single problem to any folder
    python3 migration.py source_folder/problem_name target_folder/problem_name --external-id 7

    # Migrate to production folder
    python3 migration.py dev_folder/problem_name production/problem_name --external-id 8 --sample 10

    # Migrate multiple problems from config file
    python3 migration.py --config migration_config.json

    # Migrate with custom sampling
    python3 migration.py source_folder/problem target_folder/problem --external-id 15 --sample 20

Config file format (migration_config.json):
    {
        "migrations": [
            {
                "source": "source_folder/problem_name",
                "target": "target_folder/problem_name",
                "external_id": "7",
                "title": "Problem Title",
                "difficulty": "Medium",
                "sample_size": 10
            }
        ]
    }
"""

import json
import random
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Optional


class ProblemMigrator:
    """Handles migration of a single problem from source to target folder."""
    
    def __init__(self, source_dir: Path, target_dir: Path, 
                 external_id: str, title: Optional[str] = None,
                 difficulty: Optional[str] = None, sample_size: int = 10,
                 random_seed: int = 42):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.external_id = external_id
        self.title = title
        self.difficulty = difficulty
        self.sample_size = sample_size
        self.random_seed = random_seed
        
        # Set random seed for reproducible sampling
        random.seed(random_seed)
        
    def extract_metadata_from_description(self) -> Dict:
        """Extract title and difficulty from description.txt if not provided."""
        desc_file = self.source_dir / "description.txt"
        if not desc_file.exists():
            raise FileNotFoundError(f"description.txt not found in {self.source_dir}")
        
        with open(desc_file, 'r') as f:
            content = f.read()
        
        # Extract title (first non-empty line)
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        title = lines[0] if lines else "Untitled Problem"
        
        # Try to infer difficulty from folder name or default to Medium
        folder_name = self.source_dir.name.lower()
        if 'easy' in folder_name:
            difficulty = "Easy"
        elif 'hard' in folder_name:
            difficulty = "Hard"
        else:
            difficulty = "Medium"
        
        return {
            "title": self.title or title,
            "difficulty": self.difficulty or difficulty,
            "description": content
        }
    
    def create_problem_description_json(self) -> None:
        """Create problem_description.json in target directory."""
        print(f"  📄 Creating problem_description.json...")
        
        metadata = self.extract_metadata_from_description()
        
        problem_desc = {
            "external_id": self.external_id,
            "title": metadata["title"],
            "difficulty": metadata["difficulty"],
            "description": metadata["description"],
            "constraints": "",
            "tags": ["Problem Solving", "Algorithm"],
            "templates": {
                "python_path": "templates/python.py",
                "cpp_path": "templates/cpp.cpp"
            },
            "wrappers": {
                "python_path": "wrappers/wrapper.py",
                "cpp_path": "wrappers/wrapper.cpp"
            }
        }
        
        output_file = self.target_dir / "problem_description.json"
        with open(output_file, 'w') as f:
            json.dump(problem_desc, f, indent=2)
        
        print(f"     ✅ Created with external_id={self.external_id}, title='{metadata['title']}'")
    
    def find_testcase_files(self) -> Dict[str, Path]:
        """Find Python and C++ testcase JSON files."""
        # Look for files matching pattern: *_python_testcases.json and *_cpp_testcases.json
        python_files = list(self.source_dir.glob("*_python_testcases.json"))
        cpp_files = list(self.source_dir.glob("*_cpp_testcases.json"))
        
        if not python_files or not cpp_files:
            raise FileNotFoundError(
                f"Testcase files not found in {self.source_dir}. "
                f"Expected: *_python_testcases.json and *_cpp_testcases.json"
            )
        
        return {
            "python": python_files[0],
            "cpp": cpp_files[0]
        }
    
    def sample_test_cases(self, test_cases: List[Dict]) -> List[Dict]:
        """
        Sample N test cases ensuring ALL visible cases are included.
        Visible cases (is_visible=true) are always included.
        Remaining slots filled with random hidden cases.
        """
        # Separate visible and hidden test cases
        visible = [tc for tc in test_cases if tc.get('is_visible') == True]
        hidden = [tc for tc in test_cases if tc.get('is_visible') != True]
        
        # Start with all visible cases
        selected = visible.copy()
        
        # Fill remaining slots with random hidden cases
        remaining_slots = self.sample_size - len(visible)
        if remaining_slots > 0 and hidden:
            random_hidden = random.sample(hidden, min(remaining_slots, len(hidden)))
            selected.extend(random_hidden)
        
        return selected
    
    def create_combined_testcase_json(self) -> None:
        """Create combined testcase.json with sampled test cases."""
        print(f"  🧪 Creating testcase.json...")
        
        testcase_files = self.find_testcase_files()
        
        # Read Python test suite
        with open(testcase_files["python"]) as f:
            python_suite = json.load(f)
        
        # Read C++ test suite
        with open(testcase_files["cpp"]) as f:
            cpp_suite = json.load(f)
        
        original_python_count = len(python_suite['test_cases'])
        original_cpp_count = len(cpp_suite['test_cases'])
        
        # Sample test cases
        sampled_python = self.sample_test_cases(python_suite['test_cases'])
        sampled_cpp = self.sample_test_cases(cpp_suite['test_cases'])
        
        print(f"     Original: {original_python_count} Python, {original_cpp_count} C++ test cases")
        print(f"     Sampled: {len(sampled_python)} Python, {len(sampled_cpp)} C++ test cases")
        
        # Create combined structure
        combined = {
            "python": {
                "metadata": python_suite['metadata'],
                "test_cases": sampled_python
            },
            "cpp": {
                "metadata": cpp_suite['metadata'],
                "test_cases": sampled_cpp
            }
        }
        
        # Write to target
        output_file = self.target_dir / "testcase.json"
        with open(output_file, 'w') as f:
            json.dump(combined, f, indent=2)
        
        size_kb = output_file.stat().st_size / 1024
        print(f"     ✅ Created testcase.json ({size_kb:.1f}KB)")
    
    def copy_templates(self) -> None:
        """Copy template files to templates/ subdirectory."""
        print(f"  📝 Copying templates...")
        
        templates_dir = self.target_dir / "templates"
        templates_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy Python template
        python_src = self.source_dir / "template.py"
        python_dst = templates_dir / "python.py"
        if python_src.exists():
            shutil.copy2(python_src, python_dst)
            print(f"     ✅ Copied template.py → templates/python.py")
        else:
            print(f"     ⚠️  Warning: template.py not found")
        
        # Copy C++ template
        cpp_src = self.source_dir / "template.cpp"
        cpp_dst = templates_dir / "cpp.cpp"
        if cpp_src.exists():
            shutil.copy2(cpp_src, cpp_dst)
            print(f"     ✅ Copied template.cpp → templates/cpp.cpp")
        else:
            print(f"     ⚠️  Warning: template.cpp not found")
    
    def copy_wrappers(self) -> None:
        """Copy wrapper files to wrappers/ subdirectory."""
        print(f"  🔄 Copying wrappers...")
        
        wrappers_dir = self.target_dir / "wrappers"
        wrappers_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy Python wrapper
        python_src = self.source_dir / "wrapper.py"
        python_dst = wrappers_dir / "wrapper.py"
        if python_src.exists():
            shutil.copy2(python_src, python_dst)
            print(f"     ✅ Copied wrapper.py → wrappers/wrapper.py")
        else:
            print(f"     ⚠️  Warning: wrapper.py not found")
        
        # Copy C++ wrapper
        cpp_src = self.source_dir / "wrapper.cpp"
        cpp_dst = wrappers_dir / "wrapper.cpp"
        if cpp_src.exists():
            shutil.copy2(cpp_src, cpp_dst)
            print(f"     ✅ Copied wrapper.cpp → wrappers/wrapper.cpp")
        else:
            print(f"     ⚠️  Warning: wrapper.cpp not found")
    
    def migrate(self) -> bool:
        """Perform complete migration."""
        print(f"\n{'='*70}")
        print(f"Migrating: {self.source_dir.name} → {self.target_dir.name}")
        print(f"{'='*70}")
        
        try:
            # Create target directory
            self.target_dir.mkdir(parents=True, exist_ok=True)
            
            # Execute migration steps
            self.create_problem_description_json()
            self.create_combined_testcase_json()
            self.copy_templates()
            self.copy_wrappers()
            
            print(f"✅ Migration complete for {self.target_dir.name}!")
            return True
            
        except Exception as e:
            print(f"❌ Migration failed: {e}")
            return False


def migrate_from_config(config_file: Path) -> None:
    """Migrate multiple problems from a configuration file."""
    print(f"Reading configuration from: {config_file}")
    
    with open(config_file) as f:
        config = json.load(f)
    
    migrations = config.get("migrations", [])
    print(f"Found {len(migrations)} problems to migrate\n")
    
    success_count = 0
    failed = []
    
    for idx, migration_spec in enumerate(migrations, 1):
        print(f"\n[{idx}/{len(migrations)}] Processing migration...")
        
        migrator = ProblemMigrator(
            source_dir=migration_spec["source"],
            target_dir=migration_spec["target"],
            external_id=migration_spec["external_id"],
            title=migration_spec.get("title"),
            difficulty=migration_spec.get("difficulty"),
            sample_size=migration_spec.get("sample_size", 10),
            random_seed=migration_spec.get("random_seed", 42)
        )
        
        if migrator.migrate():
            success_count += 1
        else:
            failed.append(migration_spec["target"])
    
    # Summary
    print(f"\n{'='*70}")
    print(f"MIGRATION SUMMARY")
    print(f"{'='*70}")
    print(f"✅ Successful: {success_count}/{len(migrations)}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for target in failed:
            print(f"   - {target}")
    print(f"{'='*70}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Migrate Judge0 problems from any source folder to any target folder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "source",
        nargs="?",
        help="Source problem directory (e.g., dev_folder/problem_name, problems/my_problem, source/problem_xyz)"
    )
    
    parser.add_argument(
        "target",
        nargs="?",
        help="Target directory - can be any folder path (e.g., prod_folder/problem_name, output/my_problem, destination/problem_xyz)"
    )
    
    parser.add_argument(
        "--external-id",
        help="External ID for the problem (required for single migration)"
    )
    
    parser.add_argument(
        "--title",
        help="Problem title (optional, extracted from description.txt if not provided)"
    )
    
    parser.add_argument(
        "--difficulty",
        choices=["Easy", "Medium", "Hard"],
        help="Problem difficulty (optional, inferred if not provided)"
    )
    
    parser.add_argument(
        "--sample",
        type=int,
        default=10,
        help="Number of test cases to sample from each language (default: 10)"
    )
    
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducible sampling (default: 42)"
    )
    
    parser.add_argument(
        "--config",
        type=Path,
        help="JSON configuration file for batch migration"
    )
    
    args = parser.parse_args()
    
    # Config-based migration
    if args.config:
        if not args.config.exists():
            print(f"❌ Config file not found: {args.config}")
            return 1
        migrate_from_config(args.config)
        return 0
    
    # Single migration
    if not args.source or not args.target:
        parser.print_help()
        return 1
    
    if not args.external_id:
        print("❌ --external-id is required for single migration")
        return 1
    
    migrator = ProblemMigrator(
        source_dir=args.source,
        target_dir=args.target,
        external_id=args.external_id,
        title=args.title,
        difficulty=args.difficulty,
        sample_size=args.sample,
        random_seed=args.seed
    )
    
    success = migrator.migrate()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
