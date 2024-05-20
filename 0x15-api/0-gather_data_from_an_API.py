#!/usr/bin/python3
""" For an employee ID, returns information about the TODO list progress. """
import json
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            sys.argv[1])
    dicti = json.loads(response.text)
    name = dicti.get('name')
    response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + sys.argv[1])
    todos = json.loads(response.text)
    tasks = len(todos)
    completed = [task for task in todos if task.get('completed')]
    done = len(completed)
    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))
    for task in completed:
        print("\t", task.get('title'))
