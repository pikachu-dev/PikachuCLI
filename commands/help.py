# Module Imports
import os
import subprocess
import sys

# Stop Script Function

def stop_script():
    print("Stopping this script and executing the welcome screen")
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the Command-Line-Interface
    subprocess.run([sys.executable, "welcome.py"]) # Execute another script
    sys.exit()

# Commands List as Variable
commands = r"""
'help' - Displays all available commands
'clear_credentials' - Clear the credentials.json file
"""

# Clear the Console
os.system('cls' if os.name == 'nt' else 'clear') # Clear the Command-Line-Interface

# Print the commands
print(f"\n{commands}")