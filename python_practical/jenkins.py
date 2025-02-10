# jenkins_test.py
import sys

def main():
    print("Jenkins Test Script Running...")
    print("Python Version:", sys.version)
    print("Hello, Jenkins! The test was successful.")
    return 0  # Exit code 0 indicates success

if _name_ == "__main__":
    exit(main())