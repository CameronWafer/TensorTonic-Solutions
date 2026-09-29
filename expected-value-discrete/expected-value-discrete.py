import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x = [float(i) for i in x]
    p = [float(i) for i in p]
    
    nums = []
    for i in range(len(x)):
        rv = x[i] * p[i]
        nums.append(rv)
    
    return sum(nums)