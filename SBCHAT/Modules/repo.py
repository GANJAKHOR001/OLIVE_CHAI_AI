from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ChatBot import app

@app.on_message(filters.command("repo"))
async def start(_, msg):
    await msg.reply_photo(
        photo="https://files.catbox.moe/extt9m.jpg",
        caption="""Hey there, I'm Tamanna ♥︎

If you want my bot repo, click below to get the source code.

Powered by @II_SB_SIMPLE_II ✨""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/II_SB_SIMPLE_II"),
             InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/powerfulboys123/powerfulboys123/blob/main/README.md")]
        ])
    )