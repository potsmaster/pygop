import pygop

pygop = pygop.pygop()
pygop.printHouseInfoTable()

# pygop.setBulbLevelByDid(216401854199230426, 1, 0)
# pygop.setRoomLevelByRid(2, 1, 0)
#pygop.setBulbLevelByName('Desk Light', 1, 100)

pygop.setRoomLevelByName('Living Room', 1, 0)
pygop.setRoomLevelByName('Bedroom',0, 1)
pygop.setRoomLevelByName('Hall',0, 1)
