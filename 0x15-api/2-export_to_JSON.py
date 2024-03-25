#!/usr/bin/python3
"""
Exports to-do list information for a specified employee ID to JSON format.

Exports user info and to-do list corresponding to an employee ID to JSON file
"""

import json
import requests
import sys


def fetch_user_todos(user_id):
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided user ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the user ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }


if __name__ == "__main__":
    user_id = sys.argv[1]  # Extract the user ID from command-line arguments

    user_data = fetch_user_todos(user_id)  # Fetch to-do list for specific user

    # Write the user's to-do list data to a JSON file named with the user ID
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(user_data, jsonfile, indent=4)
