#!/usr/bin/python3
"""
Exports to-do list information for a specified employee ID to JSON format.

Exports user info and to-do list corresponding to an employee ID to JSON file
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Extract the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information for the specified employee ID
    user_data = requests.get(base_url + "users/{}".format(employee_id)).json()
    username = user_data.get("username")

    # Fetch the to-do list associated with the employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Prepare a dictionary to store user and to-do list information
    data_to_export = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos_data
        ]
    }

    # Export the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(data_to_export, json_file, indent=4)
