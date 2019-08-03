import os
import time
import json
import random
import logging
import asyncio
import aiohttp
import discord
import requests
import configparser



from shutil import copyfile
from discord.ext.commands import BucketType
from datetime import datetime, timedelta
from discord import utils as dutils
from discord.ext import commands
from dateutil.relativedelta import relativedelta
#from asyncpg.pool import Pool
#from dbutils import config
#from utils.config import config

def f_time(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return ' {0} hours, {1} minute {2} second.'.format(hours,minutes,sec)
    elif minutes > 1 and sec == 1:
        return '{0} days, {1} hours, {2} minutes {3} second.'.format(days,hours,minutes,sec)
    elif minutes == 1 and sec > 1:
        return '{0} days, {1} hours, {2} minute {3} seconds.'.format(days,hours,minutes,sec)
    else:
        return '{0} days, {1} hours, {2} minutes {3} seconds.'.format(days,hours,minutes,sec)




# Setup logger
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('@%(name)s [%(levelname)s] %(asctime)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(max_messages=15000, command_prefix='=')

bot.remove_command('help')


# On bot login
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name='With AA Members!'))
	print('/-----------------------------------------------------------------------------')
	print('| # ME')
	print('| Name:     ' + bot.user.name)
	print('| ID:       ' + str(bot.user.id))

	print('|----------------------------------------------------------------------------')
	print('| # MODULES')
	
#	bot.load_extension('misc')
#	bot.load_extension('dblcog')
#	bot.load_extension('admin')

@bot.event

async def on_message(message):

	if message.channel.category.id == 585007278931836949:


		if 'discord.gg' in message.content.lower():
			uid = message.author
			async for msg in message.channel.history(limit=100):
				if msg.author == bot.user:
					msgd = await message.channel.fetch_message(msg.id)
					await msg.delete()
					embed = discord.Embed(timestamp=datetime.now(),color=0x0000ff)
					embed.add_field(name='Reminder',value='**⚠️You can post 2 ads per 24 hours. \n ⚠️Ads without a description will get deleted. \n ⚠️Ads with expired invites will get deleted. \n ⚠️When you leave this server all ads posted by you will get auto-deleted. \n ⚠️No link shorteners or any kind of malicious links.**')
					embed.set_footer(text="Thank you for using Advanced Advertisements")
					await message.channel.send(embed=embed)

	await bot.process_commands(message) 
#@bot.command()d
#@commands.is_owner()
#async def init(ctx):
#	for category in ctx.guild
				
@bot.event
async def on_member_remove(member):
	def leaver(member):
		return member.id == bot.user
	for channel in member.guild.text_channels:
		await channel.purge(limit=700, check=lambda m: m.author.id == member.id, bulk=False)
admins = [115476520922906626]
@bot.command()
async def say(ctx,*,content:str):
	if ctx.author.id in admins:
		em = discord.Embed(title='',color=0xff00ff)
		em.add_field(name='Advanced Advertisements',value=content)
		await ctx.send(embed=em)
		await ctx.message.delete()
		
bot.run(str(os.environ.get('BOT_TOKEN')))
