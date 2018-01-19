from os.path import expanduser


def getApplicationFolder():
    return expanduser("~") + "/ply/config"


def getMusicFolder():
    file = open(getApplicationFolder() + "/path.txt", "r")
    return file.read()

