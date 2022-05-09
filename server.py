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
serverstarttime = time.time()
print("Waiting for a connection, Server Started")
maxPlayers = 10

players = []
for i in range(maxPlayers):
    players.append(Player(i+1, 30, 30, 50, 34, (0, 0, 0), f"Player{i+1}"))

monster = []
monster.append(Monster(time.time(), serverstarttime))

currentPlayer = {}


def threaded_client(conn, player):
    """
    start thread for each client to receive data from server

    Args:
        conn (socket): connection from client
        player (int): id of player
    """
    print(player, "connected")
    global currentPlayer
    conn.send(pickle.dumps((players[player], time.time())))

    reply = ""
    while True:
        attacksuccess = 0
        try:
            data = pickle.loads(conn.recv(65536))
            if data.atk != 0:
                if data.atk == 9999:  # player hp - 1
                    monster.pop(0)
                    monster.append(Monster(time.time(), serverstarttime))
                elif monster[0].weakskill[0] == data.atkelement:
                    monster[0].weakskill.pop(0)
                    data.atksuccess = 45
                    attacksuccess = 45
                    if len(monster[0].weakskill) == 0:
                        monster.pop(0)
                        monster.append(Monster(time.time(), serverstarttime))
                data.atk = 0
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                reply = {
                    "playeratksuccess": attacksuccess,
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
