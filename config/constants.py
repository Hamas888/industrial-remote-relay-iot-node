CONFIG_FILE         = "./config/settings.json"
GSM_BAUDRATE        = 115200
GSM_SERIAL_PORT     = "/dev/serial0"
FIRMWARE_VERSION    = "1.0.0"

GSM_PIN             = 4

RELAY_PINS          = {
    1: 23,
    2: 24
}

EXTERNAL_RELAY_PINS = {
    1: 22,
    2: 27
}

DEFAULT_SETTINGS = {
    "apn":              "***Network_APN***",
    "Peer":             "***PPP_Peer***",
    "port":             GSM_SERIAL_PORT,
    "baudrate":         GSM_BAUDRATE,
    "user":             "",
    "password":         "",
    "deviceIMEI":       "Not Configured",
    "deviceLogs":       "No errors",
    "deviceError":      "None",
    "deviceBattery":    100,
    "defaultSettings":  True,
    "firmwareVersion":  FIRMWARE_VERSION,
    "relays":           {1: True, 2: True},
    "extRelays":        {1: False, 2: False},
    "eventFlag":        False,
    "updateFlag":       False,
    "networkStatus":    0,
    "executionTime":    0,
    "gpsLatitude":      0,
    "gpsLongitude":     0,
    "fixLatitude":      0,
    "fixLongitude":     0,
    "geoFanceRadius":   150,
    "geoFanceFlag":     False,
    "alertPhoneNumber": "Not Configured",
    "alertFlag":        False,
    "alert":            "None",
    "motionFlag":       False
}