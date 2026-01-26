from functions.run_py_file import run_python_file

def test():
    print("Test 1: run_python_file('calculator', 'main.py')")
    print(run_python_file("calculator", "main.py"))
    print("-" * 40)

    print("Test 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("-" * 40)

    print("Test 3: run_python_file('calculator', 'tests.py')")
    print(run_python_file("calculator", "tests.py"))
    print("-" * 40)

    print("Test 4: run_python_file('calculator', '../main.py')")
    print(run_python_file("calculator", "../main.py"))
    print("-" * 40)

    print("Test 5: run_python_file('calculator', 'nonexistent.py')")
    print(run_python_file("calculator", "nonexistent.py"))
    print("-" * 40)

    print("Test 6: run_python_file('calculator', 'lorem.txt')")
    print(run_python_file("calculator", "lorem.txt"))
    print("-" * 40)

if __name__ == "__main__":
    test()
