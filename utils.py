def getDataFromServer(network, player, allp=[], status={}, monster=[]):
    while(len(allp) != 0):
        allp.pop(0)
    data = network.send(player)
    allp += data["players"]
    for i in range(10):
        status[i] = data["status"][i]
    while(len(monster) != 0):
        monster.pop(0)
    monster.append(data["monster"])
    return allp, status, monster


def setdatafromserver(allp, status, monster, tempallp, tempstatus, tempmonster):
    while(len(allp) != 0):
        allp.pop(0)
    for i in tempallp:
        allp.append(i)
    for i in tempstatus:
        status[i] = tempstatus[i]
    while(len(monster) != 0):
        monster.pop(0)
    monster.append(tempmonster[0])


def redrawWindow(layout, map,  player, allp, status):
    layout.updatemap(map)
    layout.updateplayer(player)
    layout.updateallplayer(allp)
    layout.updatestatus(status)
    layout.draw()
