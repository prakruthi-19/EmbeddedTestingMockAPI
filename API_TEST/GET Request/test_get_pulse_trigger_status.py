import random

import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


def test_get_pulse_trigger_status():
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('GET_TRIGGER_PULSE_STATUS')
    data = JsonData.GET_TRIGGER_PULSE_TIME_DATA
    sec = random.randint(-1000, 1000)
    nsec = random.randint(-1000, 1000)
    print(sec,nsec)
    data["sec"] = sec
    data["nsec"] = nsec
    if (sec > 0) and (nsec > 0):
        with responses.RequestsMock() as rsps:
            rsps.add(
                responses.GET,
                url=url + endpoint,
                json=data,
                status=200,
                content_type="application/json",
            )
            resp = requests.get(url + endpoint)
            log.info("Getting the data from " + url + endpoint)
            resp_data = resp.json()
            log.info("The response json is " + str(resp_data))
            assert resp.status_code == 200
            log.info("Verified the status code to be " + str(resp.status_code))
    else:
        with responses.RequestsMock() as rsps:
            rsps.add(
                responses.GET,
                url=url + endpoint,
                json=data,
                status=500,
                content_type="application/json",
            )
            resp = requests.get(url + endpoint)
            log.info("Getting the data from " + url + endpoint)
            resp_data = resp.json()
            log.info("The response json is " + str(resp_data))
            assert resp.status_code == 500
            log.info("Error while retrieving the pulse interval")
