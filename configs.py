# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "10471716"))
	API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7026982034:AAHQ_xujlY3BXxrGiEfAdgntWQx3FS0WBYk")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "FileStore_l_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002004959023"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', 'moneykamalo.com')
	SHORTLINK_API = os.environ.get('SHORTLINK_API', '39ce44211c1ea606c4ecf195fb8a2d52444e7c85')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "6883997969"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "botio_devs")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002004959023")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Predator HackerzZ](https://t.me/APPUZ_001) 
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/botio_devs)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Appus](https://t.me/APPUZ_001)
 
 I am Super noob Please Support My Hard Work.
 """


	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

"""
