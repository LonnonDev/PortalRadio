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
try:
	source = '/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio'
	os.chdir('/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio')
except:
	source = 'E:/Coding Shit/Code/PortalRadio/'
	os.chdir('E:/Coding Shit/Code/PortalRadio/')

class CommandErrorHandler(commands.Cog, name="ErrorHandler"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'CommandError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ConversionError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ConversionError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.MissingRequiredArgument):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'MissingRequiredArgument'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ArgumentParsingError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ArgumentParsingError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.UnexpectedQuoteError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'UnexpectedQuoteError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.InvalidEndOfQuotedStringError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'InvalidEndOfQuotedStringError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ExpectedClosingQuoteError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ExpectedClosingQuoteError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.BadArgument):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'BadArgument'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.BadUnionArgument):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'BadUnionArgument'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.PrivateMessageOnly):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'PrivateMessageOnly'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.NoPrivateMessage):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'NoPrivateMessage'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.CheckFailure):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'CheckFailure'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.CheckAnyFailure):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'CheckAnyFailure'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.CommandNotFound):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'CommandNotFound'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.DisabledCommand):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'DisabledCommand'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.CommandInvokeError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'CommandInvokeError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.TooManyArguments):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'TooManyArguments'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.UserInputError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'UserInputError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.CommandOnCooldown):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'CommandOnCooldown'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.MaxConcurrencyReached):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'MaxConcurrencyReached'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.NotOwner):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'NotOwner'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.MissingPermissions):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'MissingPermissions'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.BotMissingRole):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'BotMissingRole'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.MissingAnyRole):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'MissingAnyRole'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.BotMissingAnyRole):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'BotMissingAnyRole'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.NSFWChannelRequired):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'NSFWChannelRequired'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ExtensionError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ExtensionError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ExtensionAlreadyLoaded):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ExtensionAlreadyLoaded'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ExtensionNotLoaded):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ExtensionNotLoaded'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.NoEntryPointError):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'NoEntryPointError'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ExtensionFailed):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ExtensionFailed'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass
		elif isinstance(error, commands.ExtensionNotFound):
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			errortype = 'ExtensionNotFound'
			embed=discord.Embed(title=f"Error {errortype}", color=color)
			embed.add_field(name="-", value=f"```\n{error}\n```", inline=False)
			await ctx.send(embed=embed, delete_after=30)
			try:
				await ctx.message.delete()
			except:
				pass

		ctx.author = 'console'
		erro = traceback.format_exception(type(error), error, error.__traceback__)
		dw = ''
		error = dw.join(erro)
		log(ctx, '\n\nIgnoring exception in command {}:'.format(ctx.command))
		log(ctx, error)

def log(ctx, logtext):
	try:
		source = '/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio'
		os.chdir('/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio')
	except:
		source = 'E:/Coding Shit/Code/PortalRadio/'
		os.chdir('E:/Coding Shit/Code/PortalRadio/')
	errorlog = open("errorlogs.txt", 'w', encoding='utf-8')
	try:
		source = '/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio'
		os.chdir('/media/Lonnon/CoolDrive/Coding Shit/Code/PortalRadio')
	except:
		source = 'E:/Coding Shit/Code/PortalRadio/'
		os.chdir('E:/Coding Shit/Code/PortalRadio/')
	now = datetime.now()
	ct = now.strftime("%H:%M:%S")
	if ctx.author == 'console':
		person = ''
	else:
		person = str(ctx.author.id)
	errorlog.write(f"\n{ct} | {ctx.author} {person} {logtext}")
	errorlog.close()

def setup(bot):
	print("ErrorHandler Loaded...")
	bot.add_cog(CommandErrorHandler(bot))
def teardown(bot):
	print("ErrorHandler Unloaded...")