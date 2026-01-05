def add(a, b):
    return a + b


def main():
    print("Hello from Python app running in Jenkins!")
    result = add(2, 3)
    print(f"3 + 3 = {result}")


if __name__ == "__main__":
    main()

