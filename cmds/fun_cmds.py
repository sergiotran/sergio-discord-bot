from discord.ext import commands
from discord.ext.commands.context import Context

# Commands declare
@commands.command()
async def chui(ctx : Context, *args):
    if len(args) == 0:
        return

    name = " ".join(args)
    await ctx.send("Dit me " + name)

# Init
def init_fun_commands(bot: commands.Bot):
    bot.add_command(chui)
