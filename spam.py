import requests
import time

# BanSpam! - up
BanSpamUpChannel = "https://discord.com/api/v9/channels/1063531754431983709/messages"

# iHemo - worlds
iHemoWorldsChannel = "https://discord.com/api/v9/channels/734717853965615124/messages"

# iHemo - items
iHemoItemsChannel = "https://discord.com/api/v9/channels/900836866373333052/messages"

worldPromoMessage = {
    'content': "Selling multiple worlds:\n- **EGGTRY** (Gacha Egg World) for 50 DLS\n- **AUDIORACK** for 20 DLS\n- **BUYSTARFIREBLOCKS** for 20 DLS\n\nDM either <@209971916268634112> or <@1130810950925156422>"
}

itemPromoMessage = {
    'content': "Selling multiple items in **FOXQUEST**:\n- SELL Royal Cresent Charm 650 WLS\n- SELL Pink Fedora 8 WLS\n- SELL Amethyst Choker 80 WLS\n- SELL Heartbow 70 WLS\n- SELL Lunar Drum 70 WLS\n- SELL Tied-up Buns 30 WLS\n- SELL Pink Teeny Angel Wings 105 WLS\n- SELL Shifty Block 8 WLS EACH\n- SELL Dragon Hand 40 WLS\n- SELL Super-Dragon Mask 5 WLS\n- SELL Prehistoric Dragon Claw 5 WLS\n- SELL Star Dragon Claw 5 WLS\n- SELL Emergency Dragon Claw 5 WLS\n- SELL Gourmet Dragon Claw 4 WLS\n- SELL Mah-Kah-Ron Hat 110 WLS\n- SELL Bunny Slippers 550 WLS\n- SELL Loafers 95 WLS\n- SELL Flower Pot 750 WLS\n- SELL Builder's Lock 30 WLS\n- SELL Mountain Dire Wolf 320 WLS\n- SELL TK69's Mystical Etherboard 240 WLS\n\nALL GO TO **FRP** or **FOXQUEST**"
}

notif = {
    'content': "Sent a message promoting your worlds at https://discord.com/channels/571992648190263317/734717853965615124 and at https://discord.com/channels/571992648190263317/900836866373333052"
}

header = {
    'authorization': "MTEzMDgxMDk1MDkyNTE1NjQyMg.G2oGd_.91tFou7z97ZbDTsVVLiklUpyrDeW4wWSFcvYZgQ"
}

# promoting worlds
r = requests.post(iHemoWorldsChannel, data=worldPromoMessage, headers=header)

# promoting items
r = requests.post(iHemoItemsChannel, data=itemPromoMessage, headers=header)

# notif
r = requests.post(BanSpamUpChannel, data=notif, headers=header)

print("sent multiple messages.")
time.sleep(7800)
