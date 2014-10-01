import phonenumbers
import requests
import string
import logging

logger = logging.getLogger(__name__)


class SmsAPI():
    def __init__(self, api_user, api_pass, number, msg, _from,
                 url="http://www.easysmsapi.si/poslji-sms/"):
        self.params = dict()

        self.number = number
        self.response = None
        self.params["un"] = api_user,

        self.params["ps"] = str(api_pass),
        self.params["from"] = str(_from),
        self.params["to"] = self._get_to()
        self.params["cc"] = self._get_cc()

        self.params["dr"] = "1"
        self.params["m"] = msg
        self.body = None
        print(type(_from))
        if isinstance(_from, str) or isinstance(_from, unicode):
            self.params["sid"] = 1
            self.params["sname"] = str(_from)
        else:
            self.params["sid"] = 0
        self.url = url

    def _get_to(self):
        x = phonenumbers.parse("+" + self.number, None)
        return "0%s" % x.national_number

    def _get_cc(self):
        x = phonenumbers.parse("+" + self.number, None)
        return str(x.country_code)

    def parse_response(self):
        self.body = self.response.text.strip()
        ff = self.body.split("##")
        result = dict()
        result["id"] = int(ff[0])
        if result["id"] == -1:
            result["send_code"] = result["id"]
        else:
            #ok
            result["send_code"] = 0
            result["cost"] = ff[1]
            result["from"] = ff[2]
            result["to"] = ff[3]
            result["id"] = result["id"]
        return result

    def send_request(self):

        self.response = requests.get(self.url, params=self.params)
        return self.parse_response()