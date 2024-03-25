#!/usr/bin/python3
"""
This script exports to-do list info for a specified employee ID to CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Base URL for the JSON API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch employee details from the API and convert the response to JSON
    employee_id = requests.get(url + "users/{}".format(employee_id)).json()

    # Extract the username from the fetched employee data
    username = employee_data.get("username")

    # Fetch the to-do list items associated with the employee ID
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Create a CSV file for exporting the to-do list information
    with open(f"{employee_id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
