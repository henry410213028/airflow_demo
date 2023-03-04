from travel import udf as travel_udf
from remider import discord, utils

def fetch_travel_events(**kwargs):
    events = travel_udf.list_events(**kwargs)

    dag_id = kwargs["dag_run"].run_id
    task_instance = kwargs["ti"]
    obj_path = utils.write_data(events, dag_id, "events")

    task_instance.xcom_push(key="events", value=obj_path)


def send_activity_msg(**kwargs):
    task_instance = kwargs["ti"]
    obj_path = task_instance.xcom_pull(key="events")
    events = utils.read_data(obj_path)

    content = "\n".join(events)
    discord.send_msg(content)


def clean_up(**kwargs):
    task_instance = kwargs["ti"]
    obj_path = task_instance.xcom_pull(key="events")
    utils.remove_data(obj_path)
