import os

def get_file_content(working_directory, file_path):

    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isfile(target_dir) == False:
        return f'Error: {target_dir} is not a directory'


