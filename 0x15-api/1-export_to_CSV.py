#!/usr/bin/env bash
"""Extend python script to export data in the csv format"""

import csv
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(USER_ID)).json()
    USERNAME = user.get("USERNAME")
    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows([
            [USER_ID, USERNAME, t.get("completed"), t.get("title")]
            for t in todos])
