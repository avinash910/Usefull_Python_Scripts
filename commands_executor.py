import subprocess

def run_commands_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                command = line.strip()
                if command:
                    print("Executing command:")
                    print(command)
                    try:
                        subprocess.run(command, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        print("Command failed with error: ")
                        print(e)
                        return 1  # Exit code 1 indicates failure
        print("All commands executed successfully.")
        return 0  # Exit code 0 indicates success
    except OSError:
        print("File not found:")
        print(file_path)
        return 1  # Exit code 1 indicates failure

if __name__ == "__main__":
    file_path = "commands.txt"  # Replace with the path to your commands file
    exit_code = run_commands_from_file(file_path)
    exit(exit_code)
