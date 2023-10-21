from datetime import datetime

from service import Repository


def add_task(task_name: str):
    query = """INSERT 
                INTO tasks (title, description, deadline_dt) 
                VALUES ( %s, %s, %s);"""

    description = None
    deadline_dt = None
    values = (task_name, description, deadline_dt)

    try:
        Repository.execute(query, values)

    except Exception as inst:
        print(type(inst))
        print(inst.args)


def update_description(task_id: int, description: str):
    query = """UPDATE tasks SET description=%s WHERE task_id=%s"""
    values = (description, task_id)
    try:
        Repository.execute(query, values)
    except Exception as inst:
        print(type(inst))
        print(inst.args)


def update_deadline_dt(task_id: int, deadline_dt: datetime):
    query = """UPDATE tasks SET deadline_dt=%s WHERE task_id=%s"""
    values = (deadline_dt, task_id)
    Repository.execute(query, values)


def get_all_tasks():
    return Repository.fetch_all_from("tasks")
