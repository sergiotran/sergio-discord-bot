from discord.ext import commands

class FunCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def chui(self, ctx: commands.Context, *, name: str):
        await ctx.send('Dit me ' + name)
