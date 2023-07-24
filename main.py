from intents import get_intents
from discord.ext.commands import Bot

# Command imports
from cmds.fun_cmds import init_fun_commands
from cmds.music_cmds import init_music_commands

# Constants
token = 'MTExODQzNTIzNzk5OTkzOTY1NQ.G8STIG.Oe61fxRbuvIqD4iCEX4JJix66UvbQRiFjDiSh8'
command_prefix = "?"
intents = get_intents()

# Init bot instance
bot = Bot(command_prefix=command_prefix, intents=intents)

# Init bot commands
init_fun_commands(bot)
init_music_commands(bot)

# Run bot
bot.run(token)
