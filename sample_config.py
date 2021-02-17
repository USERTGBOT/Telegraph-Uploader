import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1696923786:AAGJ6Pfg7Lbeagbvv3tDaS-Cv67O4NlTmC8", "")

    APP_ID = int(os.environ.get("2327886", 12345))

    API_HASH = os.environ.get("b27fc6b63c22a6917438a57bc616075c", "")
