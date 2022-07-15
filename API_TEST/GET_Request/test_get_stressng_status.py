import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("status,is_running", [("success", True), ("Failed", False), ("Loading", False)])
def test_stressng_status(status, is_running):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('GET_STRESSNG_STATUS_ENDPOINT')
    data = JsonData.GET_STRESSNG_STATUS
    print(status, is_running)
    data["status"] = status
    data["svc_status"]["is_running"] = is_running
    if status == "success":
        status_code = 200
    elif status == "Failed":
        status_code = 400
    elif status == "Loading":
        status_code = 102
    else:
        status_code = 502
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
        assert resp_data["status"] == status
        assert resp.status_code == status_code
        log.info("Verified the status code to be "+str(status_code)+" and status is "+status)



