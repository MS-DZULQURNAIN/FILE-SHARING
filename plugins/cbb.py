#(©)Codexbotz
#Reedit by MS DZULQURNAIN

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ FILE SHARING BOT TELEGRAM 1 BUTTON\n○ Pemilik : <a href='tg://user?id={OWNER_ID}'>Saya</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Repo : <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING'>by MS-DZULQURNAIN</a>\n○ Channel : @MS_DZULQURNAIN_NET\n○ Beli/bongkar chip hdi terpercaya: @ZULLL_CHIP</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Tutup", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
