import click

from utils import Player


def run():
    Player.getGame().mixer.pause()
