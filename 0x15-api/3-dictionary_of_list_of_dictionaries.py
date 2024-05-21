import requests
import json


if __name__ == "__main__":
    # Define the URLs
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch data from the URLs
    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    # Convert response data to JSON
    users = response_users.json()
    todos = response_todos.json()

    # Create a dictionary to store the data
    data = {}

    # Process users and todos
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')

        # Filter todos for the current user
        user_todos = [
                todo for todo in todos if todo.get('userId') == user.get('id')
        ]

        # Structure the tasks
        tasks = [{
            'username': username,
            'task': todo.get('title'),
            'completed': todo.get('completed')
        } for todo in user_todos]

        # Add the tasks to the dictionary under the user_id key
        data[user_id] = tasks

        # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
