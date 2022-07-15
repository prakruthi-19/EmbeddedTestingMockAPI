import pytest
import requests
import responses

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("register", (0x01, "0x01", " ", -0x01,))
def test_get_imx_register(register):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('READ_IMX_REGISTER_VALUE_ENDPOINT')
    data = JsonData.READ_IMX_REGISTER_VALUE_DATA
    status = "Success"
    data["Register id"] = register
    if type(register) == str or register == " " or register < 1:
        status_code = 400
        status = "Failed"
        data["status"] = status
    else:
        status_code = 200

    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            url=url + endpoint,
            json=data,
            status=status_code,
            content_type="application/json",
        )
        resp = requests.get(url + endpoint)
        resp_data = resp.json()
        log.info("Getting the data from "+url+endpoint+". The response json is "+str(resp_data))
        assert resp.status_code == status_code
        assert resp_data["status"] == status
        log.info("Verified the status code to be "+str(status_code)+" and status is "+status)
