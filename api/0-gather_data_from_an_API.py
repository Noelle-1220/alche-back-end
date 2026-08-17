#!/usr/bin/python3
"""Gather data from a REST API for a given employee ID.

This module fetches an employee's TODO list from
https://jsonplaceholder.typicode.com and displays the progress of
that employee's tasks on the standard output.
"""
import requests

import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    """Fetch and display the TODO list progress for an employee.

    Args:
        employee_id (int): the ID of the employee.
    """
    user_url = "{}/users/{}".format(BASE_URL, employee_id)
    todos_url = "{}/todos".format(BASE_URL)

    user_response = requests.get(user_url)
    user = user_response.json()
    employee_name = user.get("name")

    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
    