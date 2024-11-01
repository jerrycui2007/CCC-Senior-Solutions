# https://dmoj.ca/problem/ccc96s3
from itertools import combinations


def generate_bit_patterns(n: int, k: int) -> list[str]:
    """Generate all possible bit patterns of length n containing exactly k ones.

    Args:
        n: Length of the bit pattern
        k: Number of ones required in each pattern

    Returns:
        List of strings representing all possible bit patterns
    """
    return [''.join('1' if i in ones else '0' for i in range(n)) for ones in combinations(range(n), k)]


def main() -> None:
    """Process multiple test cases and output the bit patterns."""
    test_cases = int(input())
    
    for i in range(test_cases):
        n, k = map(int, input().split())
        patterns = generate_bit_patterns(n, k)
        
        print("The bit patterns are")
        print(*patterns, sep='\n')
        
        # Print newline between test cases, but not after the last one
        if i < test_cases - 1:
            print()


if __name__ == "__main__":
    main()

