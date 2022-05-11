import json

server = "25.34.159.172"  # Input server IP of you hamachi host here
# server = "127.0.0.1"  # Localhost
port = 5555
maxPlayers = 15

# width = 256
# height = 144

width = 1280
height = 720

# width = 1536
# height = 864

# width = 1960
# height = 1080


def scale(length):
    return length*width/1536
