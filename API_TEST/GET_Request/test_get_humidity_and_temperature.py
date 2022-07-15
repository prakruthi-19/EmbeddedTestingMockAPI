import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


def test_humidity_and_temp():
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('HUMIDITY_AND_TEMP_ENDPOINT')
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            url + endpoint,
            json=JsonData.HUMIDITY_AND_TEMPERATURE_DATA,
            status=200,
            content_type="application/json",
        )
        resp = requests.get(url + endpoint)
        log.info("Executing get request for endpoint " + url + endpoint)
        if float(resp.elapsed.total_seconds()) < 0.1:
            status = "PASS"
        else:
            status = "FAIL"

        if status == "PASS":
            assert resp.status_code == 200
        else:
            assert resp.status_code == 400
        log.info("Verified the status code to be " + str(resp.status_code) + " and status to be " + status)
