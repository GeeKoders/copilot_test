import string
from collections import defaultdict

def clean_text(line: str) -> list[str]:
    """Lowercase, remove punctuation, and split into tokens."""
    translator = str.maketrans('', '', string.punctuation)
    return line.lower().translate(translator).split()

def count_tokens(tokens: list[str], counts: dict[str, int]) -> None:
    """Update counts dict with token frequencies."""
    for token in tokens:
        counts[token] += 1

def process_transcript(lines: list[str]) -> dict[str, int]:
    """Return word-count mapping for a chat transcript."""
    counts: dict[str, int] = defaultdict(int)
    for line in lines:
        tokens = clean_text(line)
        count_tokens(tokens, counts)
    most_common = max(counts.items(), key=lambda kv: kv[1])
    print(f"Most common word → {most_common[0]} ({most_common[1]})")
    return dict(counts)

# Sample input and function call
lines = [
    "Hello, how are you?",
    "I am fine. How are you doing?",
    "I am doing well. Thank you!"
]

# Call the function and store the result
word_counts = process_transcript(lines)

# Print the full word count dictionary
print(word_counts)