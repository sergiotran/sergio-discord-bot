from discord.ext import commands
from discord.message import Message

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx : commands.Context):
        await ctx.send('Pong')

    @commands.Cog.listener()
    async def on_message(self, message : Message):
        if message.author == self.bot.user:
            return

        if 'hello' in message.content.lower():
            await message.channel.send('Hi')
