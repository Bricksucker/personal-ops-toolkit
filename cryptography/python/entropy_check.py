import math
from collections import Counter

def shannon_entropy(data: str) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    length = len(data)
    entropy = -sum((count/length) * math.log2(count/length) for count in counts.values())
    return entropy

password = "Tr0ub4dor&3"
print(f"Entropy: {shannon_entropy(password):.2f} bits per character")
