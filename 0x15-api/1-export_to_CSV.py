#!/usr/bin/python3
"""
This script exports to-do list info for a specified employee ID to CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line arguments
    user_id = sys.argv[1]

    # Base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch employee details from the API and convert the response to JSON
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the employee ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create a CSV file for exporting the to-do list information
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
