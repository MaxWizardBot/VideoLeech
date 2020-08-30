import aiohttp

from tobrot import LOGGER, GP_LINKS_API_KEY, CHANNEL_URL


async def generate_gp_link(message,link,file_name):
    try:
        data = await get_shortlink(link)
        if not data["status"] == "error":
            caption_str = f'\nFile Name: <b>{file_name}</b> ' \
                          f'\n\n <b>=============================</b>' \
                          f'\n\n <center>👉<b>[Direct Download Link]({data["shortenedUrl"]})</b>👈</center>' \
                          f'\n\n <b>=============================</b>'
            caption_str +=f'\n\n 💡 <b>[How to Download?](t.me/MThowtodownload/3)</b> 💡'
            if CHANNEL_URL is not None:
                caption_str += f"\n ⚡ Powered By: <b>[MoviezTrends]({CHANNEL_URL})</b> ⚡"
            await message.reply(caption_str, quote=True,disable_web_page_preview=True)
        else:
            await message.reply(f'Unable to generate GP Link due to FileName. Generate link from [Website](https://gplinks.in)', quote=True,disable_web_page_preview=True)
    except Exception as e:
        await LOGGER.info(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://gplinks.in/api'
    params = {'api': GP_LINKS_API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        LOGGER.info("Calling GP Links API")
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data