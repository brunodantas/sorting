from typing import List

def countingsort(lst: List[int]) -> List[int]:
    """Simple counting sort implementation assuming non-negative integers"""
    # Handle empty list
    if not lst:
        return []
    
    # Find the maximum value
    max_val = max(lst)

    # Initialize occurrences list
    # Using list multiplication for better performance
    occurs = [0] * (max_val + 1)
    
    # Count occurrences
    for e in lst:
        occurs[e] += 1
    
    # Build output list
    out = []
    for index, occur in enumerate(occurs):
        if occur > 0:
            # Add the element index, occur times
            out += [index] * occur
    
    return out
