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

from service.Tasks import add_task, update_description, get_all_tasks, delete_task


class ActionCreateTask(Action):
    def name(self) -> Text:
        return "create_task"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        task_name = tracker.get_slot("task_name")
        if len(task_name) > 0:
            task_name = task_name[0].upper() + task_name[1:]
        try:
            add_task(task_name)
            dispatcher.utter_message(text=f"Задача \"{task_name}\" создана!")
        except Exception as inst:
            dispatcher.utter_message(text=f"Задача не была создана")
            print(type(inst))
            print(inst.args)

        return []


class ActionShowAllTasks(Action):
    def name(self) -> Text:
        return "show_all_tasks"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            tasks = get_all_tasks()
            lst = ""
            for task in tasks:
                lst += str(task[0])+" "+str(task[1])+"\n"
            dispatcher.utter_message(text=lst)
        except Exception as inst:
            print(type(inst))
            print(inst.args)

        return []


class DeleteTask(Action):
    def name(self) -> Text:
        return "delete_task"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            task_id = tracker.get_slot("task_id")
            delete_task(task_id)
            dispatcher.utter_message(text=f"Задача #{task_id} была удалена")
        except Exception as inst:
            dispatcher.utter_message(text=f"Задача #{task_id} не была найдена")
            print(type(inst))
            print(inst.args)

        return []