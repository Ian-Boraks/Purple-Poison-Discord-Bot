import api
import discord
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

guild_ids = api.guild 

@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send("Pong!")

client.run(api.api)