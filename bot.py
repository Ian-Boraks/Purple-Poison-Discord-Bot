import api
import discord
from discord.ext import commands
from datetime import date


client = discord.Client()#Creates Client
client = commands.Bot(command_prefix=["pp.", "Pp.", "PP.", "pP."])#Sets prefix for commands(!Command)
client.remove_command("help")#Removes help command

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def help(ctx):
    await ctx.send("""pp.<command> <arg>\n\ncommand     |      arg\nnew_ctf      |    "[ctf name]"\nnew_channel      |      "[channel name]"\nnew_challenge (chall)      |       "[challenge name]"\nprogress_update (pu)    |    🟢, 🔵, 🟡, 🔴""")

@client.command(pass_context=True)
async def new_ctf(ctx, ctf_name):
    todays_date = date.today()
    category_name = "🟢 [" + str(todays_date.year) + "] " + ctf_name
    new_category = await ctx.guild.create_category(category_name)
    new_gen = await new_category.create_text_channel("general")
    new_botspam = await new_category.create_text_channel("bot-spam")

@client.command(pass_context=True)
async def new_channel(ctx, channel_name):
    await ctx.message.channel.category.create_text_channel(channel_name)


@client.command(pass_context=True)
async def new_challenge(ctx, channel_name):
    await ctx.message.channel.category.create_text_channel("🔵" + channel_name)

@client.command(pass_context=True)
async def chall(ctx, channel_name):
    await ctx.message.channel.category.create_text_channel("🔵" + channel_name)

@client.command(pass_context=True)
async def progress_update(ctx, new_emoji):
    if ctx.message.channel.name[0] not in ["🟢", "🔵", "🟡", "🔴"]:
        await ctx.send("That is not a valid channel to run **progress_update** in.\nPlease run this command in a challenge channel")
        return

    # if new_emoji is not in list of emojis break
    if new_emoji not in ["🟢", "🔵", "🟡", "🔴"]:
        await ctx.send("That is not a valid emoji.\nPlease use one of the following: 🟢, 🔵, 🟡, 🔴")
        return

    new_name = new_emoji + ctx.message.channel.name[1:]
    temp = await ctx.message.channel.edit(name=new_name)
    await ctx.send("Progress updated!")

@client.command(pass_context=True)
async def pu(ctx, new_emoji):
    if ctx.message.channel.name[0] not in ["🟢", "🔵", "🟡", "🔴"]:
        await ctx.send("That is not a valid channel to run **progress_update** in.\nPlease run this command in a challenge channel")
        return

    # if new_emoji is not in list of emojis break
    if new_emoji not in ["🟢", "🔵", "🟡", "🔴"]:
        await ctx.send("That is not a valid emoji.\nPlease use one of the following: 🟢, 🔵, 🟡, 🔴")
        return

    new_name = new_emoji + ctx.message.channel.name[1:]
    temp = await ctx.message.channel.edit(name=new_name)
    await ctx.send("Progress updated!")

client.run(api.api)