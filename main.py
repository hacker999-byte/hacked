import discord
from discord.ext import commands, tasks
import string
import time
import requests
import asyncio
#import json
import random
import os
from random import randint
import clear
import sys
#from os import system, name
#import colored
from colored import fg, attr
#from pypresence import Presence
import threading
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor

class colors:

  main = fg('#00fefc')
  reset = attr('reset')

os.system(f'cls & title [DOXX] - Configuration')


proxies = []
rotating = cycle(proxies)

try:
  for line in open('Proxies.txt'):
    proxies.append(line.replace('\n',""))
  # print(f"Trying Proxies Successfull")
except:
    print(f"Failed to Load Proxies From Proxies.txt")


token = input(f'{colors.main}> {colors.reset}Token{colors.main}:{colors.reset} ')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

if sys.platform == "linux":
    clear = lambda: sys("clear")
else:
    clear = lambda: sys("cls & mode 70,24")

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.AutoShardedBot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")



class DOXX:
  
 def __init__(self):
      self.colour = '\x1b[38;5;196m'
 
 def BanFunction(guild, member):
   while True:
     r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
     if 'retry_after' in r.text:
         time.sleep(r.json()['retry_after'])
     else:
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
           print(f"[{colors.main}-{colors.reset}] {colors.main}Banned {colors.reset}{member.strip()}")
           break
        else:
          break

 async def Ban():
   guild = input(f"{colors.main}>{colors.reset} Guild ID{colors.main}:{colors.reset} ")
   print()
   members = open('Scraped/members.txt')
   for member in members:
      threading.Thread(target=DOXX.BanFunction, args=(guild, member)).start()
      threading.Thread(target=DOXX.BanFunction, args=(guild, member)).start()
   members.close()




 
 async def Menu():
  os.system(f'cls & title [DOXXbeta ] - Connected: {client.user}')
  print(f'''

              \x1b[38;5;196m██████╗░░█████╗░██╗░░██╗██╗░░██╗
              \x1b[38;5;196m██╔══██╗██╔══██╗╚██╗██╔╝╚██╗██╔╝
              \x1b[38;5;196m██║░░██║██║░░██║░╚███╔╝░░╚███╔╝░
              \x1b[38;5;196m██║░░██║██║░░██║░██╔██╗░░██╔██╗░█▄▄ █▀▀ ▀█▀ ▄▀█
              \x1b[38;5;196m██████╔╝╚█████╔╝██╔╝╚██╗██╔╝╚██╗█▄█ ██▄ ░█░ █▀█
              \x1b[38;5;196m╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  
                     
                 ┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓
                    ┋ \x1b[38;5;196m[1\x1b[38;5;196m] Ban Members  

                    ┋ \x1b[38;5;196m[X\x1b[38;5;196m] Exit                 
                 ┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛ {colors.reset}                 
                        [{colors.main}Credits{colors.reset}:\x1b[38;5;196m ROXX ADDA ]   
'''.replace("$", f"{colors.main}${colors.reset}").replace("┅", f"{colors.main}┅{colors.reset}").replace("┋", f"{colors.main}┋{colors.reset}"))
  option=input(f"{colors.main}>{colors.reset} Action{colors.main}:{colors.reset} ")
  if option == '1' or option == '1':
     await DOXX.Ban() 
     time.sleep(2)
     await DOXX.Menu()
  elif option == '2' or option == '2':
     await DOXX.kick()
     time.sleep(2)
     await DOXX.Menu()
  elif option == '3' or option == '3':
     await DOXX.Menu()
  elif option == '4' or option == '4':
     await DOXX.Guild()
     time.sleep(2)
     await DOXX.Menu()
  elif option == 'X' or option == 'x':
     os._exit(0)


  @staticmethod
  def is_virtualized(self):
        for check in self.blacklisted_platforms:
            if self.manufacturer == check:
                return True
        return False




 def Startup():
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{colors.main}> {colors.reset}Token Not Valid')
            input()
            os._exit(0)

 @client.event
 async def on_ready():
    await DOXX.Menu()

if __name__ == "__main__":
  DOXX.Startup()
