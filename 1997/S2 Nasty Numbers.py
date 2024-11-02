#https://dmoj.ca/problem/ccc97s2
from math import isqrt


def is_nasty_number(n: int) -> bool:
    """Determine if a number is nasty.
    
    A number is nasty if it has two different pairs of factors (a,b) and (c,d)
    where a*b = c*d = n and either:
    - a + b = c - d, or
    - a + b = d - c
    
    Args:
        n: Number to check
        
    Returns:
        True if the number is nasty, False otherwise
    """
    sums = set()
    diffs = set()
    
    # Get all factors
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            j = n // i 
            curr_sum = i + j
            curr_diff = abs(j - i)
            
            if curr_sum in diffs or curr_diff in sums:
                return True
                
            sums.add(curr_sum)
            diffs.add(curr_diff)
    
    return False


def main() -> None:
    """Process multiple test cases and determine if each number is nasty."""
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        result = "is nasty" if is_nasty_number(n) else "is not nasty"
        print(f"{n} {result}")


if __name__ == "__main__":
    main()
