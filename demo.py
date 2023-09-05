import ast

# Read the content of file1.py
with open('file1.py', 'r') as file1_content:
    file1_code = file1_content.read()



def read_input_file(file_path):
    
    with open(file_path) as f:
        input_str = f.read()
    return input_str

code = read_input_file("file2.py")
print(code)

# Parse the AST of file2.py

file2_ast = ast.parse(code)

# Define a custom AST visitor to find the import and usage of greet function
class GreetVisitor(ast.NodeVisitor):
    def __init__(self):
        self.greet_usage_found = False

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name == "file1":
                self.greet_usage_found = True
        self.generic_visit(node)

    def visit_Name(self, node):
        if self.greet_usage_found and node.id == "greet":
            # The node here represents the usage of greet function
            print("Found usage of greet function in file2.py")
            self.greet_usage_found = False  # Reset the flag
        self.generic_visit(node)

# Instantiate the visitor and traverse the AST
greet_visitor = GreetVisitor()
greet_visitor.visit(file2_ast)
