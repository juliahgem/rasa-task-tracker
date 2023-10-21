import psycopg2

from service import Repository


def add_task(task_name):
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
