#TASK 1
import subprocess
import os

# List of Python scripts to run sequentially
scripts = ['script1.py', 'script2.py', 'script3.py']

for script in scripts:
    if os.path.exists(script):
        print(f"\n🔹 Executing {script}...")
        # Use 'python' for Windows
        result = subprocess.run(['python', script])

        # Check return code
        if result.returncode == 0:
            print(f"{script} completed successfully.\n")
        else:
            print(f"Error executing {script} (Return code: {result.returncode})\n")
    else:
        print(f"File not found: {script}")
