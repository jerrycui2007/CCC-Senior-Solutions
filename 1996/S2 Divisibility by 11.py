# https://dmoj.ca/problem/ccc96s2

def check_divisibility(num: str) -> tuple[bool, list[int]]:
    """
    Check if a number is divisible by 11 using the divisibility rule.
    
    The rule: repeatedly remove the last digit and subtract it from the remaining number
    until we get a number that's small enough to easily check divisibility.
    
    Args:
        num: The number as a string
        
    Returns:
        A tuple containing:
        - Boolean indicating if number is divisible by 11
        - List of intermediate steps for output
    """
    steps = [int(num)]
    current = int(num)
    
    while current >= 11:
        last_digit = current % 10
        current = current // 10 - last_digit
        steps.append(current)
    
    return current % 11 == 0, steps


def format_output(num: str, steps: list[int], is_divisible: bool) -> None:
    """
    Format and print the output according to problem specifications.
    
    Args:
        num: Original number
        steps: List of intermediate steps
        is_divisible: Whether the number is divisible by 11
    """
    # Print each step of the process
    for step in steps:
        print(step)
    
    # Print the final result
    result = "is" if is_divisible else "is not"
    print(f"The number {num} {result} divisible by 11.")
    print()  # Empty line between test cases


def main() -> None:
    """Process multiple test cases from input."""
    test_cases = int(input())
    
    for _ in range(test_cases):
        num = input().strip()
        is_divisible, steps = check_divisibility(num)
        format_output(num, steps, is_divisible)


if __name__ == "__main__":
    main()