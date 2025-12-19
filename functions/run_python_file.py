import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if valid_target_path == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(target_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if target_path.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
        if args is not None:
            command.extend(args)

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = ""

        if result.returncode != 0:
            output += f'Error: Process exited with code {result.returncode}'
        elif result.stdout == None or result.stderr == None:
            output += f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nNo output produced\n"
        else:
            output += f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nNo output produced\n"

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}\n"


