#!/usr/bin/python3
"""module for reading data from restful api and writing to a csv file"""


def display_details(user_id=None):
    """display details from the restful api"""

    try:
        user_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
        users = requests.get('https://jsonplaceholder.typicode.com/users')
    except Exception as err:
        print(err.args)

    user_tasks_json = json.loads(user_tasks.text)
    users_json = json.loads(users.text)
    user_id_tasks = []
    for user_task in user_tasks_json:
        if user_task['userId'] == int(user_id):
            user_id_tasks.append(user_task)

    try:
        filename = user_id + '.csv'
        with open(file=filename, mode='w',
                  encoding='utf-8',  newline='') as csv_file:
            fieldnames = ['userId', 'username', 'completed', 'title']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            for user_task in user_id_tasks:
                user_task['username'] = users_json[1]['username']
                del user_task['id']
                csv_writer.writerow(user_task)
    except Exception as err:
        print(err.args)


if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys
    display_details(sys.argv[1])
