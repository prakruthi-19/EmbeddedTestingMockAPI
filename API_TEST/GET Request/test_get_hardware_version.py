import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("status", ['success', 'failed', 'loading'])
def test_get_hardware_version(status):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('GET_HARDWARE_VERSION_ENDPOINT')
    if status == "success":
        with responses.RequestsMock() as reps:
            reps.add(
                responses.GET,
                url + endpoint,
                json=JsonData.GET_HARDWARE_VERSION_DATA,
                status=200,
                content_type="application/json",
            )
            resp = requests.get(url + endpoint)
            log.info("Executing get request for endpoint " + url + endpoint)
            data = resp.json()
            log.info("The response data is " + str(data))
            assert data["revision"] == "1.1"
            assert data["board"] == "CruiseBoardName"
            assert resp.status_code == 200
            log.info(
                "Verified the board name to be " + data["board"] + " and status code to be " + str(resp.status_code))

    elif status == "failed":
        with responses.RequestsMock() as reps:
            reps.add(
                responses.GET,
                url + endpoint,
                json=JsonData.GET_HARDWARE_VERSION_DATA,
                status=400,
                content_type="application/json",
            )
            resp = requests.get(url + endpoint)
            log.info("Executing get request for endpoint " + url + endpoint)
            data = resp.json()
            log.info("The response data is " + str(data))
            assert data["revision"] == "1.1"
            assert data["board"] == "CruiseBoardName"
            assert resp.status_code == 400
            log.info("Verified the board name to be " + data["board"] + " and status code to be " + str(resp.status_code))

    elif status == "loading":
        with responses.RequestsMock() as reps:
            reps.add(
                responses.GET,
                url + endpoint,
                json=JsonData.GET_HARDWARE_VERSION_DATA,
                status=102,
                content_type="application/json",
            )
            resp = requests.get(url + endpoint)
            log.info("Executing get request for endpoint " + url + endpoint)
            data = resp.json()
            log.info("The response data is " + str(data))
            assert data["revision"] == "1.1"
            assert data["board"] == "CruiseBoardName"
            assert resp.status_code == 102
            log.info("Verified the board name to be " + data["board"] + " and status code to be " + str(resp.status_code))
