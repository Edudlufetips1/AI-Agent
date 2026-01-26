import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path = os.path.abspath(working_directory)
        full_path = os.path.join(abs_path, file_path)
        target_dir = os.path.normpath(full_path)
        
        if os.path.commonpath([abs_path, target_dir]) != abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        absolute_file_path = target_dir
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=abs_path, capture_output=True, text=True, timeout=30)
        output = []
        
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        if not result.stdout and not result.stderr:
            output.append('No output produced')
        if result.stdout:
            output.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
            output.append(f'STDERR:\n{result.stderr}')
        return "\n".join(output) 
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    