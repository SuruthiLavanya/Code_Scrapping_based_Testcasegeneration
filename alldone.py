import random
import contextlib
import sys

# Given code
given_code = """
def test_temperature_sensor():
    temperature = {}
    if temperature < -20 or temperature > 120:
        print(f"Error: Out of range temperature reading detected: {temperature}")
    elif temperature < 0:
        print(f"Warning: Below freezing temperature reading detected: {temperature}")
    elif temperature > 100:
        print(f"Warning: High temperature reading detected: {temperature}")
    else:
        print(f"Temperature reading within acceptable range: {temperature}")

test_temperature_sensor()
"""

# Generating random values
operators = ['-', '>', '<', '>']
constants = [-20, 120, 0, 100]
generated_values = []

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
    generated_values.append(value)
value = random.uniform(0,100)
generated_values.append(value)

# Modify and execute the given code with generated values
with contextlib.redirect_stdout(sys.stdout):
    for value in generated_values:
        modified_code = given_code.replace("{}", str(value))
        exec(modified_code)
