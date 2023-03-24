#!/usr/bin/python3
"""Module for fetching data from a restful api"""


def display_details(user_id=None):

    try:
        user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos').json()
        response = requests.get(
                'https://jsonplaceholder.typicode.com/users')
        username = response.json()[int(user_id) - 1]['username']
    except Exception as err:
        print(err.args)

    json_dict = {}
    users_list = []
    json_dict[user_id] = users_list
    for user in user_tasks:
        if user['userId'] == int(user_id):
            json_dict[user_id].append({
                "task": user['title'],
                "completed": user['completed'],
                "username": username})

    filename = user_id + '.json'
    with open(file=filename, mode='w', encoding='utf-8') as file:
        json.dump(json_dict, file)


if __name__ == "__main__":
    import json
    import requests
    import sys
    display_details(sys.argv[1])
