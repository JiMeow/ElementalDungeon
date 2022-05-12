from setting import *

from threading import *
from player import Player
from monster import Monster
import socket
import json
import time
import pickle
import pygame
import hashlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(20)
monstercnt = 1
serverstarttime = time.time()
print("Waiting for a connection, Server Started")

players = []
for i in range(maxPlayers):
    players.append(Player(i+1, 30, 30, 50, 34, (0, 0, 0), f"Player{i+1}"))

monster = []
monster.append(Monster(time.time(), serverstarttime, monstercnt))

currentPlayer = {}
scoreboard = {}


def threaded_client(conn, player):
    """
    start thread for each client to receive data from server

    Args:
        conn (socket): connection from client
        player (int): id of player
    """
    print(player, "connected")
    global currentPlayer
    global scoreboard
    global serverstarttime
    global monstercnt
    conn.send(pickle.dumps((players[player], time.time())))
    reply = ""
    while True:
        attacksuccess = 0
        timeinvokedelay = 0
        try:
            data = pickle.loads(conn.recv(65536))
            monster[0].update(1/60)
            if data.atk != 0 and monster[0].tempx < width:
                if data.atk == 9999:  # player hp - 1
                    monster.pop(0)
                    serverstarttime = time.time()
                    monstercnt = 1
                    for name in scoreboard:
                        scoreboard[name] = [0, data.id]
                    monster.append(
                        Monster(time.time(), serverstarttime, monstercnt))
                elif sorted(monster[0].weakskill[0]) == sorted(data.atkelement):
                    if data.name not in scoreboard:
                        scoreboard[data.name] = [0, data.id]
                    scoreboard[data.name][0] += 1
                    monster[0].weakskill.pop(0)
                    data.atksuccess = 45
                    attacksuccess = 45
                    if len(monster[0].weakskill) == 0:
                        monster.pop(0)
                        monstercnt += 1
                        monster.append(
                            Monster(time.time(), serverstarttime, monstercnt))
                else:
                    data.timeinvokedelay = 45
                    timeinvokedelay = 45
                    print("Invoke Fail")

            data.atk = 0
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                reply = {
                    "playerreturn": {
                        "playeratksuccess": attacksuccess,
                        "timeinvokedelay": timeinvokedelay,
                        "scoreboard": scoreboard
                    },
                    "players": players,
                    "status": currentPlayer,
                    "monster": monster[0]
                }
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break

    print(player, "disconnected")
    currentPlayer[player] = 0
    scoreboard.pop(players[player].name)
    players[player].x = 30
    players[player].y = -100
    players[player].rect = pygame.Rect(30, -100, 54, 30)
    conn.close()


def main():
    """
    start server wait for client to connect
    and check number of player and decide 
    which client will be which id
    """
    for i in range(maxPlayers):
        currentPlayer[i] = 0
    idx = 0
    while True:
        conn, addr = s.accept()
        for i in range(maxPlayers):
            if currentPlayer[i] == 0:
                currentPlayer[i] = 1
                idx = i
                break
        thread = Thread(target=threaded_client, args=(conn, idx))
        thread.start()


main()
