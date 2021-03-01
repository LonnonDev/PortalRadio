import traceback
import sys
from discord.ext import commands
import discord
import time
import json
import random
import os
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
import itertools
os.chdir('E:/Code/PortalRadio/')

# Useful Cog
class Useful(commands.Cog, name="Useful Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['ping', 'uptime'])
	async def info(self, ctx):
		ping = '{0}ms'.format(round(float(self.bot.latency) * 1000), 0)
		randomimg = random.randint(1, 11)
		datetimeformat = "%d Day(s), %H Hour(s), %M Minute(s), %S Second(s)"
		x = datetime.datetime.now()
		x = str(x.strftime("%d Day(s), %H Hour(s), %M Minute(s), %S Second(s)"))
		f = open("E:/Code/EcoIsCringe/storage/started.txt", 'r')
		time = f.read()
		f.close()
		diff = datetime.datetime.strptime(x, datetimeformat) - datetime.datetime.strptime(time, datetimeformat)
		# Silly random color
		color = random.randint(0, 0xFFFFFF)
		embed=discord.Embed(title=f"Info...", color=color)
		embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
		if randomimg == 1:
			embed.set_image(url="https://media.giphy.com/media/3og0IGzJmvAoY5ijmw/giphy.gif")
		elif randomimg == 2:
			embed.set_image(url="https://media.giphy.com/media/3og0IUEEbY9wRwrBL2/giphy.gif")
		elif randomimg == 3:
			embed.set_image(url="https://media.giphy.com/media/3osxY4Ll9eqJoY1N9m/giphy.gif")
		elif randomimg == 4:
			embed.set_image(url="https://media.giphy.com/media/l4Ki5FgQxmVUfkOvC/giphy.gif")
		elif randomimg == 5:
			embed.set_image(url="https://media.giphy.com/media/l0IylR4JqKHLjaP60/giphy.gif")
		elif randomimg == 6:
			embed.set_image(url="https://media.giphy.com/media/1gh2Upxof8mxW/giphy.gif")
		elif randomimg == 7:
			embed.set_image(url="https://media.giphy.com/media/HZMBatubcJ1sY/giphy.gif")
		elif randomimg == 8:
			embed.set_image(url="https://media.giphy.com/media/eEtcTm7xuF7nq/giphy.gif")
		elif randomimg == 9:
			embed.set_image(url="https://media.giphy.com/media/jg9OpejAzMmIg/giphy.gif")
		elif randomimg == 10:
			embed.set_image(url="https://media.giphy.com/media/akWoonvV6swIU/giphy.gif")
		elif randomimg == 11:
			embed.set_image(url="https://media.giphy.com/media/HZMBatubcJ1sY/giphy.gif")

		embed.set_thumbnail(url="attachment://test.png")
		embed.add_field(name="Uptime", value=f"Uptime of {diff} ", inline=True)
		embed.add_field(name="Ping", value=f"Ping of the bot is {ping} ", inline=True)
		await ctx.send(embed=embed)

	# Reloads the Cog
	@commands.command()
	@commands.is_owner()
	async def reload(self, ctx, cog : str):
		initial_extensions = [f'cogs.{cog}']
		for extension in initial_extensions:
			self.bot.reload_extension(extension)
		await ctx.send(f"Reloaded {cog}.py")


# setup the Cog
def setup(bot):
	print("Useful Commands Loaded...")
	bot.add_cog(Useful(bot))
def teardown(bot):
	print("Useful Commands Unloaded...")