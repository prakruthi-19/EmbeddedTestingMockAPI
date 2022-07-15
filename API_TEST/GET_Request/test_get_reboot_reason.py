import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("reason", ['soft reboot', 'hard reboot', 'random reboot', " "])
def test_get_system_time(reason):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('REBOOT_REASON_ENDPOINT')
    data = JsonData.GET_REBOOT_REASON_DATA
    data['reason'] = reason
    match reason:
        case 'soft reboot':
            status_code = 200
        case 'hard reboot':
            status_code = 500
        case 'random reboot':
            status_code = 401
        case default:
            status_code = 400

    with responses.RequestsMock() as reps:
        reps.add(
            responses.GET,
            url + endpoint,
            json=data,
            status=status_code,
            content_type="application/json",
        )
        resp = requests.get(url + endpoint)
        log.info("Getting the data from " + url + endpoint)
        resp_data = resp.json()
        log.info("The response json is " + str(resp_data))
        assert resp_data['reason'] == reason
        assert resp.status_code == status_code
        log.info("Verified the status code to be " + str(status_code) + " and reason is " + reason)
