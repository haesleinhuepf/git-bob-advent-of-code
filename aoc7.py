from itertools import product
from operator import add, mul

def evaluate_expr(nums, ops):
    """
    Evaluate expression with given numbers and operators left-to-right.
    
    Parameters
    ----------
    nums : list
        List of numbers
    ops : list 
        List of operator functions
    
    Returns
    -------
    int
        Result of expression evaluation
    """
    result = nums[0]
    for i, op in enumerate(ops):
        result = op(result, nums[i+1])
    return result

def find_valid_equations(filename):
    """
    Find equations that can be satisfied with + and * operators.
    
    Parameters
    ----------
    filename : str
        Input file containing equations
        
    Returns
    -------
    int
        Sum of test values for valid equations
    """
    operators = {'+': add, '*': mul}
    total = 0
    
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(':')
            test_value = int(parts[0])
            nums = [int(x) for x in parts[1].split()]
            
            # Try all possible operator combinations
            for ops in product(operators.values(), repeat=len(nums)-1):
                if evaluate_expr(nums, ops) == test_value:
                    total += test_value
                    break
                    
    return total

if __name__ == "__main__":
    result = find_valid_equations("aoc7.txt")
    print(f"Total calibration result: {result}")
