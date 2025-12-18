import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):

    working_dir_abs = os.path.abspath(working_directory)

    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot read "{file_path} as it is outside the permitted working directory'
    
    print(target_path)
    if os.path.isfile(target_path) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_path, "r") as f:
            content = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return content
    except: 
        return f"Error: Unable to read file"


