import colorama
from colorama import Fore
import time
import secrets
import string
user = string.ascii_lowercase + string.digits
pwdd = string.ascii_letters + string.digits + string.punctuation
colorama.init()
time.sleep(0.25)
print("Installing libraries...")
time.sleep(0.5)
print(Fore.LIGHTRED_EX + """
                     .__    .___                                        ____  ___            
____________  ______ |__| __| _/____    ____  ____   ____   ____   ____ \   \/  /    .__     
\_  __ \__  \ \____ \|  |/ __ |\__  \ _/ ___\/ ___\ / ___\_/ __ \ /    \ \     /   __|  |___ 
 |  | \// __ \|  |_> >  / /_/ | / __ \/  \__\  \___/ /_/  >  ___/|   |  \/     \  /__    __/ 
 |__|  (____  /   __/|__\____ |(____  /\___  >___  >___  / \___  >___|  /___/\  \    |__|    
            \/|__|           \/     \/     \/    \/_____/      \/     \/      \_/            
""")
time.sleep(0.45)
print("OVERCLOCKED account creation - true (mode 1)")
print("Fast account creation - true (mode 2)")
print("Extreme account creation - true (mode 3)")
print("Webhook account creation - true (mode 4)")
print("Millions account creaton mode - true (mode 5)")
time.sleep(0.1)
input("Press enter to continue...")
print("Starting account creation...")
amount1 = 0
amount2 = 9999
while amount1 <= amount2:
    n = 0
    a = 999
    amount1 = amount1 + 1
    while n <= a:
        n = n + 1
        print(Fore.LIGHTBLUE_EX+"[-] Creating username (length 17)...")
        time.sleep(0)
        print(Fore.LIGHTBLUE_EX+"[-] Creating password (length 85)...")
        time.sleep(0)
        username = ''
        for i in range(17):
            username +=''.join(secrets.choice(user))
        pwd = ''
        for i in range(85):
            pwd += ''.join(secrets.choice(pwdd))
        time.sleep(0)
        print(Fore.CYAN+"[-] Writing data to file...")
        time.sleep(0)
        file1 = open("accounts.txt", "a")
        L = ["Username: "+str(username),'\n','Password: '+str(pwd),'\n','\n']
        file1.writelines(L)
        file1.close()
        print(Fore.GREEN+"[-] Written! Adding more to file in in 0 seconds...")
        time.sleep(0)
    if n >= a:
        print("Uploading text file to webhook...")
        from discord_webhook import DiscordWebhook
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1065382589390655670/xZydyOKHvVxMC2txKTnoNuHLEx4__9BtrWTPkAqS3pRf226l5U02bPyZjBLiaFJm9kdq', content='Account File **'+str(amount1)+'** Created:', username="Account Webhook (Made by Max)")
        response = webhook.execute()
        time.sleep(0.25)
        webhook1 = DiscordWebhook(url='https://discord.com/api/webhooks/1065382589390655670/xZydyOKHvVxMC2txKTnoNuHLEx4__9BtrWTPkAqS3pRf226l5U02bPyZjBLiaFJm9kdq', username="Account Webhook (Made by Max)")
        with open("accounts.txt", "rb") as f:
             webhook1.add_file(file=f.read(), filename='accounts.txt')
        response = webhook1.execute()
        time.sleep(1)
        print("Clearing text file...")
        time.sleep(0.5)
        with open("accounts.txt",'r+') as file:
            file.truncate(0)
        time.sleep(2)
        n = 0
