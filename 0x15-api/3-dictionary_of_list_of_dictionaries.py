#!/usr/bin/python3
"""Extend your python script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users")
    users = users.json()

    todos = requests.get(url + 'todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
            todoAll[user.get('id')] = taskList

        with open('todo_all_employees.json', mode='w') as f:
            json.dump(todoAll, f)
