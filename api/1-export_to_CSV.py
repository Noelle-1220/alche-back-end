#!/usr/bin/python3
"""Gather data from a REST API for a given employee ID and export to CSV.

This module fetches an employee's TODO list from
https://jsonplaceholder.typicode.com and exports all of that
employee's tasks to a CSV file named after the employee's ID.
"""
import csv
import requests

import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def export_to_csv(employee_id):
    """Fetch an employee's tasks and export them to a CSV file.

    Args:
        employee_id (int): the ID of the employee.
    """
    user_url = "{}/users/{}".format(BASE_URL, employee_id)
    todos_url = "{}/todos".format(BASE_URL)

    user_response = requests.get(user_url)
    user = user_response.json()
    username = user.get("username")

    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
    