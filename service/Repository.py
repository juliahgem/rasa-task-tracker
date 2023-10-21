import psycopg2


class Database:
    connection = None
    cursor = None


def connect():
    try:
        Database.connection = psycopg2.connect(
            dbname="postgres",
            host="localhost",
            user="postgres",
            password="postgres",
            port="5433"
        )
        Database.cursor = Database.connection.cursor()

    except ConnectionError as inst:
        print(type(inst))
        print(inst.args)


def get_connection():
    return Database.connection


def get_cursor():
    return Database.cursor


def execute(query, values):
    try:
        Database.cursor.execute(query, values)
        Database.connection.commit()
    except Exception as inst:
        print(type(inst))
        print(inst.args)


def fetch_all_from(table: str):
    Database.cursor.execute("""SELECT * FROM "%s";""" % table)
    return Database.cursor.fetchall()
