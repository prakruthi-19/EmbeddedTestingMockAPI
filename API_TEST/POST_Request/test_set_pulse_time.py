import random

import pytest
import requests
import responses
from responses import matchers

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("sec, nsec", [(1234, 1234), (2345, 2345)])
def test_set_pulse_time(sec, nsec):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('SET_TRIGGER_PULSE_TIME')
    data = JsonData.SET_TRIGGER_PULSE_TIME_DATA
    data["sec"] = sec
    data["nsec"] = nsec
    pulse_time = [2, 3, 5, 6, 7, 8]
    ptime = random.choice(pulse_time)
    with responses.RequestsMock() as reps:
        reps.add(
            method=responses.POST,
            url=url + endpoint,
            json=data,
            match=[matchers.json_params_matcher(data)],
            status=200,
        )
        resp = requests.post(
            url + endpoint,
            headers={"Content-Type": "application/json"},
            json=data,
        )
        log.info("Executing the post request for the endpoint " + url + endpoint)
        data_resp = resp.json()
        assert data_resp["sec"] == sec
        assert data_resp["nsec"] == nsec
        log.info("Verified the seconds and nanoseconds to be " + str(sec) + str(nsec))
        if data_resp["sec"] == sec and data_resp["nsec"] == nsec:
            data_resp["pulse_time"] = ptime
            log.info("Setting the pulse time as " + str(ptime))
        else:
            data_resp["pulse_time"] = 'Null'
