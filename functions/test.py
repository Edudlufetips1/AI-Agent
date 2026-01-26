from get_files_info import get_dirs_info
from get_files_info import (
    get_files_info,
    get_dirs_info,
    get_files_only_info,
)

print("Result for files-only in current directory:")
print(get_files_only_info("calculator", "."))
print(get_dirs_info("calculator", "."))