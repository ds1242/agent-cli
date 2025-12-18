import os

def get_files_info(working_directory, directory="."):

    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isdir(directory) == False:
        return f'Error: {directory} is not a directory'


    directory_contents = os.listdir()

    output = []

    for item in directory_contents:
        try: 
            file_size = os.path.getsize(item)
            is_dir = os.path.isdir(item)
            
            output.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
        except:
            f'Error: Cannot list "{item}" as it is outside the permitted working directory'

    return output

