import json

server = "25.34.159.172"  # Input server IP of you hamachi host here
# server = "127.0.0.1"  # Localhost
port = 5555


# width = 1280
# height = 720
width = 1536
height = 864
# width = 1920
# height = 1080
# width = 2560
# height = 1440
maxPlayers = 15


def update_setting():
    global width, height
    with open("config.json", "r") as f:
        config = json.load(f)
        width = config["width"]
        height = config["height"]


def scale(length):
    return length*width/1536


update_setting()
