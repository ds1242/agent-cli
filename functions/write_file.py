import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file with content provided as an argument",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The required path to the file to be written or overwritten by the provided content",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write or overwrite the file"
            )
        }
    ),
)

def write_file(working_directory, file_path, content):

    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if valid_target_dir == False:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_path) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(working_dir_abs, exist_ok=True)

        with open(target_path, 'w') as f:
            f.write(content)

        return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"

    except Exception as e:
        return f"Error: unable to write to '{file_path}' due to : {e}"
    
    
