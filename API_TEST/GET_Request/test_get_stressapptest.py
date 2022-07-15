import datetime
import random

import psutil
import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("status", [('success', 'failed', 'loading')])
def test_get_stress_apptest(status):
    status = random.choice(status)
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('MANAGE_STRESS_APPTEST')
    data = JsonData.MANAGE_STRESS_APPTEST
    data["cpu"] = psutil.virtual_memory()[2]
    data["time"] = datetime.datetime.now().second
    if status == "success":
        status_code = 200
    elif status == "failed":
        status_code = 400
    elif status == "loading":
        status_code = 102
    else:
        status_code = 500
    with responses.RequestsMock() as reps:
        reps.add(
            responses.GET,
            url + endpoint,
            json=data,
            status=status_code,
            content_type="application/json",
        )
        resp = requests.get(url + endpoint)
        resp_data = resp.json()
        log.info("Getting the data from " + url + endpoint + ". The response json is " + str(resp_data))
        assert resp.status_code == status_code
        log.info("Verified the status code to be " + str(resp.status_code))
