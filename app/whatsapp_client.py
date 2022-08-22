import os
import requests
import logging
import json
import logging
from dotenv import load_dotenv
load_dotenv()

class WhatsAppWrapper:

    API_URL = "https://graph.facebook.com/v13.0/"
    API_TOKEN = os.getenv('WHATSAPP_API_TOKEN')
    NUMBER_ID = os.environ.get('WHATSAPP_NUMBER_ID')

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}",
            "Content-Type": "application/json",
        }
        self.API_URL = self.API_URL + str(self.NUMBER_ID)

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

        # Setting log file
        logging.basicConfig(filename="log.txt", level=logging.DEBUG)
        #logging.info(self.API_URL + "/messages")
        #logging.info(self.API_TOKEN)  

        response = requests.request("POST", f"{self.API_URL}/messages", headers=self.headers, data=payload)
        
        assert response.status_code == 200, {response.status_code}

        return response.status_code