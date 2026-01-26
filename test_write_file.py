from functions.write_file import write_file

def test():
    print("Test 1: Write to 'lorem.txt' in 'calculator'")
    print("-" * 40)
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("-" * 40)

    print("Test 2: Write to 'pkg/morelorem.txt' in 'calculator'")
    print("-" * 40)
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("-" * 40)

    print("Test 3: Write to '/tmp/temp.txt' (should NOT be allowed)")
    print("-" * 40)
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("-" * 40)

if __name__ == "__main__":
    test()
