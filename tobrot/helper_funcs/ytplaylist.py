# (c) gautamajay52
# 
# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os
import shutil
import asyncio
import subprocess
import requests
from tobrot.helper_funcs.upload_to_tg import upload_to_tg, upload_to_gdrive
from tobrot import (
    DOWNLOAD_LOCATION
)


async def yt_playlist_downg(message, i_m_sefg):
    url = message.text
    usr = message.from_user.id
    messa_ge = i_m_sefg.reply_to_message
    fol_der = f"{usr}youtube"
    print(url)
    print(usr)
    print(messa_ge)
    print(fol_der)
    try:
        os.mkdir(fol_der)
    except:
        pass
    cmd = ["youtube-dl", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4", "-o", f"{fol_der}/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s", f"{url}"]
    gau_tam = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    gau, tam = await gau_tam.communicate()
    LOGGER.info(gau.decode('utf-8'))
    LOGGER.info(tam.decode('utf-8'))
    if os.path.exists('blame_my_knowledge.txt'):
        get_g = os.listdir(fol_der)
        print(get_g)
        for ga_u in get_g:
            print(ga_u)
            ta_m = os.path.join(fol_der, ga_u)
            print(ta_m)
            shutil.move(ta_m, './')
            await upload_to_gdrive(ga_u, i_m_sefg, messa_ge, usr)
    else:
        final_response = await upload_to_tg(i_m_sefg, fol_der, usr, {})
        print(final_response)
    try:
        shutil.rmtree(fol_der)
    except:
        pass
