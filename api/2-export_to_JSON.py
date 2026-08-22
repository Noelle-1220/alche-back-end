#!/usr/bin/python3
"""Gather data from a REST API for a given employee ID and export to JSON.

This module fetches an employee's TODO list from
https://jsonplaceholder.typicode.com and exports all of that
employee's tasks to a JSON file named after the employee's ID.
"""
import json
import requests

import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def export_to_json(employee_id):
    """Fetch an employee's tasks and export them to a JSON file.

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

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
