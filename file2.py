# file2.py
import file1

names = ["Alice", "Bob", "Charlie", ""]
for name in names:
    greeting = file1.greet(name)
    print(greeting)
