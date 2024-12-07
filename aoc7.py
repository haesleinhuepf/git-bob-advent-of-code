import itertools

def evaluate_expression(numbers, operators):
    """
    Evaluate expression with given numbers and operators left-to-right.
    
    Parameters
    ----------
    numbers : list of int
        Numbers in the expression
    operators : list of str
        Operators (+, *) between numbers
        
    Returns
    -------
    result : int
        Result of evaluating the expression
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        else:
            result *= numbers[i+1]
    return result

def can_make_test_value(test_value, numbers):
    """
    Check if test value can be made with any combination of operators.
    
    Parameters
    ----------
    test_value : int
        Target value to achieve
    numbers : list of int
        Numbers to combine with operators
        
    Returns
    -------
    bool
        True if test value can be achieved, False otherwise
    """
    ops = ['+', '*']
    for operators in itertools.product(ops, repeat=len(numbers)-1):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def solve(input_file):
    """
    Solve the calibration problem from input file.
    
    Parameters
    ----------
    input_file : str
        Path to input file
        
    Returns
    -------
    int
        Sum of test values that can be achieved
    """
    total = 0
    with open(input_file) as f:
        for line in f:
            parts = line.strip().split(':')
            test_value = int(parts[0])
            numbers = [int(x) for x in parts[1].strip().split()]
            
            if can_make_test_value(test_value, numbers):
                total += test_value
                
    return total

if __name__ == "__main__":
    result = solve("aoc7.txt")
    print(f"Total calibration result: {result}")
