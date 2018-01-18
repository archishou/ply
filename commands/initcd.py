import click
from os.path import expanduser
import os


def run():
    path = expanduser("~") + "/ply"
    try:
        os.makedirs(path)
    except OSError:
        pass
    click.echo(path)
