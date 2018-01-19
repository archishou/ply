import click
from utils import application
from utils import Player
import pygame


def run(song):
    click.echo("Playing: " + song)
    playSong(application.getMusicFolder() + "/" + song + ".wav")


def playSong(song):
    Player.getGame().mixer.music.load(song)
    Player.getGame().mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
