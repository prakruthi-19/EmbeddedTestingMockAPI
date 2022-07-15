import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("status,boot_status", [("Pass", "Success"), ("Fail", "Failed"), ("Loading", "Loading")])
def test_get_boot_status_value(status, boot_status):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('GET_BOOT_STATUS_ENDPOINT')
    data = JsonData.GET_BOOT_STATUS_DATA
    data["boot-status"] = boot_status
    data["status"] = status
    if status == "Pass":
        status_code = 200
    elif status == "Fail":
        status_code = 400
    elif status == "Loading":
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
        log.info("Executing get request for endpoint " + url + endpoint)
        resp_data = resp.json()
        log.info("The response data is " + str(resp_data))
        assert resp_data["status"] == status
        log.info("Verified the status to be " + resp_data["status"])
        assert resp.status_code == status_code
        log.info("Verified the status code to be " + str(resp.status_code))
