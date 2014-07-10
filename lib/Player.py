# !/usr/bin/python
'''
Created on Wed May  9 12:32:20 2012

@author: marcel
'''
#IMPORT & INITIALIZE
import pygame, random
from pygame.sprite import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        Sprite.__init__(pygame.sprite.Sprite)
        #bowman simply standing
        self.image = pygame.image.load("./sprites/hero_without_arrow.png")
        self.rect = self.image.get_rect()
        self.is_arrowed = 0
        self.is_targeting = 0

    def update(self):
        pos = pygame.mouse.get_pos()

        #left and right borders
        if pos[0] < 100:
            self.rect.centerx = 100
            self.rect.centery = pos[1]
        if pos[0] > 750:
            self.rect.centerx = 750
            self.rect.centery = pos[1]
        #top and bottom borders
        if pos[1] < 100:
            self.rect.centery = 100
            self.rect.centerx = pos[0]
        if pos[1] > 550:
            self.rect.centery = 550
            self.rect.centerx = pos[0]
        #corners(top-left, top-right, bottom-left, bottom-right)
        if pos == (100, 100) or pos == (750, 100) or pos == (100, 550) or pos == (750, 550):
            self.rect.center = pos

        if pos[0] in range(101, 749) and pos[1] in range(101, 549):
            self.rect.center = pos

    def reload(self):
        #bowman is armed
        self.image = pygame.image.load("./sprites/hero_stand.png")
        self.is_arrowed = 1

    def target(self):
        #bowman is targeting
        self.image = pygame.image.load("./sprites/hero_armed.png")
        self.is_targeting = 1

    def shoot(self):
        #bowman after shoot
        self.image = pygame.image.load("./sprites/hero_without_arrow.png")
        self.is_arrowed = 0
        self.is_targeting = 0

    def get_rect(self):
        return self.rect