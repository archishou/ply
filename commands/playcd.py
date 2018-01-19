import click
from utils import application
import pygame


def run(song):
    click.echo("Playing: " + song)
    playSong(application.getMusicFolder() + "/" + song + ".wav")


def playSong(song):
    pygame.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
