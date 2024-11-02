#!/usr/bin/env python3
# https://dmoj.ca/problem/ccc97s1


def generate_sentences(subjects: list[str], verbs: list[str], objects: list[str]) -> list[str]:
    """Generate all possible sentences in alphabetical order.
    
    Args:
        subjects: List of subject phrases
        verbs: List of verb phrases
        objects: List of object phrases
        
    Returns:
        List of complete sentences in strict alphabetical order
    """
    
    # Generate all combinations
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject} {verb} {obj}."
                sentences.append(sentence)
    
    return sorted(sentences, key=str.casefold)  # Use casefold for case-insensitive sorting


def main() -> None:
    """Process multiple test cases and output sentences for each."""
    test_cases = int(input())
    
    for _ in range(test_cases):
        # Read counts
        num_subjects = int(input())
        num_verbs = int(input())
        num_objects = int(input())
        
        # Read phrases
        subjects = [input() for _ in range(num_subjects)]
        verbs = [input() for _ in range(num_verbs)]
        objects = [input() for _ in range(num_objects)]
        
        # Generate and print sentences
        sentences = generate_sentences(subjects, verbs, objects)
        for sentence in sentences:
            print(sentence)


if __name__ == "__main__":
    main()
