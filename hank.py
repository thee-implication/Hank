import discord
import sqlite3
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "$", intents=intents)


@client.event
async def on_ready():
	channel = client.get_channel(804579091700514869)
	await channel.send('Oh Sweet baby rays, Hank is ready.')
	print("Oh Sweet baby rays, Hank is READY")

@client.event 
async def on_message(message):
 if message.content.startswith('$getmembers'):
 	member_list = []
 	for guild in client.guilds:
 		print(guild)
 		for member in guild.members:
 			member_list.append(member)

client.run('OTgwMjg2MDE2MTM0OTg3ODc2.GB6pmM.TDIRbLlf59zNaoOiDnmKATNzeaAUKAhlAEU84E')
