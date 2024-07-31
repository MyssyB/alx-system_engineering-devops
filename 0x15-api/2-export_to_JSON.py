#!/usr/bin/python3
"""Extend python script to export data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    USER_ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(USER_ID)).json()
    USERNAME = user.get("username")

   i todos = requests.get(url + "todos", params={"userId": USER_ID}).json()
    tasks = [{
        "task": task.get('title'),
        "completed": task.get('completed'),
        "username": USERNAME
        } for task in todos]

    data = {USER_ID: tasks}

    with open("{}.json".format(USER_ID), "w") as jsonfile:
        json.dump(data, jsonfile)
