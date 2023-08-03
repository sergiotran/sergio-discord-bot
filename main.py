from intents import get_intents
from discord.ext.commands import Bot
from helpers.env import getEnv
import asyncio
from cogs.example import ExampleCog
from cogs.fun import FunCog 
from cogs.music import MusicCog


async def setup_cogs(bot : Bot):
    await bot.add_cog(ExampleCog(bot))
    await bot.add_cog(FunCog(bot))
    await bot.add_cog(MusicCog(bot))

def main():
    token = getEnv('DISCORD_TOKEN')
    command_prefix = "?"
    intents = get_intents()

    bot = Bot(command_prefix=command_prefix, intents=intents)

    asyncio.run(setup_cogs(bot))

    if token:
        bot.run(token)

if __name__ == "__main__":
    main()
