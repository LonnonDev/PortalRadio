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
from discord.ext import tasks, commands
os.chdir('E:/Coding Shit/Code/PortalRadio/')


class TasksCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    def cog_unload(self, bot):
        self.printer.cancel()

    @tasks.loop(seconds=60.0)
    async def printer(self):
        await self.bot.wait_until_ready()
        guild = self.bot.get_guild(785241980162408450)
        david = guild.get_member(348559658232971265)
        if david.nick != "TransLover":
            await david.edit(nick="TransLover")
        
# setup the Cog
def setup(bot):
	print("Tasks Commands Loaded...")
	bot.add_cog(TasksCog(bot))
def teardown(bot):
	print("Tasks Commands Unloaded...")