# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "20053544"))
    API_HASH = os.environ.get("API_HASH", "f26c4d28081c11e0c48707143f7bb5b1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6534036538:AAFlLurKj-OB1H0RTnNzcsjhvAZcoeVCYmw")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "1439022100"))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://MovieTimeHD1:MovieTimeHD1@cluster0.trfqzij.mongodb.net/")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001870034903"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
