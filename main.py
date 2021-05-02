# Made with python3
# (C) @Achubiju
# Copyright permission under MIT License
# All rights reserved by Achu biju


import os
import pyrogram
import asyncio
import time
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

FayasNoushad = Client(
    "Country Info Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """
Hello {}, I am a country information finder bot. Give me a country name I will send the informations of the country.

Made by @Amalbiju154
"""
HELP_TEXT = """
- Just send me a country name
- Then I will check and send you the informations

<b><u>Informations :-</u></b>
Name, Native Name, Capital, Population, Region, Sub Region, Top Level Domains, Calling Codes, Currencies, Residence, Timezone, Wikipedia, Google

Made by @Amalbiju154
"""
ABOUT_TEXT = """
- **Bot :** `Country Info Bot`
- **Creator :** [Achubiju](https://t.me/Amalbiju154)
- **Channel :** [Yᴇᴀɢᴇʀɪsᴛ Bᴏᴛs ](https://t.me/Animemusicarchive6)
- **Yᴇᴀɢᴇʀɪsᴛ Bᴏᴛs Sᴜᴩᴩᴏʀᴛ :** [Click here](https://t.me/Yeageristbots)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://t.me/Animemusicarchive6'),
        InlineKeyboardButton('Group', url='https://t.me/Yeageristbots')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
    country = CountryInfo(update.text)
    info = f"""
Name : `{country.name()}`
Native Name : `{country.native_name()}`
Capital : `{country.capital()}`
Population : `{country.population()}`
Region : `{country.region()}`
Sub Region : `{country.subregion()}`
Top Level Domains : `{country.tld()}`
Calling Codes : `{country.calling_codes()}`
Currencies : `{country.currencies()}`
Residence : `{country.demonym()}`
Timezone : `{country.timezones()}`
"""
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country.name()}')
        ],[
        InlineKeyboardButton('Channel', url='https://t.me/Animemusicarchive6'),
        InlineKeyboardButton('Group', url='https://t.me/Yeageristbots')

        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except FloodWait as floodwait:
        await asyncio.sleep(floodwait.x)
        return countryinfo(bot, update)
    except KeyError as keyerror:
        print(keyerror)
    except Exception as error:
        print(error)

FayasNoushad.run()
