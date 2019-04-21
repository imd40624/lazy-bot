import discord
import asyncio
import youtube_dl
import os
import colorsys
import logging
import typing
import json
import aiohttp
import requests
import string
import translate
import html
import math
import functools
import psutil
import traceback
import re
from random import choice as randchoice
import rethinkdb as r
import discord, datetime, time
from translate import Translator
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions 
from discord.utils import get,find
from time import localtime, strftime
import requests as rq
import random
from discord.ext import commands
from urllib.request import Request, urlopen
import json
import urllib
import requests
import Token
import time
from datetime import datetime
from urllib.parse import quote_plus

start_time = time.time()

bot = commands.Bot(command_prefix="ly.")


async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='ly.help', type=2))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+' users', type=3))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name=str(len(bot.servers))+' servers', type=3))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='music'))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='I need some vote;('))
        await asyncio.sleep(5)
            
            
@bot.event
async def on_ready():
   bot.loop.create_task(status_task())
   print(bot.user.name)
	
   print('Servers connected to:')
   for server in bot.servers:
        print(server.name)
    
    
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")   
    
    
    
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xe67e22)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Created at", value=user.created_at)
    embed.add_field(name="Nickname", value=user.nick)
    embed.add_field(name="Bot", value=user.bot)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)  
    
    
@bot.command(Pass_Context=True) 
async def invite(ctx):
    embed=discord.Embed(title="Invite Me", description="Invite LaZy today!", color=0xff0000)
    embed.set_author(name="Invite LaZy")
    embed.set_footer(text="Made By DAKSH#0053") 
    embed.add_field(name="Invite", value=f"[Click here for Link](https://discordapp.com/api/oauth2/authorize?client_id=569463328942850078&permissions=8&scope=bot)")
    await bot.send(embed=embed)
    
  
@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await bot.send('{0.name} joined in {0.joined_at}'.format(member)) 
   
   
   
@bot.event
async def on_member_remove(member):
    server = member.server
    channel = get(member.server.channels, name="join-leave")
    s=discord.Embed(description="**{}** just left the server".format(member.name), colour=0xf84b50, timestamp=datetime.utcnow())
    s.set_author(name=member, icon_url=member.avatar_url)
    s.set_footer(text="User ID: {}".format(member.id))
    await bot.send_message(channel, embed=s)   
   
   
   
@bot.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await bot.send_message(ctx.message.channel, embed=em)
    await bot.delete_message(ctx.message)
   
   
   
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await bot.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await bot.delete_message(ctx.message)   
      
      
      
      
      
      
bot.run(os.environ['BOT_TOKEN'])      
