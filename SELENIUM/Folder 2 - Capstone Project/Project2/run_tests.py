import unittest
import pytest
import sys
import os
import argparse

def run_with_pytest():
    """Runs test suite using Pytest test runner and generates HTML report."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(base_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_path = os.path.join(reports_dir, "pytest_report.html")

    args = [
        os.path.join(base_dir, "tests"),
        "-v",
        f"--html={report_path}",
        "--self-contained-html"
    ]
    print(f"\n=======================================================")
    print(f"[RUNNER] Launching Framework Test Suite with Pytest...")
    print(f"=======================================================\n")
    exit_code = pytest.main(args)
    print(f"\n[PyTest Execution Completed] Exit code: {exit_code}")
    print(f"[HTML Report] Generated at: {report_path}\n")
    return exit_code

def run_with_unittest():
    """Runs test suite using Unittest discovery test runner."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")

    print(f"\n=======================================================")
    print(f"[RUNNER] Launching Framework Test Suite with Unittest...")
    print(f"=======================================================\n")

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=tests_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\n[Unittest Execution Summary]")
    print(f"Tests Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Selenium Automation Framework Runner")
    parser.add_argument(
        "--runner", 
        choices=["pytest", "unittest"], 
        default="pytest", 
        help="Specify test runner to execute suite (pytest or unittest)"
    )
    args = parser.parse_args()

    if args.runner == "pytest":
        sys.exit(run_with_pytest())
    else:
        sys.exit(run_with_unittest())
