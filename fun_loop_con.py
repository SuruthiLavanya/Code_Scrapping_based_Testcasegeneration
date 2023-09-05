import ast

class MyVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"\nFound function: ",ast.dump(node))
        self.generic_visit(node)  

    def visit_If(self, node):
        print("\nFound if condition:",ast.dump(node))
        
        if node.orelse and not any(isinstance(orelse, ast.If) for orelse in node.orelse): 
            print("\nFound else block:")
            for statement in node.orelse:
                print(ast.dump(statement))
            
        self.generic_visit(node)

    def visit_While(self, node):
        print("\nFound while loop:",ast.dump(node))
        self.generic_visit(node)
    def visit_For(self,node):
        print("\nFound For loop:",ast.dump(node))
        self.generic_visit(node)
        
        
        
        
'' '''
    
# file2.py
import file1

names = ["Alice", "Bob", "Charlie", ""]
for name in names:
    greeting = file1.greet(name)
    print(greeting)
def greet(name):
    if len(name) > 0:
        return f"Hello, {name}!"
    else:
        return "Hello, anonymous!"

'''''''

''' """
def my_function():
    print("Hello")
    my()
def my():
    print("Hi")
i = 3
while i != 0:
    print(i)
    i -= 1

my_function()
my()
def test_temperature_sensor():
    for i in range(3):
        if temperature < -20 or temperature > 120:
            print(f"Error: Out of range temperature reading detected: {temperature}")
        elif temperature < 0:
            print(f"Warning: Below freezing temperature reading detected: {temperature}")
        elif temperature > 100:
            print(f"Warning: High temperature reading detected: {temperature}")
        else:
            print(f"Temperature reading within acceptable range: {temperature}")
    while(i!=0):
    	print(i)

if 10 > 0:
    print("YES")
"""



def read_input_file(file_path):
    print(file_path)
    with open(file_path) as f:
        input_str = f.read()
    return input_str

code = read_input_file("file2.py")



# Parse the code
parsed_code = ast.parse(code)

# Create an instance of the visitor and visit the AST
visitor = MyVisitor()
visitor.visit(parsed_code)
