from cmath import log
import logging
import os
import requests

import json


class WhatsAppWrapper:

    API_URL = "https://graph.facebook.com/v13.0/"
    API_TOKEN = os.environ.get("WHATSAPP_API_TOKEN")
    NUMBER_ID = os.environ.get("WHATSAPP_NUMBER_ID")

    def __init__(self):
        self.headers = {
            #"Authorization": f"Bearer {self.API_TOKEN}",
            "Authorization": "Bearer EAAPZC3q7dV18BABtENvY2NQzxtwcwiGe5T2GYOpLO92tNuZBwUqMsI8Ltp6JtwVSZCajj9J0FgT3GtO8JTT1H8C9pEnAEVTGW0eEEMrdAFEqldd8BYP9AFI53eX564Tv0t8ZCjLRZAPYeME76cg7fDbCCYO3FXdfem51D2RY3BpcZB17DvecIirsmn72SgG8B28bsmeQrVd3WXGjElmZAhw",
            "Content-Type": "application/json",
        }
        self.API_URL = str(self.API_URL) + str(self.NUMBER_ID)

    def send_template_message(self, template_name, language_code, phone_number):

        payload = json.dumps({
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        })

        #logging.debug('msg');

        #f"{self.API_URL}/messages"

        response = requests.request("POST", "https://graph.facebook.com/v13.0/105769248921601/messages", headers=self.headers, data=payload)
        #response = requests.request("POST", str(self.API_URL) + str(self.NUMBER_ID), headers=self.headers, data=payload)

        assert response.status_code == 200, {response.status_code}

        return response.status_code