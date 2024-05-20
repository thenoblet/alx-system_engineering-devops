
#!/usr/bin/python3
""" Export data in the JSON format. """
import json
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    dicti = json.loads(response.text)
    ans = {}
    for user in dicti:
        username = user.get('username')
        userId = str(user.get('id'))
        response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                                "?userId=" + userId)
        todos = json.loads(response.text)
        tasks = [task for task in todos]
        ans[userId] = []
        for task in tasks:
            task_dict = {"task": task.get('title'),
                         'completed': task.get('completed'),
                         'username': username}
            ans.get(userId).append(task_dict)
    with open("todo_all_employees.json", "w") as f:
        json.dump(ans, f)

