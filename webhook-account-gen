import discord_webhook
from discord_webhook import *
import colorama
from colorama import Fore
import time
import sys
import string
import secrets
import json
colorama.init()
user = string.ascii_lowercase + string.digits
pwdd = string.ascii_letters + string.digits
print(Fore.LIGHTRED_EX+"[-] Loading libraries...")
time.sleep(0.25)
print("[-] Loading dependencies...")
time.sleep(0.15)


print(Fore.LIGHTMAGENTA_EX+"[CRACKED BY POOPOOMAN] Logged in!")	

print(Fore.BLUE+"""
                                                            $$\      $$\  $$$$$$\  $$\   $$\ 
                                                            $$$\    $$$ |$$  __$$\ $$ |  $$ |
 $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\  $$$$\  $$$$ |$$ /  $$ |\$$\ $$  |
 \____$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$\$$\$$ $$ |$$$$$$$$ | \$$$$  / 
 $$$$$$$ |$$ /      $$ /      $$ /  $$ |$$$$$$$$ |$$ |  $$ |$$ \$$$  $$ |$$  __$$ | $$  $$<  
$$  __$$ |$$ |      $$ |      $$ |  $$ |$$   ____|$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$  /\$$\ 
\$$$$$$$ |\$$$$$$$\ \$$$$$$$\ \$$$$$$$ |\$$$$$$$\ $$ |  $$ |$$ | \_/ $$ |$$ |  $$ |$$ /  $$ |
 \_______| \_______| \_______| \____$$ | \_______|\__|  \__|\__|     \__|\__|  \__|\__|  \__|
                              $$\   $$ |                                                     
                              \$$$$$$  |                                                     
                               \______/                                                      
""")
time.sleep(0.25)
print("Welcome to accgenMAX.")
time.sleep(0.15)
webhook_bruh = input("Enter webhook URL: ")
time.sleep(0.25)
print("Attaching webhook URL to server...")
time.sleep(0.15)
webhook_conbruh = input("What do you want your webhook to say for a test message? ")
time.sleep(0.25)
print("Attaching content to webhook URL...")
time.sleep(0.15)
print("Running message...")
time.sleep(0.35)
webhook = DiscordWebhook(url=str(webhook_bruh), content=str(webhook_conbruh))
response = webhook.execute()
time.sleep(0.25)
n = 0
x = int(input("How many accounts do you want to generate? "))
time.sleep(0.15)
print("Saving number...")
while n <= x:
    n = n + 1
    embed_color_pallete = '8b0000', '000000', 'FFFFFF', 'FFA500', 'FFFF00', '00FF00', '000FF', 'A020F0', 'FFC0CB'
    color_pallete = Fore.RED, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX
    color = ''
    for i in range(1):
        color += ''.join(secrets.choice(color_pallete))
    embed_color = ''
    for i in range(1):
        embed_color += ''.join(secrets.choice(embed_color_pallete))
    username = ''
    for i in range(17):
        username +=''.join(secrets.choice(user))
    pwd = ''
    for i in range(85):
        pwd +=''.join(secrets.choice(pwdd))
    print(str(color)+"Loaded account data, printing into webhook in 0.5 seonds...")
    time.sleep(0.5)
    webhook = DiscordWebhook(url=str(webhook_bruh))
    embed = DiscordEmbed(title='Account '+str(n)+' Generated', description='Username: '+str(username)+'\n'+'Password: '+str(pwd), color=str(embed_color))
    webhook.add_embed(embed)
    response = webhook.execute()
    print("Executed webhook message, repeating script in 0.25 seconds...")
    time.sleep(0.25)
if n <= x:
    print(Fore.GREEN+"Finished creating accounts, exiting program in 3 seconds...")
    time.sleep(3)


