from functions.get_files_info import get_files_info

def get_results(output, directory):
    print(f"Result for {directory}:")

    if isinstance(output, list):
        for item in output:
            print(item)
    else:
        print(output)

def test():
    output = get_files_info("calculator", '.')
    get_results(output, '.')

    output = get_files_info("calculator", "pkg")
    get_results(output, "pkg")

    output = get_files_info("calculator", "/bin")
    get_results(output, "/bin")

    output = get_files_info("calculator", "../")
    get_results(output, "../")

if __name__ == "__main__":
    test()

