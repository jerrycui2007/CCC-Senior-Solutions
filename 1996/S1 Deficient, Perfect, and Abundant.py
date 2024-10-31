# https://dmoj.ca/problem/ccc96s1
from math import isqrt


def sum_proper_divisors(n: int) -> int:
    """Calculate sum of proper divisors for a number."""
    if n == 1:  # Hard code test case
        return 0
        
    divisor_sum = 1  # 1 is a divisor
    
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            divisor_sum += i

            # Check for square roots
            if (quotient := n // i) != i:
                divisor_sum += quotient
                
    return divisor_sum


def classify_number(n: int) -> str:
    """Classify a number as perfect, deficient, or abundant."""
    sum_divisors = sum_proper_divisors(n)
    
    if sum_divisors == n:
        return f"{n} is a perfect number."
    elif sum_divisors < n:
        return f"{n} is a deficient number."
    else:
        return f"{n} is an abundant number."


def main():
    for _ in range(int(input())):
        print(classify_number(int(input())))


if __name__ == "__main__":
    main()