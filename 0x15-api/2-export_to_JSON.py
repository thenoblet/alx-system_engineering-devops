#!/usr/bin/python3
""" Export data in the CSV format.. """
import json
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            sys.argv[1])
    dicti = json.loads(response.text)
    username = dicti.get('username')
    response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + sys.argv[1])
    todos = json.loads(response.text)
    tasks = [task for task in todos]
    ans = {sys.argv[1]: []}
    for task in tasks:
        task_dict = {"task": task.get('title'),
                     'completed': task.get('completed'), 'username': username}
        ans.get(sys.argv[1]).append(task_dict)
    with open(sys.argv[1] + ".json", "w") as f:
        json.dump(ans, f)
