#!/usr/bin/python3
"""Module to get information from a restful api"""


def display_details(user_id=None):
    """display data from the restful api"""
    try:
        user_response = requests.get(
                'https://jsonplaceholder.typicode.com/users')
        user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos')
    except Exception as err:
        print(err.args)

    user_list = json.loads(user_response.text)
    user_task_list = json.loads(user_tasks.text)
    for user in user_list:
        if user['id'] == int(user_id):
            needed_user = user
            break

    tasks = completed_tasks = 0
    for user_task in user_task_list:
        if user_task['userId'] == int(user_id):
            tasks += 1
        if (user_task['completed'] is True and
                user_task['userId'] == int(user_id)):
            completed_tasks += 1

    print('Employee %s is done with tasks(%d/%d):' %
          (needed_user['name'], completed_tasks, tasks))

    for user_task in user_task_list:
        if (user_task['completed'] is True and
                user_task['userId'] == int(user_id)):
            print('\t{}'.format(user_task['title']))


if __name__ == "__main__":
    import json
    import requests
    import sys
    display_details(sys.argv[1])
