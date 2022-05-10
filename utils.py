from setting import *


def getDataFromServer(network, player, allp=[], status={}, monster=[], playerreturn={}):
    while(len(allp) != 0):
        allp.pop(0)
    data = network.send(player)
    allp += data["players"]
    for i in range(maxPlayers):
        status[i] = data["status"][i]
    while(len(monster) != 0):
        monster.pop(0)
    monster.append(data["monster"])
    playerreturn["playeratksuccess"] = data["playerreturn"]["playeratksuccess"]
    playerreturn["timeinvokedelay"] = data["playerreturn"]["timeinvokedelay"]
    playerreturn["scoreboard"] = data["playerreturn"]["scoreboard"]
    # print(playerreturn)
    return allp, status, monster


def setdatafromserver(allp, status, monster, player, scoreboard, tempallp, tempstatus, tempmonster, playerreturn):
    while(len(allp) != 0):
        allp.pop(0)
    for i in tempallp:
        allp.append(i)
    for i in tempstatus:
        status[i] = tempstatus[i]
    while(len(monster) != 0):
        monster.pop(0)
    monster.append(tempmonster[0])
    player.atksuccess = max(
        playerreturn["playeratksuccess"], player.atksuccess)
    player.timeinvokedelay = max(
        playerreturn["timeinvokedelay"], player.timeinvokedelay)
    for name in playerreturn["scoreboard"]:
        scoreboard[name] = playerreturn["scoreboard"][name]


def redrawWindow(layout, map,  player, allp, status, monster, scoreboard):
    layout.updatemap(map)
    layout.updateplayer(player)
    layout.updateallplayer(allp)
    layout.updatestatus(status)
    layout.updatemonster(monster)
    layout.updatescoreboard(scoreboard)
    layout.draw()
