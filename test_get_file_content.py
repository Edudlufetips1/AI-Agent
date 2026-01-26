from functions.get_file_content import get_file_content

def test():
    print("Test 1: Get content of 'lorem.txt'")
    print("-" * 40)
    lorem = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(lorem)}")
    print(f"Last 120 chars:\n{lorem[-120:]}")
    print("-" * 40)

    print("Test 2: Get content of 'main.py'")
    print("-" * 40)
    print(get_file_content("calculator", "main.py"))
    print("-" * 40)

    print("Test 3: Get content of 'pkg/calculator.py'")
    print("-" * 40)
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("-" * 40)

    print("Test 4: Get content of '/bin/cat' (should error or not allowed)")
    print("-" * 40)
    print(get_file_content("calculator", "/bin/cat"))
    print("-" * 40)

    print("Test 5: Get content of 'pkg/does_not_exist.py' (should error)")
    print("-" * 40)
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("-" * 40)

if __name__ == "__main__":
    test()
