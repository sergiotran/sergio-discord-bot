import json
from discord.ext import commands
from discord.ext.commands.context import Context

from yt_dlp import YoutubeDL

file = open('../log.json', 'w')

# Commands declare
@commands.command()
async def play(ctx : Context, *,  search : str):
    voice_state = ctx.author.voice

    if voice_state is None:
        return await ctx.send('Hay tham gia vao voice chat')

    info = YoutubeDL({
        'format': 'bestaudio',
        'noplaylist': 'True'
    }).extract_info(f"ytsearch:{search}", download=False)

    if not info:
        return await ctx.send('Khong the tai bai hat nay, xin vui long thu lai')

    entry = info['entries'][0]

    m4aList = list(filter(lambda x: x['audio_ext'] == 'm4a', entry['formats']))

    return await ctx.send(m4aList[0]['url'])

# Init
def init_music_commands(bot: commands.Bot):
    bot.add_command(play)
