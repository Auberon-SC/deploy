# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from zeinzo import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from zeinzo.helpers.misc import git, heroku

MSG_ON = """
🔥 **Personal-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("svmbots")
            await bot.join_chat("zeintod")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ZEINZO").info("Starting Personal-UserBot")
    LOGGER("ZEINZO").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("ZEINZO").info(f"Personal-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    LOOP.run_until_complete(main())
