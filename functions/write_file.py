import os

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