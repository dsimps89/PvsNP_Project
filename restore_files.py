import os
import re

def remove_functions_and_blocks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove the main() function, the test() function, and the __main__ block
    content = re.sub(r'\n*def main\(\):.*?\n\s*def test\(\):.*?\n\s*if __name__ == \'__main__\':.*?\n\s*main\(\)', '', content, flags=re.DOTALL)

    with open(file_path, 'w') as file:
        file.write(content)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                remove_functions_and_blocks(file_path)

process_directory('p_vs_np')
