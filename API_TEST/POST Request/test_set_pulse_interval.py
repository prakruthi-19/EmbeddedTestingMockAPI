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
def test_set_pulse_interval(sec, nsec):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('SET_TRIGGER_PULSE_INTERVAL')
    data = JsonData.SET_TRIGGER_PULSE_INTERVAL_DATA
    data["sec"] = sec
    data["nsec"] = nsec
    pulse_interval = ["0-10", "10-15", "30-37", "23-25"]
    pinterval = random.choice(pulse_interval)
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
            data_resp["pulse_time"] = pinterval
            log.info("Setting the pulse interval as " + pinterval)
        else:
            data_resp["pulse_time"] = 'Null'
