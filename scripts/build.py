# scripts/build.py
import os
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(PROJECT_ROOT, 'build')

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error: {command}")
        sys.exit(result.returncode)

def build():
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)
    os.chdir(BUILD_DIR)
    run_command("cmake ..")
    run_command("cmake --build .")
    print("Build successful.")

def clean():
    if os.path.exists(BUILD_DIR):
        for root, dirs, files in os.walk(BUILD_DIR, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(BUILD_DIR)
        print("Cleaned build directory.")
    else:
        print("No build directory to clean.")

def format_code():
    run_command("clang-format -i src/*.cpp")
    print("Code formatted successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 build.py [build|clean|format]")
        sys.exit(1)

    if sys.argv[1] == "build":
        build()
    elif sys.argv[1] == "clean":
        clean()
    elif sys.argv[1] == "format":
        format_code()
    else:
        print("Unknown command.")
