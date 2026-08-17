import discord
from roblox import Roblox

TOKEN = 'YOUR_DISCORD_TOKEN_HERE'

client = discord.Client(intents=discord.Intents.default())
roblox = Roblox()


@client.event
async def on_connect():
    print(f'Connected as {client.user}')

    user = await roblox.get_user(7437887983)
    print('User description: ', user.description)


@client.event
async def on_disconnect():
    await roblox.close()


client.run(TOKEN)
