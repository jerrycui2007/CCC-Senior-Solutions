# https://dmoj.ca/problem/ccc96s5


def find_maximum_distance(length: int, x: list[int], y: list[int]) -> int:
    """Find the maximum distance between matching elements in arrays x and y.
    
    The distance is calculated as j-i where:
    - i is the index of a number in array x
    - j is the index of the same number in array y
    - only the leftmost occurrence in x and rightmost occurrence in y are considered
    
    Args:
        length: The length of both arrays
        x: First array of integers
        y: Second array of integers
        
    Returns:
        Maximum distance found between any matching elements
    """
    # Store first occurrence of each number in x
    first_x = {}
    for i, num in enumerate(x):
        if num not in first_x:
            first_x[num] = i
    
    # Store last occurrence of each number in y
    last_y = {}
    for i in range(length - 1, -1, -1):
        if y[i] not in last_y:
            last_y[y[i]] = i
    
    # Calculate maximum distance
    max_distance = 0
    for num in first_x:
        if num in last_y:
            max_distance = max(max_distance, last_y[num] - first_x[num])
    
    return max_distance


def main() -> None:
    """Process multiple test cases and output the maximum distance for each."""
    test_cases = int(input())
    
    for _ in range(test_cases):
        length = int(input())
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        
        result = find_maximum_distance(length, x, y)
        print(f"The maximum distance is {result}")


if __name__ == "__main__":
    main()