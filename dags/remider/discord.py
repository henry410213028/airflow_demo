import requests
from airflow.models import Variable

def send_msg(content: str) -> None:
    url = Variable.get("remider_webhook_url")
    if url:
        requests.post(url, json={"content": content})
