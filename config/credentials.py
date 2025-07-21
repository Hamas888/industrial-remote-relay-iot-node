# config/credentials.py

import os
from dotenv import load_dotenv

load_dotenv("variables.env")  # load variables from .env file

AWS_ACCESS_KEY_ID       = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY   = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION              = os.environ.get('AWS_REGION')
AWS_BUCKET_NAME         = os.environ.get('AWS_BUCKET_NAME')

AWS_ENDPOINT            = "*******************************.amazonaws.com"
MQTT_PORT               = 8883
MQTT_TOPICS             = {
    "publish": "*******/Uplink/",
    "subscribe": "*******/Downlink/",
    "streamUP": "*******/StreamUP/",
    "streamDOWN": "*******/StreamDOWN/"
}

ROOT_CA                 = "credentials/root_ca.pem"
CLIENT_CERT             = "credentials/client_cert.pem"
PRIVATE_KEY             = "credentials/private_key.pem"
