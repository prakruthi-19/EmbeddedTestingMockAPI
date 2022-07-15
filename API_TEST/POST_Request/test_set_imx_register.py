import pytest
import requests
import responses
from responses import matchers

from Config import configParser
from Json import JsonData
from Log import Logger

log = Logger.getlogger()


@pytest.mark.parametrize("register,register_value", [(0x01, 100), (0x02, 200), (0x03, 300)])
def test_set_imx_register(register, register_value):
    url = configParser.getConfig('url')
    endpoint = configParser.getConfig('SET_IMX_REGISTER_ENDPOINT')
    data = JsonData.SET_IMX_REGISTER_VALUE_DATA
    data["register_details"]["register"] = register
    data["register_details"]["register_value"] = register_value
    print(register, register_value)
    with responses.RequestsMock() as reps:
        reps.add(
            method=responses.POST,
            url=url + endpoint,
            json=data,
            match=[matchers.json_params_matcher(data)],
            status=201
        )
        resp = requests.post(
            url + endpoint,
            headers={"Content-Type": "application/json"},
            json=data,
        )
        log.info("Executing post request for the endpoint " + url + endpoint + " with post data " + str(data))
        resp_data = resp.json()
        assert resp.status_code == 201
        assert resp_data["Status"] == "Success"
        assert resp_data["register_details"]["register"] == register
        assert resp_data["register_details"]["register_value"] == register_value
        log.info("Verified the response register_details and status to be " + resp_data["Status"]+" with status code "+str(resp.status_code))
