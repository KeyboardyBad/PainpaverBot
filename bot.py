import discord
import sys
import random
import asyncio
from discord.ext import commands, tasks
from time import localtime, strftime, sleep
from datetime import datetime

intents = discord.Intents.all()
intents.guilds = intents.members = True
TOKEN = "TOKEN"
log_channel_id = 0 #把這個改成log頻道（例如管理員的頻道）的ID
hb_channel_id = 0 #把這個改成祝人生日快樂的頻道的ID
hb_role = "<@&0>" #把這個改成今年壽星身分組的@（格式為"<@&123456789>"）
description = "原本是搞人用的，現在沒人可搞，改邪歸正，然後開源了（笑臉表符）"
bot = commands.Bot(command_prefix=commands.when_mentioned_or('^'), description=description, intents=intents)

bot.hbtimes = 0
@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    happy_birthday.start()

"""@bot.command()
async def cap(ctx):
    '''會考倒數'''
    d = datetime(2022, 5, 21, 8, 20, 0)-datetime.now()
    await ctx.channel.send(f"距離`2022/5/21 8:20:00`\n還有`{d.days}`天`{d.seconds//3600}`小時`{d.seconds%3600//60}`分鐘`{d.seconds%60}`秒")""" #其實是111會考倒數
@bot.command()
async def 斷(ctx):
    """接龍萬用"""
    await ctx.send("㡭三小>:(") #打錯字是故意的

@bot.command()
async def arstarst(ctx):
    """arstarst"""
    for i in range(12):
        await ctx.author.send("arstarst")
        await asyncio.sleep(1)
    await ctx.author.send(":)")

@bot.command()
async def echo(ctx, *, args):
    """for test purposes"""
    await ctx.channel.send(args)

@bot.command()
async def pick(ctx, n: int, *choices):
    """從多個選項中隨機選出n個"""
    await ctx.channel.send("結果為："+ "、".join(random.sample(choices, n)))
@bot.command()
async def start(ctx):
    """開始祝人生日快樂"""
    if happy_birthday.is_running():
        await ctx.channel.send("已經開始了")
    else:
        happy_birthday.start()
        await ctx.channel.send("開始了")
@bot.command()
async def stop(ctx):
    """暫停祝人生日快樂"""
    if not happy_birthday.is_running():
        await ctx.channel.send("還沒開始")
    else:
        happy_birthday.stop()
        await ctx.channel.send("停了")

@bot.group()
async def status(ctx):
    """正在..."""
    if ctx.invoked_subcommand is None:
        await bot.change_presence()
        await bot.get_channel(log_channel_id).send(f"<@{ctx.author.id}>已清除機器人狀態！")
@status.command()
async def play(ctx, *, game):
    """正在玩..."""
    await bot.change_presence(activity=discord.Game(game))
    await bot.get_channel(log_channel_id).send(f"<@{ctx.author.id}>已設定機器人狀態：正在玩{game}")
@status.command()
async def stream(ctx, url, *, name):
    """正在直播...網址在前"""
    await bot.change_presence(activity=discord.Streaming(name=name, url=url))
    await bot.get_channel(log_channel_id).send(f"<@{ctx.author.id}>已設定機器人狀態：正在直播{name}，網址{url}")
@status.command()
async def watch(ctx, *, name):
    """正在看..."""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
    await bot.get_channel(log_channel_id).send(f"<@{ctx.author.id}>已設定機器人狀態：正在看{name}")
@status.command()
async def listen(ctx, *, name):
    """正在聽..."""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
    await bot.get_channel(log_channel_id).send(f"<@{ctx.author.id}>已設定機器人狀態：正在聽{name}")

@tasks.loop(seconds = 5)
async def happy_birthday():
    await bot.get_channel(hb_channel_id).send(hb_role + "生日快樂！")
    bot.hbtimes+=1
    sys.stdout.flush();print(f"\r{strftime('%Y-%m-%d %H:%M:%S', localtime())}\t祝完了第{bot.hbtimes}次\t", end="")
    if all([c == "0" for c in str(bot.hbtimes)[1:]]):
        print(f"\n{strftime('%Y-%m-%d %H:%M:%S', localtime())}\t祝完了第{bot.hbtimes}次\t", end="")

@bot.group()
async def this_is(ctx):
    """這裡是..."""
    if ctx.invoked_subcommand is None:
        await ctx.channel.send("這什麼都不是")
@this_is.command()
async def gay_club(ctx):
    """...男同俱樂部，不是群聊"""
    await ctx.channel.send(file=discord.File(r"gay-not-general.mp4"))
@this_is.command()
async def general(ctx):
    """...群聊，不是男同俱樂部"""
    await ctx.channel.send(file=discord.File(r"general-not-gay.mp4"))
@this_is.command()
async def not_poor_club(ctx):
    """...群聊，不是丐幫（你媽了個ㄅ）"""
    await ctx.channel.send(file=discord.File(r"general-not-poor-club.mp4"))

bot.run(TOKEN)
