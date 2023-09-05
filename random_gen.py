# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

operators = ['-', '-', '>', '<', '>']
constants = [-50, -20, 120, 0, 100]

for operator in range(len(operators)):
    if operators[operator] == '-':
        lower_limit = -50
        upper_limit = constants[operator]
    elif operators[operator] == '>':
        lower_limit = constants[operator]
        upper_limit = 150
    elif operators[operator] == '<':
        lower_limit = -20
        upper_limit = constants[operator]
    else:
        lower_limit = -50
        upper_limit = 150
    
    value = random.uniform(lower_limit, upper_limit)
    print(f"Operator: {operators[operator]}, Constant: {constants[operator]}, Value: {value}")
