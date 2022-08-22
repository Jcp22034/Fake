import requests
import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import base64
import random
import os
import datetime
import json
import httpx

def startingtitlecard():
    titlecard()
    asktokenorhook()

def titlecard():
    global fakever
    global fakedes
    os.system("cls")
    print("  _____           _            ")
    print(" |  ___|   __ _  | | __   ___  ")
    print(" | |_     / _` | | |/ /  / _ \ ")
    print(" |  _|   | (_| | |   <  |  __/ ")
    print(" |_|      \__,_| |_|\_\  \___| ")
    print()
    print("A basic fake image logger to mess with others!")
    print()
    print(f"Version {fakever} - {fakedes}")
    print("-------------------------------")

def endtitlecard():
    titlecard()
    input("\n\nSuccessfully Sent! Press enter to close!")
    os.system("cls")
    print("\n\nThank you for using Fake! Goodbye!")
    input("\n\nPress enter to close!\n\n")
    quit()

def asktokenorhook():
    print("\n\nThis self-bot uses BOTH a token and a webhook!\n\nThe token is needed to get target's information!")
    tokenorhook = 0
    tokenorhook = input("\n\nDo you want to:\n\n1) Start\n2) Help\n\nOption: ")
    if tokenorhook == str(1):
        fakingtoken()
        tokenandhook()
    elif tokenorhook == str(2):
        helpmenu()
    else:
        asktokenorhookfailed()

def asktokenorhookfailed():
    titlecard()
    print("\nIncorrect input!")
    tokenorhook = 0
    tokenorhook = input("\n\nDo you want to:\n1) Startid)\n2) Help\n\nOption: ")
    if tokenorhook == str(1):
        fakingtoken()
        tokenandhook()
    elif tokenorhook == str(2):
        helpmenu()
    else:
        asktokenorhookfailed()

def fakingtoken():
    titlecard()
    #get first part of token
    global id1
    id1 = input("\n\nEnter target's ID: ")
    if len(id1) != 18:
        fakingtokenfailed()
    else:
        if id1.isdigit():
            token1 = base64.b64encode(id1.encode('ascii'))
            token1 = str(token1)
            #generate fake parts
            faketoken2 = str(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-",k=6))
            faketoken3 = str(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-",k=26))
            #make into token format
            fakepart = faketoken2 + "." + faketoken3
            fakepart = fakepart.replace(",","")
            fakepart = fakepart.replace(" ","")
            fakepart = fakepart.replace("'","")
            token1 = token1.replace("b'","")
            token1 = token1.replace("'","")
            fakepart = fakepart.replace("[","")
            fakepart = fakepart.replace("]","")
            #compile all bits for a full token
            global totaltoken
            totaltoken = token1 + "." + fakepart
        else:
            fakingtokenfailed()

def fakingtokenfailed():
    titlecard()
    #get first part of token
    global id1
    print("\nInvalid ID!")
    id1 = input("\n\nEnter target's ID: ")
    if len(id1) != 17:
        fakingtokenfailed()
    else:
        if id1.isdigit():
            token1 = base64.b64encode(id1.encode('ascii'))
            token1 = str(token1)
            #generate fake parts
            faketoken2 = str(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-",k=6))
            faketoken3 = str(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-",k=26))
            #make into token format
            fakepart = faketoken2 + "." + faketoken3
            fakepart = fakepart.replace(",","")
            fakepart = fakepart.replace(" ","")
            fakepart = fakepart.replace("'","")
            fakepart = fakepart.replace("[","")
            fakepart = fakepart.replace("]","")
            #compile all bits for a full token
            global totaltoken
            totaltoken = token1 + "." + fakepart
        else:
            fakingtokenfailed()
    
def helpmenu():
    titlecard()
    print("\n\nHelp menu:\n\n1) Start\n2) Input target's id\n3) Input a client/human token to use for gathering data\n4) Input your webhook\n5) Nitro questions\n6) y/n if you want to get pinged\n7) Scare your friends!")
    input("\nMade for educational purposes only!\n\nPress enter to continue")
    startingtitlecard()
def tokenandhook():
    titlecard()
    global id1
    global embed
    global totaltoken
    global usertoken
    global tokenworks
    global webhooktmp
    global falsewebhook
    global pingall
    usertoken = input("\n\nTokens are ONLY used to gather data!\n\n\nEnter the token you want to use: ")
    validatetoken()
    if tokenworks == 1:
        input("\n\nValid token! Press enter to continue!")
        titlecard()
        webhooktmp = input("\n\nPlease enter your webhook url: ")
        if webhooktmp == "":
            tokenandhook()
        else:
            
            validatewebhook()
            if falsewebhook == 0:
                input("\n\nValid Webhook! Press enter to continue!")
                hideorno()
                image()
                getnitro()
                titlecard()
                pingall=input("\n\nWould you like to @everyone? y/n: ")
                if pingall[0] == "y" or pingall[0] =="Y":
                    pingall = 1
                else:
                    pingall = 0
                getinfo()
            else:
                input("\n\nInvalid Webhook! Press enter to retry!")
                tokenandhook()
    else:
        input("\n\nPress enter to retry!")
        tokenandhook()

def image():
    global imglink
    titlecard()
    ifimg = input("\n\nWould you like to attach an image to the embed? y/n: ")
    if ifimg[0] == "y" or ifimg[0] == "Y":
        imglink = input("\n\nEnter image link: ")
    else:
        imglink=False

def hideorno():
    global hideinfo
    hideinfo = 0
    titlecard()
    choice = input("\n\nWould you like to hide the generated info (make it more believable)? y/n: ")
    if choice[0] == "y" or choice[0] == "Y":
        hideinfo = 1
    else:
        hideinfo = 0

def getnitro():
    global nitro
    nitro = 0
    nitro2 = 0
    titlecard()
    editnitro = input("\n\nChange target's nitro? y/n: ")
    if editnitro[0]=="y" or editnitro[0]=="Y":
        titlecard()
        badge = input("\n\nDoes the target have a nitro badge? y/n: ")
        if badge[0] == "y" or badge[0] == "Y":
            nitro = 1
        boostbadge = input("\n\nDoes the user have a boosting badge? y/n: ")
        if boostbadge[0] == "y" or boostbadge[0] == "Y":
            nitro2 = nitro2 + 1
        custombanner = input("\n\nDoes the target have a gif/playable custom banner? y/n: ")
        if custombanner[0] == "y" or custombanner[0] == "Y":
            nitro = 2
            nitro2 = nitro2 + 1
        if nitro == 2 or nitro2 > 1:
            nitro = "Nitro"
        elif nitro == 1:
            nitro = "Nitro Classic"
        else:
            nitro = "None"
    else:
        nitro="None"
        
def getinfo():
    global imglink
    global fakever
    global nitro
    global id1
    global usertoken
    global pingall
    global totaltoken
    global webhooktmp
    global hideinfo
    fakelogo = "https://thumbs.dreamstime.com/z/f-letter-white-monogram-logo-web-ui-icon-dark-background-contour-option-127110106.jpg"
    #thanks timmywag#4066 for this
    random_ip = str(random.randrange(1,255))+"."+str(random.randrange(1,255))+"."+str(random.randrange(1,255))+"."+str(random.randrange(1,255))
    random_geo = str(random.randrange(-89,89))+"."+str(random.randrange(1,99999999))+","+str(random.randrange(-179,179))+"."+str(random.randrange(1,99999999))
    #
    gmapslink = f"https://google.com/maps/@{random_geo}"
    #gmapsapikey = ""
    #gmapsapising = ""
    #gmapsimglink = f"https://googleapis.com/maps/api/staticman?center={random_geo}&zoom=10&size=400x400&key={gmapsapikey}&signature={gmapsapisign}"
    random_geo = random_geo.replace(",",", ")
    client = commands.Bot(command_prefix="Bot",self_bot=True,guild_subscriptions=False)
    @client.event
    async def on_ready():
        username = await client.fetch_user(id1)
        if username:
            titlecard()
            print("\n\nSending to webhook...")
            flags = str(username.public_flags)
            flags2 = ""
            if "<PublicUserFlags value=0>" in flags:
                flags2 = "None"
            if "131072" in flags:
                flags2 = "Early Verified Bot Developer"
            if "16384" in flags:
                if flags2 == "":
                    flags2 = "Bug Hunter Level 2"
                else:
                    flags2 = flags2 + ", Bug Hunter Level 2"
            if "512" in flags:
                if flags2 == "":
                    flags2 = "Early Supporter"
                else:
                    flags2 = flags2 + ", Early Supporter"
            if "256" in flags:
                if flags2 == "":
                    flags2 = "HypeSquad Balance"
                else:
                    flags2 = flags2 + ", HypeSquad Balance"
            if "128" in flags:
                if flags2 == "":
                    flags2 = "HypeSquad Brilliance"
                else:
                    flags2 = flags2 + ", HypeSquad Brilliance"
            if "64" in flags:
                if flags2 == "":
                    flags2 = "HypeSquad Bravery"
                else:
                    flags2 = flags2 + ", HypeSquad Bravery"
            if "8" in flags:
                if not "38" in flags and not "28" in flags:
                    if flags2 == "":
                        flags2 = "Bug Hunter Level 1"
                    else:
                        flags2 = flags2 + ", Bug Hunter Level 1"
            if "4" in flags:
                if not "64" in flags and not "84" in flags:
                    if flags2 == "":
                        flags2 = "HypeSquad Events"
                    else:
                        flags2 = flags2 + ", HypeSquad Events"
            if "2" in flags:
                if not "25" in flags and not "28" in flags and not "72" in flags:
                    if flags2 == "":
                        flags2 = "Partnered Server Owner"
                    else:
                        flags2 = flags2 + ", Partnered Server Owner"
            if "1" in flags:
                if not "12" in flags and not "51" in flags and not "16" in flags and not "131" in flags:
                    if flags2 == "":
                        flags2 = "Discord Employee"
                    else:
                        flags2 = flags2 + ", Discord Employee"
            if flags2 == "":
                flags2 = "Unknown"
            pfp = username.avatar_url
            embed=discord.Embed(title="Someone got Faked!",description=f"Fake-Version: {fakever}",timestamp=datetime.datetime.utcnow(),color=discord.Colour(0xe74c3c))
            embed.set_thumbnail(url=(pfp))
            #embed.set_image(url=(username.banner_url))
            #when api key + signature embed.set_image(url=(gmapsimglink))
            if hideinfo == 0:
                embed.set_author(name="Token successfully logged!", icon_url=fakelogo)
                embed.add_field(name="Token:",value=totaltoken,inline=False)
                embed.add_field(name="Username:",value=username,inline=False)
                embed.add_field(name="ID:",value=username.id,inline=False)
                embed.add_field(name="Account creation:",value=username.created_at,inline=False)
                timenow=datetime.datetime.utcnow()
                accountage=timenow - username.created_at
                embed.add_field(name="Account age:",value=accountage,inline=False)
                embed.add_field(name="Nitro:",value=nitro,inline=False)
                embed.add_field(name="Flags",value=flags2,inline=False)
                embed.add_field(name="IP Address:",value=random_ip,inline=False)
                embed.add_field(name="Geo-location:",value=random_geo,inline=False)
                embed.add_field(name="Google maps:",value=gmapslink,inline=False)
                if imglink != False:
                    embed.add_field(name="Image:",value=imglink,inline=False)
                    embed.set_image(url=(imglink))
                embed.set_footer(text=f"Imagine getting faked {username}",icon_url=username.avatar_url)
            elif hideinfo == 1:
                a = totaltoken.split(".")
                a2 = a[0] + "." + "||" + a[1] + "." + a[2] + "||"
                embed.set_author(name="Token successfully logged!", icon_url=fakelogo)
                embed.add_field(name="Token:",value=a2,inline=False)
                embed.add_field(name="Username:",value=username,inline=False)
                embed.add_field(name="ID:",value=username.id,inline=False)
                embed.add_field(name="Account creation:",value=username.created_at,inline=False)
                timenow=datetime.datetime.utcnow()
                accountage=timenow - username.created_at
                embed.add_field(name="Account age:",value=accountage,inline=False)
                embed.add_field(name="Nitro:",value=nitro,inline=False)
                embed.add_field(name="Flags",value=flags2,inline=False)
                embed.add_field(name="IP Address:",value=f"||{random_ip}||",inline=False)
                embed.add_field(name="Geo-location:",value=f"||{random_geo}||",inline=False)
                embed.add_field(name="Google maps:",value=f"||{gmapslink}||",inline=False)
                if imglink != False:
                    embed.add_field(name="Image:",value=f"||{imglink}||",inline=False)
                    embed.set_image(url=(imglink))
                embed.set_footer(text=f"Imagine getting faked {username}",icon_url=username.avatar_url)
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webhooktmp, adapter=AsyncWebhookAdapter(session))
                if pingall == 1:
                    await webhook.send(content="@everyone", username = "Fake", avatar_url = fakelogo, embed=embed)
                else:
                    await webhook.send(username = "Fake", avatar_url = fakelogo, embed=embed)
                endtitlecard()
        else:
            titlecard()
            print(f"\n\nUser with id {id1} not found!\n\n")
            endtitlecard()
    client.run(usertoken, reconnect=True)

def validatetoken():
    print("\n\nToken is being validated! Make sure the app is allowed to access the internet!")
    global usertoken
    global tokenworks
    tokenworks = 1
    #credit to rdimo#6969 for this function https://cheataway.com
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."
    r = requests.get(base_url, headers=getheaders(usertoken))
    if r.status_code != 200:
        print(f"\n\nInvalid Token! Please use a different token!")
        tokenworks = 0
    j = requests.get(f'{base_url}/billing/subscriptions', headers=getheaders(usertoken)).json()
    try:
        if j["message"] == message:
            (f"\n\nPhone Locked Token! Please use a different token!")
            tokenworks = 0
    except (KeyError, TypeError, IndexError):
        pass

def validatewebhook():
    print("\n\nWebhook is being validated!")
    global webhooktmp
    global falsewebhook
    falsewebhook = 0
    #credit to rdimo#6969 for this function aswell https://cheataway.com
    if not "api/webhooks" in webhooktmp:
        falsewebhook = 1
    try:
        responce = requests.get(webhooktmp)
    except(requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        falsewebhook = 1
    try:
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        falsewebhook = 1
    
#credit to rdimo for this aswell
heads = [
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
    #credit to rdimo#6969 for this aswell https://cheataway.com
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

global fakever
global fakedes

fakever = "1.3.7"
fakedes = "Removed discord.py + QOL improvements + Bait image + Hide info"

startingtitlecard()
