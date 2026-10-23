import os
import json
import subprocess
import sys
import time

# Check User Registration
file_path_credentials = os.path.join("db", "credentials.json")

def unregistered_user():
    global file_path_credentials

    # Read credentials.json
    with open(file_path_credentials, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Get Data from credentials.json
    single_user_registration_status = data.get("single_user_registration_status")
    single_user_registration_token = data.get("single_user_registration_token")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    os.system('cls' if os.name == 'nt' else 'clear') # Clear the Command-Line-Interface
    print("Hello, User. It seems like you are not registered or an error happened while the registration was completed.")
    print("Your credentials are all 'None' or 'null'. Please check the credentials and register again:")
    print(f"single_user_registration_status: {single_user_registration_status}")
    print(f"single_user_registration_token: {single_user_registration_token}")
    print(f"email: {email}")
    print(f"username: {username}")
    print(f"password: {password}")

    vote_return_register = input("\nDo you want to register? Y=Yes, N=No: ")
    if vote_return_register == "Y":
        subprocess.run([sys.executable, "register.py"])
        sys.exit()
    elif vote_return_register == "N":
        sys.exit()
    else:
        print("Please type (Y) to register or (N) to cancel.")
        time.sleep(2)
        unregistered_user()

# Global Variables
username = None
cmd_input = None

# Get Username from credentials.json
with open(file_path_credentials, "r", encoding="utf-8") as file:
    data = json.load(file)

username = data["username"]

# Command Input

def command_input():
    global cmd_input

    cmd_input = input(">>> ")

def home_screen():
    global username
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the Command-Line-Interface
    
    # Ascii-Banner
    ascii_banner = r"""
  _____ _ _              _            _____ _      _____ 
 |  __ (_) |            | |          / ____| |    |_   _|
 | |__) || | ____ _  ___| |__  _   _| |    | |      | |  
 |  ___/ | |/ / _` |/ __| '_ \| | | | |    | |      | |  
 | |   | |   < (_| | (__| | | | |_| | |____| |____ _| |_ 
 |_|   |_|_|\_\__,_|\___|_| |_|\__,_|\_____|______|_____|
                                                         
                                                         
    """
    global username, cmd_input
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii_banner) 
    print(f"Welcome, {username}!")
    print("Execute 'help' to view all available commands.")

    cmd_input = input(">>> ")

    if cmd_input == "help":
        file_path_help = os.path.join("commands", "help.py")
        subprocess.run([sys.executable, file_path_help])
        sys.exit()
    elif cmd_input == "clear_credentials":
        file_path_clearcredentials = os.path.join("commands", "clear_credentials.py")
        subprocess.run([sys.executable, file_path_clearcredentials])
        sys.exit()


with open(file_path_credentials, "r", encoding="utf-8") as file:
    data = json.load(file)

if (
    data.get("email") is None or 
    data.get("username") is None or 
    data.get("password") is None or 
    data.get("single_user_registration_token") is None or 
    data.get("single_user_registration_status") is None
):
    unregistered_user()
else:
    home_screen()