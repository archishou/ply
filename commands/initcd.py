import click
from os.path import expanduser
import os


def run():
    path = expanduser("~") + "/ply/config"
    try:
        os.makedirs(path)
    except OSError:
        pass
    click.echo(path)
    createFiles()


def createFiles():
    file = open(expanduser("~") + "/ply/config/path.txt", "w+")
    file.write(os.getcwd())
    file.close()
