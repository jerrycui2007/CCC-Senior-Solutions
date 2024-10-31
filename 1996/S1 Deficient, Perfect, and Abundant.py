# https://dmoj.ca/problem/ccc96s1
from math import isqrt
from typing import Literal


def sum_proper_divisors(num: int) -> int:
    """
    Calculate the sum of all proper divisors of a number.
    
    A proper divisor is any positive divisor other than the number itself.
    Uses optimization to check only up to square root of the number.
    
    Args:
        num: The number to find proper divisors for
        
    Returns:
        The sum of all proper divisors
    """
    if num == 1:
        return 0
    
    total = 1  # Initialize with 1 since 1 is always a proper divisor
    
    # Only need to check up to square root of num
    for divisor in range(2, isqrt(num) + 1):
        if num % divisor == 0:
            total += divisor
            # If num/divisor is different from divisor, add it too
            pair = num // divisor
            if pair != divisor:
                total += pair
    
    return total


def classify_number(num: int) -> str:
    """
    Classify a number as perfect, deficient, or abundant.
    
    A number is perfect if sum of proper divisors equals the number.
    It is deficient if sum is less than the number.
    It is abundant if sum is greater than the number.
    
    Args:
        num: The number to classify
        
    Returns:
        A string describing the classification
    """
    divisor_sum = sum_proper_divisors(num)
    
    if divisor_sum == num:
        return f"{num} is a perfect number."
    
    classification = 'deficient' if divisor_sum < num else 'abundant'
    article = 'an' if classification == 'abundant' else 'a'
    return f"{num} is {article} {classification} number."


def main() -> None:
    """Process multiple test cases from input."""
    test_cases = int(input())
    for _ in range(test_cases):
        print(classify_number(int(input())))


if __name__ == "__main__":
    main()