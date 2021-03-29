import time
import json
import random
import math
import discord
import os
import sys
import sqlite3
import secrets
import tex2pix
import datetime
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from sympy import preview
from sympy.solvers import solve
import asyncio
from discord.ext import tasks, commands
from discord.ext.commands.cooldowns import BucketType
try:
	source = '/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio'
	os.chdir('/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio')
except:
	source = 'E:/Coding Shit/Code/PortalRadio/'
	os.chdir('E:/Coding Shit/Code/PortalRadio/')

conn = sqlite3.connect("people.db")
c = conn.cursor()

class Music(commands.Cog, name="Music Commands"):
	def __init__(self, bot):
		self.bot = bot

	async def getperson(self, ctx, person: discord.Member = None):
		if person == None:
			personog = ctx.author
			person = str(ctx.author.id)
			member = str(ctx)
			membername = str(ctx.author)
		else:
			personog = person
			member = str(person)
			membername = str(person)
			person = str(person.id)
		return personog, member, membername, person

	async def personhandler(self, person):
		c.execute("SELECT * FROM people WHERE id=?", (person,))
		conn.commit()
		if c.fetchone() == None:
			c.execute("INSERT INTO people (id, coin, bank) VALUES (?, 0, 0)", (person,))
			conn.commit()

	@commands.command()
	async def balance(self, ctx, person: discord.Member = None):
		color = random.randint(0, 0xFFFFFF)
		personog, member, membername, person = await self.getperson(ctx, person)
		await self.personhandler(person)
		c.execute("SELECT * FROM people WHERE id=?", (person,))
		conn.commit()
		fetchall = c.fetchall()
		fetch = fetchall[0]
		pocket = int(round(fetch[1], 2))
		bank = int(round(fetch[2], 2))
		pocket = int(float('{:0.2f}'.format(fetch[1])))
		embed=discord.Embed(title=f"Balance", color=color)
		embed.set_author(name=membername[:-5],icon_url=personog.avatar_url)
		embed.add_field(name="Pocket", value=f"{pocket} <:blueportal:821744980506181643>", inline=True)
		embed.add_field(name="Bank", value=f"{bank} <:blueportal:821744980506181643>", inline=True)
		embed.add_field(name="Total", value=f"{pocket + bank} <:blueportal:821744980506181643>", inline=True)
		await ctx.send(embed=embed)

	@commands.command(aliases=["spg","shootportal","sp", "shootpg"])
	@commands.cooldown(1, 60*2, commands.BucketType.user)
	async def shootportalgun(self, ctx):
		color = random.randint(0, 0xFFFFFF)
		personog, member, membername, person = await self.getperson(ctx)
		c.execute("SELECT * FROM people WHERE id=?", (person,))
		conn.commit()
		fetchall = c.fetchall()
		fetch = fetchall[0]
		pocket = round(fetch[1], 2)
		bank = round(fetch[2], 2)
		
		amount = 1
		paycheck = amount + pocket
		membername = str(ctx.author)
		embed=discord.Embed(name="Portal Gun", color=color)
		embed.add_field(name="You shot", value=f"{amount}<:blueportal:821744980506181643>", inline=True)
		embed.set_author(name=membername[:-5],icon_url=personog.avatar_url)
		randomimg = random.randint(1, 2)
		if randomimg == 1:
			embed.set_image(url="https://media1.tenor.com/images/0d0c8ca68d5db8231813b095ef079b76/tenor.gif")
		elif randomimg == 2:
			embed.set_image(url="https://media.tenor.com/images/e0b55c4cb1a105308b1c7fa742600ab2/tenor.gif")
		await ctx.send(embed=embed)
		c.execute("UPDATE people SET coin=? WHERE id=?", (paycheck, person))
		# commit
		conn.commit()



def setup(bot):
	print("Economy Commands Loaded...")
	bot.add_cog(Music(bot))
def teardown(bot):
	print("Economy Commands Unloaded...")