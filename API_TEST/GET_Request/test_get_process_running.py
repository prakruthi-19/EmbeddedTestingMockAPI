import random

import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("status,process_name", [(("running", "terminated"), ("Linux", "Windows"))])
def test_get_process_running(status, process_name):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('GET_PROCESS_RUNNING_ENDPOINT')
    data = JsonData.GET_PROCESS_RUNNING_DATA
    status = random.choice(status)
    process_name = random.choice(process_name)
    data["status"] = status
    data["name"] = process_name
    if status == "running":
        status_code = 200
    else:
        status_code = 400
    with responses.RequestsMock() as reps:
        reps.add(
            responses.GET,
            url + endpoint,
            json=data,
            status=status_code,
            content_type="application/json",
        )
        resp = requests.get(url + endpoint, params={"process_name": process_name})
        resp_data = resp.json()
        log.info("Getting the data from " + url + endpoint + process_name + ". The response json is " + str(resp_data))
        assert resp_data['name'] == process_name
        assert resp.status_code == status_code
        log.info(
            "Verified the name of running process to be "+process_name+" and status code to be " + str(status_code))
