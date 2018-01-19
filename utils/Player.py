import pygame


class Player:

    game = pygame

    def __init__(self):
        Player.game.mixer.init()

    def getGame(self):
        return Player.game
