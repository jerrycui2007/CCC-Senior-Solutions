# https://dmoj.ca/problem/ccc97s5
# Yeah I know I'm not supposed to use Python, I'm supposed to use strings or whatever, I don't care


def main() -> None:
    """Process multiple test cases of division."""
    test_cases = int(input())

    for _ in range(test_cases):
        dividend = int(input())
        divisor = int(input())

        print(dividend // divisor)
        print(dividend % divisor)
        print()


if __name__ == "__main__":
    main()
