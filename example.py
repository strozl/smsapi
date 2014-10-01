import logging
from smsapi import SmsAPI
from pprint import pprint

logger = logging.getLogger()
formatter = logging.Formatter(
    '%(asctime)s  %(lineno)d:%(filename)s:%(threadName)s:%(funcName)s %(levelname)s %(message)s', "%Y-%m-%d %H:%M:%S")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

SMSAPI_USER = "test"
SMSAPI_PASS = "test"

NUMBER = "38651123456" ## telefonska stevilka v mednarodni obliki

smsapi = SmsAPI(api_user=SMSAPI_USER,
                api_pass=SMSAPI_PASS,
                number=NUMBER,
                msg="Sporocilo za posiljanje",
                _from="SenderID")

response = smsapi.send_request()

if response.get("send_code")==-1:
    logger.error("Error sending sms. Response:%s" % smsapi.body)
pprint(response)