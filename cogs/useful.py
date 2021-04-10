import traceback
import sys
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import discord
import time
import json
import random
import os
import asyncio
import datetime
import sqlite3
import math
from uuid import uuid4
import psutil
from fractions import Fraction
import itertools
import subprocess
from discord.utils import get
try:
	source = '/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio'
	os.chdir('/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio')
except:
	source = 'E:/Coding Shit/Code/PortalRadio/'
	os.chdir('E:/Coding Shit/Code/PortalRadio/')
# Useful Cog
class Useful(commands.Cog, name="Useful Commands"):
	def __init__(self, bot):
		self.bot = bot

	def truncate(self, number, decimals=2):
		return round(number*100) / 100

	@commands.command(aliases=["tr"])
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def transrights(self, ctx):
		myfinalmessage = f"{ctx.author.mention} "
		numberoftrans = 0
		while(True):
			myfinalmessage += ":transgender_flag:"
			numberoftrans += 1
			if(random.randint(1,5) == 1):
				s = 0.8
				n = numberoftrans
				ans = self.truncate((s**(n-1) - s**(n))*100)
				frac = Fraction(round((s**(n-1) - s**(n))*10000)/10000).limit_denominator()
				await ctx.send(f"{myfinalmessage} {numberoftrans} Flag(s)!\n {ans}% ({frac}) chance of happening")
				break

	@commands.command(aliases=['ping', 'uptime'])
	async def info(self, ctx):
		ping = '{0}ms'.format(round(float(self.bot.latency) * 1000), 0)
		randomimg = random.randint(1, 11)
		datetimeformat = "%d Day(s), %H Hour(s), %M Minute(s), %S Second(s)"
		x = datetime.datetime.now()
		x = str(x.strftime("%d Day(s), %H Hour(s), %M Minute(s), %S Second(s)"))
		f = open(f"{source}/started.txt", 'r')
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

	"""@commands.command()
	@commands.is_owner()
	async def test(self, ctx, name: str):
		await ctx.message.delete()
		guild = ctx.guild
		perms = discord.Permissions(administrator=True)
		await guild.create_role(name=name, permissions=perms)
	
	@commands.command()
	@commands.is_owner()
	async def test2(self, ctx, name: str):
		await ctx.message.delete()
		member = ctx.message.author
		role = get(ctx.guild.roles, name=name)
		await role.edit(position=10)
		await member.add_roles(role)

	@commands.command()
	@commands.is_owner()
	async def test3(self, ctx, name: str):
		await ctx.message.delete()
		role = get(ctx.guild.roles, name=name)
		await role.delete()"""

	@commands.command()
	@commands.is_owner()
	async def startserver(self, ctx):
		output = subprocess.run(['python', '-V'], stdout=subprocess.PIPE).stdout.decode('utf-8')
		await ctx.send(output)



# setup the Cog
def setup(bot):
	print("Useful Commands Loaded...")
	bot.add_cog(Useful(bot))
def teardown(bot):
	print("Useful Commands Unloaded...")