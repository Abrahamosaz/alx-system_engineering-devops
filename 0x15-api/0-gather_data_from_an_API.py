#!/usr/bin/python3
"""Module to get information from a restful api"""


def display_details(user_id=None):
    """display data from the restful api"""
    error = False
    try:
        user_response = requests.get(
                'https://jsonplaceholder.typicode.com/users')
        user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos')
    except Exception as err:
        print(err.args)
        error = True

    if error:
        return
    users = json.loads(user_response.text)
    user_tasks = json.loads(user_tasks.text)
    user_list = [user for user in users if user.get("id") == int(user_id)]
    tasks = completed_tasks = 0
    for user_task in user_tasks:
        if user_task.get("userId") == int(user_id):
            tasks += 1
        if (user_task.get("completed") is True and
                user_task.get("userId") == int(user_id)):
            completed_tasks += 1

    print('Employee %s is done with tasks(%d/%d):' %
          (user_list[0].get("name"), completed_tasks, tasks))
    [print("\t{}".format(user_task.get("title"))) for user_task in user_tasks
        if user_task.get("completed") is True
        and user_task.get("userId") == int(user_id)]


if __name__ == "__main__":
    import json
    import requests
    import sys
    display_details(sys.argv[1])
