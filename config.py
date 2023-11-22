from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH","dbc665db1489f9d3cfd8de4a52f1ad4b")
      API_ID = int(getenv("API_ID","23081466"))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6977089742:AAEGv9L50_Xv5PzaKoOdVFo7N4Ux0esEQ50")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
