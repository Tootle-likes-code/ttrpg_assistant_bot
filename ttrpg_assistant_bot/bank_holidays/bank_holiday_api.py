import json
from datetime import datetime

import requests
from requests import HTTPError

UK_API_ENDPOINT = "https://www.gov.uk/bank-holidays.json"


def retrieve_holidays() -> list[datetime]:
    result = requests.get(UK_API_ENDPOINT)

    if result.status_code != 200:
        raise HTTPError(result.text)

    return [datetime.strptime(event['date'], "%Y-%m-%d") for event in result.json()['england-and-wales']['events']]
