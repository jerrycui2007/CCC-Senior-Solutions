#https://dmoj.ca/problem/ccc96s4
ROMAN_TO_ARABIC = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

ARABIC_TO_ROMAN = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
)

OVERFLOW_MESSAGE = 'CONCORDIA CUM VERITATE'
MAX_VALUE = 1000


def roman_to_arabic(roman: str) -> int:
    """Convert Roman numeral to Arabic number.

    Args:
        roman: String containing Roman numeral

    Returns:
        Integer value of the Roman numeral
    """
    result = 0
    prev_value = 0
    
    # Iterate in reverse 
    for char in reversed(roman):
        curr_value = ROMAN_TO_ARABIC[char]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value
    
    return result


def arabic_to_roman(num: int) -> str:
    """Convert Arabic number to Roman numeral.

    Args:
        num: Integer to convert

    Returns:
        String containing Roman numeral representation
    """
    result = []
    
    for value, numeral in ARABIC_TO_ROMAN:
        count, num = divmod(num, value)
        result.append(numeral * count)
        
    return ''.join(result)


def process_expression(expression: str) -> str:
    """Process a single Roman numeral addition expression.

    Args:
        expression: String containing Roman numeral expression (e.g., 'X+V=')

    Returns:
        Complete expression with result
    """
    term1, term2 = expression[:-1].split('+')
    total = roman_to_arabic(term1) + roman_to_arabic(term2)
    
    result = OVERFLOW_MESSAGE if total > MAX_VALUE else arabic_to_roman(total)
    return f'{expression}{result}'


def main() -> None:
    """Process multiple test cases of Roman numeral additions."""
    for _ in range(int(input())):
        print(process_expression(input()))


if __name__ == '__main__':
    main()