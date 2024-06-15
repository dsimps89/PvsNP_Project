import os

def wrap_main_block(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    in_main_block = False
    updated_lines = []
    executable_code = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#') and not in_main_block:
            executable_code.append(line)
        else:
            updated_lines.append(line)
            if stripped_line == "if __name__ == '__main__':":
                in_main_block = True

    if executable_code:
        updated_lines.append("\nif __name__ == '__main__':\n")
        updated_lines.extend("    " + line for line in executable_code)

        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        print(f"Updated {file_path}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                wrap_main_block(file_path)

directories = [
    "p_vs_np/database_problems",
    "p_vs_np/flow_problems",
    "p_vs_np/graph_theory",
    "p_vs_np/network_design"
]

for directory in directories:
    process_directory(directory)
