import os
from config import MAX_CHARS
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file = os.path.normpath(os.path.join(abs_working, file_path))
        
        common = os.path.commonpath([abs_file, abs_working])
        if common != abs_working:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(abs_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except Exception as e:
        return f'Error: {e}'
    
schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Displays a truncated string of file content at a specified file path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "content": types.Schema(
                type=types.Type.STRING,
                description="Truncated content string of a file's content, displayed as a a string, at a specified file path relative to the working directory",
            ),
        },
    ),
)