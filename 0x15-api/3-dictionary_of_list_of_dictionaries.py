#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API and exports the data to a JSON file.
"""

import json
import requests


def fetch_user_todos(user_id):
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided user ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    return [
        {
            'username': username,
            'task': t.get('title'),
            'completed': t.get('completed')
        }
        for t in todos]


if __name__ == "__main__":
    all_employee_data = {}  # Dictionary to store data for all employees

    # Fetch user information and to-do lists for all employees
    for user_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        all_employee_data[str(user_id)] = fetch_user_todos(user_id)

    # Write all employee data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employee_data, jsonfile, indent=4)
