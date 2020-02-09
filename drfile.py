import discord
from discord.ext import commands

TOKEN = 'your token'

client = commands.Bot(command_prefix = ['!'])


@client.event
async def on_ready():
    print('bot ready')

@client.event
async def on_member_join(member):
    print(f'{member} connected to da server')

@client.event
async def on_member_remove(member):
    print(f'{member} ran away:(') 

@client.command()
async def where(ctx):
    await ctx.send('too the RANCH!')

@client.command()
async def what(ctx):
    await ctx.send('Cash me outshide ha bow da!')


client.run(TOKEN)
