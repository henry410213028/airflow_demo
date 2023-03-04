import requests
from typing import List

def list_events(start_date: str, end_date: str, **kwargs) -> List[str]:
    """API doc
    https://www.travel.taipei/open-api/swagger/ui/index#/Events/Events_Activity
    """
    url = (
        "https://www.travel.taipei/open-api/zh-tw/Events/Activity?"
        f"begin={start_date}&end={end_date}&page=1"
    )
    response = requests.get(url, headers={"accept": "application/json"})
    data = response.json().get("data")
    if data:
        return [
            item["title"] for item in data
        ]


def main(**kwargs):
    for event in list_events(**kwargs):
        print(event)
