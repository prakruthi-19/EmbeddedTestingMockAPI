import random

import requests
import responses
from responses import matchers

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


def test_enable_trigger_pulse_interval():
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('ENABLE_TRIGGER_PULSE_INTERVAL_ENDPOINT')
    frequency = random.randint(0, 100)
    if frequency < 20:
        with responses.RequestsMock() as reps:
            reps.add(
                method=responses.POST,
                url=url + endpoint,
                json=JsonData.POST_ENABLE_PULSE_INTERVAL,
                match=[matchers.json_params_matcher(JsonData.POST_ENABLE_PULSE_INTERVAL)],
                status=201
            )
            resp = requests.post(
                url + endpoint,
                headers={"Content-Type": "application/json"},
                json=JsonData.POST_ENABLE_PULSE_INTERVAL
            )
            log.info("Executing Post request for endpoint "+url+endpoint)
            resp_data = resp.json()
            log.info("Response data is "+str(resp_data))
            assert resp.status_code == 201
            resp_data["message"] = "Pulse trigger Enabled successfully"
            log.info("Verified the status code to be "+str(resp.status_code)+" and the message "+resp_data["message"])

    else:
        with responses.RequestsMock() as reps:
            reps.add(
                method=responses.POST,
                url=url + endpoint,
                json=JsonData.POST_DISABLE_PULSE_INTERVAL,
                match=[matchers.json_params_matcher(JsonData.POST_DISABLE_PULSE_INTERVAL)],
                status=201
            )
            resp = requests.post(
                url + endpoint,
                headers={"Content-Type": "application/json"},
                json=JsonData.POST_DISABLE_PULSE_INTERVAL
            )
            log.info("Executing Post request for endpoint " + url + endpoint)
            resp_data = resp.json()
            log.info("Response data is " + str(resp_data))
            assert resp.status_code == 201
            resp_data["message"] = "Error since the frequency is less than 10Hz"
            log.info("Verified the status code to be "+str(resp.status_code)+" and the message "+resp_data["message"])
