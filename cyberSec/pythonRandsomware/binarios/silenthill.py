import os
import subprocess
def give_execution_permission(file_path):
    # The current permissions
    current_permissions = os.stat(file_path).st_mode

    # Add execution permissions for the user
    os.chmod(file_path, current_permissions | os.X_OK)

# Usage
give_execution_permission('darthvader_linux')
def run_binary():
    if os.name == 'nt':  # Windows
        subprocess.run(["./darthvader_windows.exe"])
    else:  # Linux
        give_execution_permission('darthvader_linux')
        subprocess.run(["./darthvader_linux"])
# Usage
run_binary()