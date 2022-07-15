GET_SOFTWARE_VERSION_DATA = {'status': 'success', 'versions': {'name': 'cruise 0.9', 'version': '0.9'}}
GET_HARDWARE_VERSION_DATA = {"status": "success", "board": "CruiseBoardName", "revision": "1.1"}
HUMIDITY_AND_TEMPERATURE_DATA = [{"device_name": "device_relative_humidity", "readings": [7.7],
                                  "unit": "Relative Humidity (Percentage)"},
                                 {"device_name": "device_temperature", "readings": [55.799], "unit": "Celsius"}]
SYSTEM_TIME_DATA = {"Region": "US/Alaska", "datetime": "current_time", "timezone": "AKDT"}
SET_IMX_REGISTER_VALUE_DATA = {"Status": "Success", "register_details": {"register": 0x01, "register_value": 100}}
READ_IMX_REGISTER_VALUE_DATA = {'status': 'Success', 'Register id': 0x01}
GET_REBOOT_REASON_DATA = {'reason': 'boot reason'}
GET_BOOT_STATUS_DATA = {"boot-status": "success", "status": "fail"}
GET_PROCESS_RUNNING_DATA = {'name': 'DiskUnmountWatcher', 'status': 'running', 'pid': 95617}
GET_STRESSNG_STATUS = {"status": "success", "svc_status": {"argument_string": "", "is_running": False}}
POST_ENABLE_PULSE_INTERVAL = {"enable": 1}
POST_DISABLE_PULSE_INTERVAL = {"disable": 1}
MANAGE_STRESS_APPTEST = {"cpu": 6, "io": 4, "hdd": 2, "vm": 2, "vm-bytes": 256, "time": 120,
                         "temp-path": "c://users/files",
                         "backoff": 10,
                         "persist": True,
                         "enable": False}
SET_STRESSNG_CONFIG = {"cpu": 6, "io": 4, "hdd": 2, "vm": 2, "vm-bytes": 256, "time": 120,
                       "temp-path": "c://users/files",
                       "backoff": 10,
                       "persist": True,
                       "enable": False
                       }
SET_TRIGGER_PULSE_TIME_DATA = {"sec":1234, "nsec":3455}
SET_TRIGGER_PULSE_INTERVAL_DATA = {"sec":1234, "nsec":3455}
GET_TRIGGER_PULSE_TIME_DATA = {"sec":1234, "nsec":3455}