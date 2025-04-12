#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7838891589:AAHWB56mT4iy1l6aUOoRh8wGNK9Oy9WMNSI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28638866"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a748074bea1e6ace57394aceb194d292")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002250340602"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7795004397"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nithish7uy:EU4G8ws46ZQr17tF@cluster0.glvel.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002457868984"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", True)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://graph.org/file/3ad8048ca8b06afe3648f-cf2818473b939ac450.jpg")
START_MSG = os.environ.get("START_MESSAGE", "нєℓℓo {first}\n\n👋🏻 ɪᴛ's ᴘʀɪᴠᴀᴛᴇ 😅 ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ 🦅 ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs 📺 ɪɴ sᴘᴇᴄɪғɪᴇᴅ 🦄 ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs 🫧 ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ 😎 sᴘᴇᴄɪᴀʟ ʟɪɴᴋ🪄.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6969391120").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "нєℓℓo {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "60"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5906206984)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
