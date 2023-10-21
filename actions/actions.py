# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import datetime
from typing import Text, Dict, Any, List

import psycopg2
from psycopg2._psycopg import cursor
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionCreateTask(Action):
    def name(self) -> Text:
        return "create_task"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        task_name = tracker.get_slot("task_name")
        task_name = task_name
        try:
            # пытаемся подключиться к базе данных
            print("Я пытаюсь...")
            conn = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="postgres",
                                    port="5433")
            curs = conn.cursor()
            try:
                query = """INSERT INTO tasks (task_id, title, description, deadline_dt) VALUES (%s, %s, %s, %s);"""
                task_id = 11
                description = ""
                deadline_dt = None
                values = (task_id, task_name, description, deadline_dt)

                curs.execute(query, values)
                conn.commit()
                dispatcher.utter_message(text=f"Задача \"{task_name}\" создана!")
            except Exception as inst:
                print(type(inst))
                print(inst.args)

        except:
            # в случае сбоя подключения будет выведено сообщение в STDOUT
            print('Can`t establish connection to database')

        return []
