import time
import json
import random
import math
import discord
import os
from os import listdir
from os.path import isfile, join
import sys
import sqlite3
import secrets
import tex2pix
import datetime
import itertools
from discord.ext import tasks, commands
from discord.ext.commands.cooldowns import BucketType
from sympy import preview
from sympy.solvers import solve
import asyncio
import ffmpeg
os.chdir('E:/Coding Shit/Code/PortalRadio/')

FFMPEG_OPTIONS = {
	'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
	'options': '-vn',
}

class Music(commands.Cog, name="Music Commands"):
	def __init__(self, bot):
		self.bot = bot
		self.loop = False
		self.vc = None
		self.song = None
		self.guild = None
		self.ruleschannel = None

	def cog_unload(self):
		self.loopsong.cancel()

	@commands.command()
	async def play(self, ctx, *, voiceline: str):
		voice_channel = ctx.author.voice.channel 
		channel = voice_channel.name
		guild = ctx.guild
		try:
			self.vc = await voice_channel.connect()
		except:
			guild = ctx.guild
			self.vc: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
		self.song = voiceline
		self.vc.play(discord.FFmpegPCMAudio(source=f"E:/Coding Shit/Code/PortalRadio/storage/{voiceline}"))

	@commands.command()
	async def upload(self, ctx, *, customfilename: str=None):
		filename = ctx.message.attachments[0].filename
		extension = f"{filename[-3]}{filename[-2]}{filename[-1]}"
		if customfilename:
			filename = str(customfilename) + "." + str(extension)
		if extension == "ogg" or extension == "mp3" or extension == "mp4" or extension == "wav" or extension == "mov":
			await ctx.message.attachments[0].save(f"E:/Coding Shit/Code/PortalRadio/storage/{filename}")
			await ctx.send("uploaded!")
		else:
			await ctx.send("That filetype is not supported!")

	@commands.command()
	async def loop(self, ctx):
		if self.loop == False:
			self.loop = True
			self.loopsong.start()
		else:
			self.loop = False
			self.loopsong.stop()

	@tasks.loop(seconds=1.0)
	async def loopsong(self):
		try:
			if self.vc.is_playing() is False:
				self.vc.play(discord.FFmpegPCMAudio(source=f"E:/Coding Shit/Code/PortalRadio/storage/{self.song}"))
		except:
			pass

	@commands.command()
	async def storage(self, ctx):
		files = [f for f in listdir("E:/Coding Shit/Code/PortalRadio/storage") if isfile(join("E:/Coding Shit/Code/PortalRadio/storage", f))]
		per_page = 10 # 10 files per page
		pages = math.ceil(len(files) / per_page)
		cur_page = 1
		chunk = files[:per_page]
		linebreak = "\n"
		message = await ctx.send(f"Page {cur_page}/{pages}:\n{linebreak.join(chunk)}")
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")
		active = True

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
						 # or you can use unicodes, respectively: "\u25c0" or "\u25b6"

		while active:
			try:
				reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
			
				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
					if cur_page != pages:
						chunk = files[(cur_page-1)*per_page:cur_page*per_page]
					else:
						chunk = files[(cur_page-1)*per_page:]
					await message.edit(content=f"Page {cur_page}/{pages}:\n{linebreak.join(chunk)}")
					await message.remove_reaction(reaction, user)

				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
					chunk = files[(cur_page-1)*per_page:cur_page*per_page]
					await message.edit(content=f"Page {cur_page}/{pages}:\n{linebreak.join(chunk)}")
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await message.delete()
				active = False

	@commands.command()
	async def stop(self, ctx):
		try:
			self.loopsong.cancel()
		except:
			pass
		try:
			self.vc.stop()
		except:
			voice_channel = ctx.author.voice.channel 
			channel = voice_channel.name
			guild = ctx.guild
			try:
				vc = await voice_channel.connect()
			except:
				guild = ctx.guild
				vc: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
			vc.stop()

	@commands.command()
	async def status(self, ctx):
		await ctx.send(f"Loop: {self.loop}")

	@commands.Cog.listener()
	async def on_message(self, ctx):
		if ctx.channel.id == 809997824585367592:
			guild = self.bot.get_guild(785241980162408450)
			ruleschannel = guild.get_channel(809997824585367592)
			lastmessages = await ruleschannel.history(limit=2).flatten()
			message = [lastmessages[1].content, lastmessages[0].content]
			rule1 = message[0].split(" ")
			oldrulenumber = rule1[1]
			newrulenumber = int(oldrulenumber.replace(":", "")) + 1
			if ctx.content.lower().startswith(f"rule {newrulenumber}: "):
				pass
			else:
				await ctx.delete()
		else:
			pass

def setup(bot):
	print("Music Commands Loaded...")
	bot.add_cog(Music(bot))
def teardown(bot):
	print("Music Commands Unloaded...")
	vc.stop()