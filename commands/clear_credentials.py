# Module Imports
import json
import os
import sys
import subprocess
import time

# Global Variables
username = None
file_path_credentials = os.path.join("db", "credentials.json")
vote = None

# Get Username from credentials.json
with open(file_path_credentials, "r", encoding="utf-8") as file:
    data = json.load(file)

username = data["username"]

# Functions
def stop_script():
    print("Stopping this script and executing the welcome screen")
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the Command-Line-Interface
    subprocess.run([sys.executable, "welcome.py"]) # Execute another script
    sys.exit()

def command():
    # Create a JSON-Dictionary for credentials.json
    credentials = {
        "single_user_registration_status": None,
        "single_user_registration_token": None,
        "email": None,
        "username": None,
        "password": None
    }

    # Write the JSON-File credentials.json
    global file_path_credentials

    with open(file_path_credentials, "w", encoding="utf-8") as file:
        json.dump(credentials, file, indent=4, ensure_ascii=False)

    print("Credentials cleared successfully.")

    def vote_return_q():
        vote_return = input("Do you want to register a new account? Y=Yes, N=No: ")
        
        if vote_return == "Y" or vote_return == "y":
            subprocess.run([sys.executable, "register.py"])
            sys.exit()
        elif vote_return == "N" or vote_return == "n":
            sys.exit()
        else:
            print("Please type (Y) to register a new account or (N) to cancel.")
            time.sleep(2)
            vote_return_q()

    vote_return_q()

print(f"Are you sure about clearing your credentials, {username}? You will need to register again.")
vote = input(f"(Y) = Continue, (N) = No\n")

if vote == "Y" or vote == "y":
    command()
elif vote == "N" or vote == "n":
    stop_script()
else:
    print("Please enter (Y) to continue or (N) to return.")