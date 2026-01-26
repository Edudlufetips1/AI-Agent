import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_path = os.path.abspath(working_directory)
        full_path = os.path.join(abs_path, file_path)
        target_dir = os.path.normpath(full_path)
        valid_target_dir = os.path.commonpath([target_dir, abs_path]) == abs_path
        
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        parent_dir = os.path.dirname(target_dir)
        os.makedirs(parent_dir, exist_ok=True)

        with open(target_dir, 'w') as f:
            f.write(content)
    except Exception as e:
        return f'Error: writing to file: {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Accepts user input as content to be written to a file at a given file path in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file relative to the working directory"),
            "content": types.Schema(
                type=types.Type.STRING,
                description="user-provided content to write to a file at given file path"),
        },
        required=["file_path", "content"]
    ),
)