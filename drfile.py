import discord
from discord.ext import commands

TOKEN = 'Njc1NzA4MDQ0OTE4OTE1MDk0.XkAqsw.Rhc6w9g-1qpsyV5DbBHALOivwII'

client = commands.Bot(command_prefix = ['!'])


@client.event
async def on_ready():
    print('klar')

@client.event
async def on_member_join(member):
    print(f'{member} har tilsluttet')

@client.event
async def on_member_remove(member):
    print(f'{member} har foladt os :(') 

@client.command()
async def where(ctx):
    await ctx.send('too the RANCH!')

@client.command()
async def what(ctx):
    await ctx.send('Cash me outshide ha bow da!')


client.run(TOKEN)
