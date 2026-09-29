from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    result = {}
    x = [float(i) for i in x]
    sorted_x = sorted(x)
    
    result["mean"] = float(sum(x) / len(x))
    
    if len(x) % 2 == 1:
        median = sorted_x[(len(x) // 2)]
    else:
        median = (sorted_x[(len(x) // 2) - 1] + sorted_x[(len(x) // 2)]) / 2
    result["median"] = float(median)

    counts = Counter(x)
    mode_item, frequency = counts.most_common(1)[0]
    result["mode"] = float(mode_item)

    return result