import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "botname",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)




@Client.on_message(filters.group & filters.forwarded)
async def channeltag(bot, message):
   try:
       chat_id = message.chat.id
       forward_msg = await message.copy(chat_id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
    
