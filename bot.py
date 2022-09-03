import discord
import random
import asyncio
from discord.ext import commands, tasks
from time import localtime, strftime, sleep
from datetime import datetime

intents = discord.Intents.default()
intents.guilds = intents.members = True
TOKEN = "TOKEN"
description = "原本是搞人用的，現在沒人可搞，改邪歸正，然後開源了（笑臉表符）"
bot = commands.Bot(command_prefix="^", description=description, intents=intents)

bot.running = True
bot.totimes = 0
bot.hbtimes = 0
@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    tort.start()
    #happy_birthday.start()
    guild = bot.get_guild(933636677799411722)
    bot.bad = [member.id for member in guild.members if len(member.roles) <= 2]
    bot.theMessage = "以下成員還沒選身分組，請到<#934606478709497876>選擇：\n"+"\n".join([f"<@{id}>" for id in bot.bad])

@bot.event
async def on_member_join(member):
    if member in bot.get_guild(933636677799411722).members:
        bot.bad.append(member.id)
        bot.theMessage = "以下成員還沒選身分組，請到<#934606478709497876>選擇：\n"+"\n".join([f"<@{id}>" for id in bot.bad])
        tort.start()

@bot.event
async def on_member_remove(member):
    if member.id in bot.bad and member not in bot.get_guild(933636677799411722).members:
        bot.bad.remove(member.id)
        bot.theMessage = "以下成員還沒選身分組，請到<#934606478709497876>選擇：\n"+"\n".join([f"<@{id}>" for id in bot.bad])
        if bot.bad != []:
            tort.start()
        else:
            tort.stop()

@bot.event
async def on_member_update(before, after):
    if after in bot.get_guild(933636677799411722).members:
        if len(after.roles) >2 and after.id in bot.bad:
            bot.bad.remove(after.id)
            bot.theMessage = "以下成員還沒選身分組，請到<#934606478709497876>選擇：\n"+"\n".join([f"<@{id}>" for id in bot.bad])
        elif len(after.roles) <= 2 and after.id not in bot.bad:
            bot.bad.append(after.id)
            bot.theMessage = "以下成員還沒選身分組，請到<#934606478709497876>選擇：\n"+"\n".join([f"<@{id}>" for id in bot.bad])
        if bot.bad != []:
            tort.start()
        else:
            tort.stop()

@bot.command()
async def start(ctx):
    """開始催促（那個群）的成員選身分組"""
    if bot.bad == []:
        await ctx.channel.send("所有成員都已經選擇身分組！")
    elif ctx.author.id not in bot.bad:
        if tort.is_running():
            await ctx.channel.send("已經開始了")
        else:
            tort.start()
            await ctx.channel.send("開始了")
    else:
        await ctx.channel.send("你還沒選身分組！")
@bot.command()
async def stop(ctx):
    """暫停催促（那個群）的成員選身分組"""
    if bot.bad == []:
        await ctx.channel.send("所有成員都已經選擇身分組！")
    elif ctx.author.id not in bot.bad:
        if not tort.is_running():
            await ctx.channel.send("還沒開始")
        else:
            tort.stop()
            await ctx.channel.send("停了")
    else:
        await ctx.channel.send("你還沒選身分組！")
"""@bot.command()
async def cap(ctx):
    '''會考倒數'''
    d = datetime(2022, 5, 21, 8, 20, 0)-datetime.now()
    await ctx.channel.send(f"距離`2022/5/21 8:20:00`\n還有`{d.days}`天`{d.seconds//3600}`小時`{d.seconds%3600//60}`分鐘`{d.seconds%60}`秒")"""
@bot.command()
async def 斷(ctx):
    """接龍萬用"""
    await ctx.send("㡭三小>:(")
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
@bot.group()
async def status(ctx):
    """正在..."""
    if ctx.invoked_subcommand is None:
        await bot.change_presence()
        await bot.get_channel(940412271040024596).send(f"<@{ctx.author.id}>已清除機器人狀態！")
@status.command()
async def play(ctx, *, game):
    """正在玩..."""
    await bot.change_presence(activity=discord.Game(game))
    await bot.get_channel(940412271040024596).send(f"<@{ctx.author.id}>已設定機器人狀態：正在玩{game}")
@status.command()
async def stream(ctx, url, *, name):
    """正在直播...網址在前"""
    await bot.change_presence(activity=discord.Streaming(name=name, url=url))
    await bot.get_channel(940412271040024596).send(f"<@{ctx.author.id}>已設定機器人狀態：正在直播{name}，網址{url}")
@status.command()
async def watch(ctx, *, name):
    """正在看..."""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
    await bot.get_channel(940412271040024596).send(f"<@{ctx.author.id}>已設定機器人狀態：正在看{name}")
@status.command()
async def listen(ctx, *, name):
    """正在聽..."""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
    await bot.get_channel(940412271040024596).send(f"<@{ctx.author.id}>已設定機器人狀態：正在聽{name}")
@tasks.loop(seconds = 1)
async def tort():
    if bot.user.id in bot.bad:
        bot.bad.remove(bot.user.id)
    if bot.bad == []:
        tort.stop()
    else:
        await bot.get_channel(936146050014646303).send(bot.theMessage)
        bot.totimes+=1
        sys.stdout.flush();print(f"\r{strftime('%Y-%m-%d %H:%M:%S', localtime())}\t搞完了第{bot.totimes}次\t", end="")
        if all([c == "0" for c in str(bot.totimes)[1:]]):
            print(f"\n{strftime('%Y-%m-%d %H:%M:%S', localtime())}\t搞完了第{bot.totimes}次\t", end="")

@tasks.loop(seconds = 5)
async def happy_birthday():
    for i in range(12):
        await bot.get_channel(879250061232574525).send(r"<@&872393257424941067> 生日快樂！")
        bot.hbtimes+=1
        sys.stdout.flush();print(f"\r{strftime('%Y-%m-%d %H:%M:%S', localtime())}\t祝完了第{bot.hbtimes}次\t", end="")
        if all([c == "0" for c in str(bot.hbtimes)[1:]]):
            print(f"\n{strftime('%Y-%m-%d %H:%M:%S', localtime())}\t祝完了第{bot.hbtimes}次\t", end="")
        await asyncio.sleep(5)

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
