# https://dmoj.ca/problem/ccc97s4


def encode_text(text: str) -> list[str]:
    """Encode text using dynamic dictionary coding.
    
    Words are replaced with their dictionary index when they appear again.
    New words are added to the dictionary with the next available index.
    
    Args:
        text: Input text to encode
        
    Returns:
        List of encoded words (mix of strings and numbers)
    """
    dictionary = {}
    counter = 1
    words = text.split()
    encoded = []
    
    for word in words:
        if word in dictionary:
            encoded.append(str(dictionary[word]))
        else:
            dictionary[word] = counter
            counter += 1
            encoded.append(word)
    
    return encoded


def process_paragraph() -> list[list[str]]:
    """Process a paragraph of text until empty line is encountered.
    
    Returns:
        List of encoded lines, where each line is a list of encoded words
    """
    result = []
    while True:
        line = input()
        if not line:  # Empty line marks end of paragraph
            break
        result.append(encode_text(line))
    return result


def main() -> None:
    """Process multiple test cases of text encoding."""
    test_cases = int(input())
    
    for i in range(test_cases):
        encoded_lines = process_paragraph()
        
        # Print encoded lines
        for line in encoded_lines:
            print(*line)
        
        # Print newline between test cases (except for last case)
        if i < test_cases - 1:
            print()


if __name__ == "__main__":
    main()
