#!/usr/bin/python3
"""Gather data from a REST API for all employees and export to JSON.

This module fetches all employees and all TODO tasks from
https://jsonplaceholder.typicode.com and exports every employee's
tasks to a single JSON file named todo_all_employees.json.
"""
import json

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def export_all_to_json():
    """Fetch all employees' tasks and export them to a JSON file."""
    users_url = "{}/users".format(BASE_URL)
    todos_url = "{}/todos".format(BASE_URL)

    users_response = requests.get(users_url)
    users = users_response.json()

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        all_tasks[str(user_id)] = tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
