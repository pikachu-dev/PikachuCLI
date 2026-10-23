# Modules
import secrets # for Secrets-Generation
import json # for Reading and Writing JSON-Files
import os # for getting the Path of the JSON-Files
import subprocess
import sys

# Global Variables

# - Single-User-Registration Variables
single_user_registration_status = True
single_user_registration_token = secrets.token_urlsafe(48)
email = None
username = None
password = None

# Functions

def stop_script():
    print("Stopping this script and executing the welcome screen")
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the Command-Line-Interface
    subprocess.run([sys.executable, "welcome.py"]) # Execute another script
    sys.exit() # Stop current script

def register_user():
    global email, username, password
    print("\nWelcome, User!")
    print("\nPlease enter your personal information to register an account:")
    # Ask for E-Mail-Address
    email = input("\nE-Mail-Address: ")
    username = input("\nUsername: ")
    password = input("\nPassword: ")

    # Create a JSON-Dictionary for credentials.json
    credentials = {
        "single_user_registration_status": single_user_registration_status,
        "single_user_registration_token": single_user_registration_token,
        "email": email,
        "username": username,
        "password": password
    }

    # Write the JSON-File credentials.json
    file_path = os.path.join("db", "credentials.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(credentials, file, indent=4, ensure_ascii=False)

    # Call stop_script function
    stop_script()

# Single-User-Registration Status-Check
print("Checking if single-user-registration is enabled...")

# Check if Single-User-Registration (SUR) is enabled
if single_user_registration_status == True:
    # If SUR enabled, call register-function
    print("Single-User-Registration is enabled.") 
    print(f"Single-User-Registration Session Token: {single_user_registration_token}")
    register_user()

else:
    # If SUR disabled, notify the user to contact administrator
    print("Single-User-Registration is disabled. Contact the project administrator to enable it.")