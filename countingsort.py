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
    for i in lst:
        occurs[i] += 1
    
    # Build output list
    out = []
    for i, v in enumerate(occurs):
        if v > 0:
            # Add the element index, occur times
            out += [i] * v
    
    return out