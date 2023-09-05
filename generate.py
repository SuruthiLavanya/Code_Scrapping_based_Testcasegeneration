import random
import subprocess
import ast
MAX_LINES = 1000

def read_input_file(file_path):
    with open(file_path) as f:
        input_str = f.read()
    return input_str

def generate_random_values(num_values):
    return [random.randint(1, 100) for _ in range(num_values)]

def execute_python_file(file_path):
    # read the input file
    code_str = read_input_file(file_path)
    
    # create a local namespace for the execution of the code
    namespace = {}
    
    # execute the code in the local namespace
    exec(code_str, namespace, namespace)
    
    # check if the code defines a function
    func_name = None
    for node in ast.walk(ast.parse(code_str)):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            break
    
    """if func_name is None:
        # if the code does not define a function, assume the last expression is the output
        output = eval(code_str, namespace, namespace)
        print(f"Output of {file_path}: {output}")
    else:
        # get the function object
        func_obj = namespace[func_name]
        
        # generate random values for the function parameters
        input_param_names = [arg.arg for arg in func_obj.__code__.co_varnames]
        num_params = len(input_param_names)
        input_values = generate_random_values(num_params)
        
        # call the function with the random values
        result = func_obj(*input_values)
        
        # print the output
        print(f"Output of {func_name} with input {input_values}: {result}")
    print()"""

def execute_c_file(file_path):
    # read the input file
    code_str = read_input_file(file_path)
    
    # compile the C program
    subprocess.run(['gcc', '-o', 'output', file_path])
    
    # execute the compiled program
    result = subprocess.run(['./output'], capture_output=True, text=True)
    
    # print the output
    print(f"Output of {file_path}:")
    print(result.stdout)
    
    if result.stderr:
        print("Error:")
        print(result.stderr)
    
    print()

def execute_java_program(java_file_path):
    # Compile the Java program
    compile_command = ["javac", java_file_path]
    compile_process = subprocess.Popen(compile_command, stderr=subprocess.PIPE)
    compile_output, compile_error = compile_process.communicate()

    if compile_error:
        print(f"Compilation error: {compile_error.decode('utf-8').strip()}")
        return

    # Get the class name from the Java file path
    java_file_name = java_file_path.split("\\")[-1]
    class_name = java_file_name.replace(".java", "")

    # Execute the Java program
    classpath = java_file_path.rsplit("\\", 1)[0]
    execute_command = ["java", "-classpath", classpath, class_name]
    execute_process = subprocess.Popen(execute_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    execute_output, execute_error = execute_process.communicate()

    if execute_error:
        print(f"Execution error: {execute_error.decode('utf-8').strip()}")
        return

    # Display the output
    print(f"Output of {java_file_path}:")
    print(execute_output.decode('utf-8').strip())

        
def execute_smalltalk_code(file_path):
    # read the input file
    code_str = read_input_file(file_path)
    
    # execute the Smalltalk code using the gst interpreter
    result = subprocess.run(['gst', '-e', code_str], capture_output=True, text=True)
    
    # print the output
    print(f"Output of {file_path}:")
    print(result.stdout)
    
    if result.stderr:
        print("Error:")
        print(result.stderr)
    
    print()
    

def execute_cpp_program(cpp_file_path):
    # Compile the C++ program
    compile_command = ["g++", cpp_file_path, "-o", "program"]
    compile_process = subprocess.Popen(compile_command, stderr=subprocess.PIPE)
    compile_output, compile_error = compile_process.communicate()

    if compile_error:
        print(f"Compilation error: {compile_error.decode('utf-8').strip()}")
        return

    # Execute the compiled program
    execute_command = ["./program"]
    execute_process = subprocess.Popen(execute_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    execute_output, execute_error = execute_process.communicate()

    if execute_error:
        print(f"Execution error: {execute_error.decode('utf-8').strip()}")
        return

    # Display the output
    print(f"Output of {cpp_file_path}:")
    print(execute_output.decode('utf-8').strip())

if __name__ == "__main__":
    input_file_path ="D:\LAM FILES\python program\Deepak\my_semi.py"

    
    
    if input_file_path.endswith(".py"):
        execute_python_file(input_file_path)
    elif input_file_path.endswith(".c"):
        execute_c_file(input_file_path)
    elif input_file_path.endswith(".java"):
        execute_java_program(input_file_path)
    elif input_file_path.endswith(".st"):
        execute_smalltalk_code(input_file_path)
    elif input_file_path.endswith(".cpp"):
        execute_cpp_program(input_file_path)                                  
    else:
        print("Unsupported file type. Please provide a Python, C, Java, C++ or smalltalk file.")

import re

MAX_LINES = 1000

def get_entry_count(program):
    # The entry count is always 1 for a Python program
    return 1

def get_conditional_count(program):
    count = 0
    for line in program:
        if re.search(r'\b(if|for|while|switch)\b', line):
            count += 1
    return count

if __name__ == '__main__':
    program = []
    line_num = 0
    entry_count, conditional_count, cyclomatic_complexity = 0, 0, 0

    # Read the program file 
    with open("D:\LAM FILES\python program\Deepak\my_semi.py") as fp:
        for line in fp:
            program.append(line)
        
    
    # Calculate the entry and conditional counts
    entry_count = get_entry_count(program)
    conditional_count = get_conditional_count(program)

    # Calculate cyclomatic complexity
    cyclomatic_complexity = conditional_count - entry_count + 2

    print(f"Entry count: {entry_count}")
    print(f"Conditional count: {conditional_count}")
    print(f"Cyclomatic complexity: {cyclomatic_complexity}")

