#!/usr/bin/python3
"""script to get all user data"""


def get_data():
    """function to get all user data"""
    datas = {}
    error = False

    try:
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        user_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    except Exception as err:
        print(err.args)
        error = True

    if error:
        return
    json_users = json.loads(users.text)
    json_user_task = json.loads(user_tasks.text)

    for user in json_users:
        c = "{}".format(user.get("id"))
        datas[c] = []
        for user_task in json_user_task:
            if user_task.get("userId") == user.get("id"):
                datas[c].append({
                    "username": user.get("username"),
                    "task": user_task.get("title"),
                    "completed": user_task.get("completed")})

    with open(file="todo_all_employees.json", mode="w",
              encoding="utf-8") as file:
        json.dump(datas, file)


if __name__ == "__main__":
    import json
    import requests
    get_data()
