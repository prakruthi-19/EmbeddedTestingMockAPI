from datetime import datetime

import pytz
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


def test_get_system_time():
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('SYSTEM_TIME_ENDPOINT')
    tz_time = pytz.timezone('US/Alaska')
    datetime_ny = datetime.now(tz_time)
    current_time = datetime_ny.strftime("%Y-%m-%d %I:%M:%S:%p %z")
    data = JsonData.SYSTEM_TIME_DATA
    data["datetime"] = current_time
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            url=url + endpoint,
            json=data,
            status=200,
            content_type="application/json",
        )
        resp = requests.get(url + endpoint)
        log.info("Executing get request using endpoint " + url + endpoint)
        data = resp.json()
        log.info("The response data is " + str(data))
        assert resp.status_code == 200
        log.info("Verified the status code to be " + str(resp.status_code))
        assert data["datetime"] == current_time
        log.info("Verified the datetime " + data["datetime"] + " with current time")
