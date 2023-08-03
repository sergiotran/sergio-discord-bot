import asyncio
import discord
from discord.ext import commands

from yt_dlp import YoutubeDL

from helpers.utils import is_youtube_url, log_to_file

class MusicCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        self.is_play = False
        self.queue = []

        self.YT_DL_OPTIONS = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

    def isPlaying(self) -> bool:
        return self.is_play

    async def joinChannel(self, ctx: commands.Context):
        voice_client = None
        if ctx.author.voice:
            voice_channel = ctx.author.voice.channel

            if ctx.voice_client is not None:
                voice_client = await ctx.voice_client.connect(voice_channel.id)
            else:
                voice_client = await voice_channel.connect()
        else:
            await ctx.send('Ban dang khong o trong voice channel')

        return voice_client

    async def leaveChannel(self, ctx):
        # Check if the bot is connected to a voice channel
        if ctx.voice_client is not None:
            # Disconnect the bot from the voice channel
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("Toi khong o trong voice channel nao ca")

    def searchYT(self, query: str):
        res = None
        with YoutubeDL(self.YT_DL_OPTIONS) as ytd:
            if is_youtube_url(query):
                res = ytd.extract_info(query, download=False)
            else:
                res = ytd.extract_info(f"ytsearch:${query}", download=False)
            if not res:
                return None
            entry = res['entries'][0]

            url = list(
                filter(lambda x: x['ext'] == 'm4a', entry['formats'])
            )[0]['url']

        return url

    @commands.command()
    async def play(self, ctx: commands.Context, *, query: str):
        url = self.searchYT(query)

        if not url:
            await ctx.send('Co loi xay ra khi search voi tu khoa: ' + query)

        voice_client = await self.joinChannel(ctx)

        self.is_play = True
        self.queue.append(url)

        while self.queue:
            current_url = self.queue.pop(0)

            if voice_client and self.isPlaying():
                voice_client.play(discord.FFmpegPCMAudio(current_url))


            while self.isPlaying():
                await asyncio.sleep(1)

            await self.leaveChannel(ctx)
        else:
            self.is_play = False

