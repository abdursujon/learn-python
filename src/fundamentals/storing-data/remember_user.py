from pathlib import Path
import json

def get_stored_user_name(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_user_name(path):
    username = input("Enter you name: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('../../../data/json/user_name.json')
    username = get_stored_user_name(path)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_user_name(path)
        print(f"We will remember you. Thanks for visiting {username}!")

greet_user()