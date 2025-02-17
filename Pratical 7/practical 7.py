import re
import os

memory_allocation = {'int': 4, 'float': 4, 'double': 8, 'char': 1, 'bool': 1, 'long': 8, 'short': 2}

def find_declarations(code):
    patterns = [r'\b(int|float|double|char|bool|long|short)\s+(\w+)(?:\s*=\s*(\w*))?\s*[;,]']
    variables = [{'name': m[1], 'type': m[0], 'initialized': m[2] if m[2] else 'None', 'used': False} 
                 for m in re.findall(patterns[0], code)]
    return variables

def find_usage(code, variables):
    for var in variables:
        if re.search(r'\b' + var['name'] + r'\b', code): var['used'] = True

def generate_symbol_table(variables):
    return [[i+1, 
             var['name'], 
             var['type'], 
             '1' if var['used'] else '0', '1', 
             memory_allocation.get(var['type'], 
            'Unknown')] 
            for i, var in enumerate(variables)]

def print_symbol_table(table):
    print(f"{'ID':<5}{'Variable':<15}{'Data Type':<15}{'Used':<10}{'Defined':<10}{'Memory Allocation'}")
    print("=" * 60)
    for row in table:
        print(f"{row[0]:<5}{row[1]:<15}{row[2]:<15}{row[3]:<10}{row[4]:<10}{row[5]}")

def analyze_code(file_path):
    if not os.path.exists(file_path): return print("File does not exist!")
    with open(file_path, 'r') as file: code = file.read()
    variables = find_declarations(code)
    find_usage(code, variables)
    print_symbol_table(generate_symbol_table(variables))

# Example usage:
file_path = r'C:\Users\admin\Desktop\mitesh\sample.txt'  # Replace with your file path
analyze_code(file_path)
