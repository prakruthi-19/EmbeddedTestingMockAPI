import datetime
import random

import psutil
import pytest
import requests
import responses
from responses import matchers

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("status", [("Success", "Failed", "Loading")])
def test_set_stressng_config(status):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('SET_STRESSNG_CONFIG')
    data = JsonData.SET_STRESSNG_CONFIG
    data["cpu"] = psutil.virtual_memory()[2]
    data["time"] = datetime.datetime.now().second
    status = random.choice(status)
    if status == "Success":
        status_code = 200
    elif status == "Failed":
        status_code = 400
    elif status == "Loading":
        status_code = 102
    else:
        status_code = 500
    with responses.RequestsMock() as reps:
        reps.add(
            method=responses.POST,
            url=url + endpoint,
            json=data,
            match=[matchers.json_params_matcher(data)],
            status=status_code
        )
        resp = requests.post(
            url + endpoint,
            headers={"Content-Type": "application/json"},
            json=data,
        )
        log.info(
            "Executing post request for the endpoint to set stressng config" + url + endpoint + " with post data " + str(
                data))
        assert resp.status_code == status_code
        log.info("Verified the status code to be " + str(resp.status_code))
