import os

def add_main_function(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if 'main' function already exists
    for line in lines:
        if 'def main()' in line:
            return

    # Add main function if it doesn't exist
    with open(file_path, 'a') as file:
        file.write("\n\ndef main():\n")
        file.write("    pass\n")
        file.write("\n\nif __name__ == '__main__':\n")
        file.write("    main()\n")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_main_function(file_path)

if __name__ == "__main__":
    directory = "p_vs_np"  # Change this to your actual package directory
    process_directory(directory)
    print("Main functions added where necessary.")
