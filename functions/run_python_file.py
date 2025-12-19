import os

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if valid_target_path == False:
            return f'Error: Cannot execute "{file_path}" as it is outsie the permitted working directory'

        if os.path.isfile(file_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]
        command.extend(args)

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
                return f'Error: Process exited with code {result.returncode}'



