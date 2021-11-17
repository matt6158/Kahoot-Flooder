import os
print("Installing libs.")
try:
    from kahoot import client 
    import string 
    import random 
    import colorama 
    from colorama import Fore, Back, Style  
    import time 
    import threading
    import ctypes
    import requests
    from pypresence import Presence 
except:
    os.system("pip install pypresence")
    os.system("pip install colorama")
    os.system("pip install KahootPY") 



bot = client() 
version = '1.0'
os.system('cls') 
ctypes.windll.kernel32.SetConsoleTitleW(f"[Kahoot Spammer v1.0] Made by Tooreex | https://discord.gg/r8vhcbFM9y") 
gameid = input(f"{Fore.MAGENTA}{Style.NORMAL}> Enter the game pin: ") 
custom_usr = input(f"{Fore.MAGENTA}{Style.NORMAL}> Enter the username for your bots: ")
threadamount = input(f"{Fore.MAGENTA}{Style.NORMAL}> Threads: ") 
print("") 
print(f"{Fore.MAGENTA}{Style.NORMAL}> Loading") 
time.sleep(2) 
print("") 
def joingame(): 
    user = ('').join(random.choices(string.ascii_letters.lower() + string.digits, k=8)) 
    usrname = custom_usr+user
    bot.join((gameid), usrname) 
    def joinHandle() : 
        pass 
    bot.on("joined", joinHandle) 
    print (f"{Fore.MAGENTA}{Style.NORMAL} Joined | {Style.BRIGHT}{usrname} {Style.NORMAL}")
    while True: 
        try:
            joingame()
        except:
            print (f"{Fore.MAGENTA}{Style.NORMAL} Error | {Style.BRIGHT}{usrname} {Style.NORMAL}") 

ctypes.windll.kernel32.SetConsoleTitleW(f"[Kahoot Spammer v1.0] Spamming {gameid} | {threadamount} Threads | {version}") 
threadamount = int(threadamount)
for x in range(threadamount):
    t1 = threading.Thread(target=joingame)
    t1.start()
