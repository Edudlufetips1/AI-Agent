import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(abs_path, directory)
    target_dir = os.path.normpath(full_path)
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    lines = []

    for name in os.listdir(target_dir):
        full_path = os.path.join(target_dir, name)
        is_dir = os.path.isdir(full_path)
        file_size = os.path.getsize(full_path)
        line = f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
        lines.append(line)
    return "\n".join(lines)

def get_dirs_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(abs_path, directory)
    target_dir = os.path.normpath(full_path)
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    lines = []

    for name in os.listdir(target_dir):
        full_path = os.path.join(target_dir, name)
        is_dir = os.path.isdir(full_path)
        if not is_dir:
            continue
        file_size = os.path.getsize(full_path)
        line = f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
        lines.append(line)
    return "\n".join(lines)

def get_files_only_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(abs_path, directory)
    target_dir = os.path.normpath(full_path)
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    lines = []

    for name in os.listdir(target_dir):
        full_path = os.path.join(target_dir, name)
        is_dir = os.path.isdir(full_path)
        if is_dir:
            continue
        file_size = os.path.getsize(full_path)
        line = f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
        lines.append(line)
    return "\n".join(lines)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)