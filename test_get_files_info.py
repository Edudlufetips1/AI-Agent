from functions.get_files_info import get_files_info

def test():
    print("Result for current directory:")
    print("-" * 40)
    print(get_files_info("calculator", "."))
    print("-" * 40)

    print("Result for 'pkg' directory:")
    print("-" * 40)
    print(get_files_info("calculator", "pkg"))
    print("-" * 40)

    print("Result for '/bin' directory:")
    print("-" * 40)
    print(get_files_info("calculator", "/bin"))
    print("-" * 40)

    print("Result for '../' directory:")
    print("-" * 40)
    print(get_files_info("calculator", "../"))
    print("-" * 40)

if __name__ == "__main__":
    test()
