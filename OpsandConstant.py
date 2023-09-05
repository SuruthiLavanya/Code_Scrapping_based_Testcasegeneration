import ast
import random
import contextlib
import sys


# Sample code snippet
"""
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

def read_input_file(file_path):
    with open(file_path) as f:
        input_str = f.read()
    return input_str

code = read_input_file("D:\LAM FILES\python program\Deepak\my_semi.py")

# Parse the code
parsed_code = ast.parse(code)

# Define a visitor to extract comparison operators and constants
class ConditionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.operators = []
        self.constants = []

    def visit_Compare(self, node):
        for op, constant in zip(node.ops, node.comparators):
            if isinstance(constant, ast.Constant):
                operator = self.get_operator_name(op)
                constant_value = constant.value
                self.operators.append(operator)
                self.constants.append(constant_value)
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.USub):
            operator = "-"
            constant_value = node.operand.value
            self.operators.append(operator)
            self.constants.append(-constant_value)
        self.generic_visit(node)

    @staticmethod
    def get_operator_name(op_node):
        if isinstance(op_node, ast.Lt):
            return "<"
        elif isinstance(op_node, ast.LtE):
            return "<="
        elif isinstance(op_node, ast.Gt):
            return ">"
        elif isinstance(op_node, ast.GtE):
            return ">="
        elif isinstance(op_node, ast.Eq):
            return "=="
        elif isinstance(op_node, ast.NotEq):
            return "!="

# Visit the AST to extract comparison operators and constants
visitor = ConditionVisitor()
visitor.visit(parsed_code)

# Print the extracted data as lists
#print("Operators:", visitor.operators)
#print("Constants:", visitor.constants)

operators = visitor.operators
constants = visitor.constants

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
    
    value = random.uniform(lower_limit, upper_limit)
    generated_values.append(value)
value = random.uniform(0,100)
generated_values.append(value)

# Modify and execute the given code with generated values
with contextlib.redirect_stdout(sys.stdout):
    for value in generated_values:
        modified_code = code.replace("{}", str(value))
        exec(modified_code)
