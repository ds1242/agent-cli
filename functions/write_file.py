

def write_file(working_directory, file_path, content):

    working_dir_abs = os.path.abspath(working_directory)

    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot read "{file_path} as it is outside the permitted working directory'
    
    if os.path.isfile(target_path) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
