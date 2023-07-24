import discord

intents = None
def get_intents() -> discord.Intents:
    global intents

    if not intents:
        intents = discord.Intents.default()

    intents.members = True
    intents.message_content = True

    return intents
