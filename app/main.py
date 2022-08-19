import os

from flask import Flask, jsonify, request
from app.whatsapp_client import WhatsAppWrapper

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get('WHATSAPP_HOOK_TOKEN')


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/send_template_message/", methods=["POST"])
def send_template_message():
    """_summary_: Send a message with a template to a phone number"""

    if "language_code" not in request.json:
        return jsonify({"error": "Missing language_code"}), 400

    if "phone_number" not in request.json:
        return jsonify({"error": "Missing phone_number"}), 400

    if "template_name" not in request.json:
        return jsonify({"error": "Missing template_name"}), 400

    client = WhatsAppWrapper()

    response = client.send_template_message(
        template_name=request.json["template_name"],
        language_code=request.json["language_code"],
        phone_number=request.json["phone_number"],
    )

    return jsonify(
        {
            "data": response,
            "status": "success",
        },
    ), 200