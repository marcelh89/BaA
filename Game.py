# !/usr/bin/python
'''
Created on Thu Apr 4 08:37 2013

@author: marcel
'''
#IMPORT & INITIALIZE
import pygame, random
from pygame.locals import *
from lib.Player import Player
from lib.Arrow import Arrow
from lib.Balloon import Balloon


def main():
    #initialize screen
    pygame.init()

    #DISPLAY
    size = (width, height) = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Bow & Arrows')
    pygame.mouse.set_visible(1)
    bg = pygame.Surface(size)
    bg = bg.convert()
    bg.fill((0, 128, 1))

    #ENTITIES
    #later get hscr from sqlitedb
    scr = 0
    hscr = 0
    keepgoing = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 20)

    score = font.render("Score " + str(scr), 1, (10, 10, 10))
    score_pos = (10, 5)
    highscore = font.render("High Score " + str(hscr), 1, (10, 10, 10))
    highscore_pos = (10, 20)

    level = 1
    levels = {1: 'Target Practice', 2: 'More Target Practise', 3: 'Bouncing Bubbles', 4: 'Slimed', 5: 'Bulls Eye',
              6: 'Fireballs'
        , 7: 'Unfriedly Skies', 8: 'Whrrrrrrrrr'}
    leveltext = font.render("Level " + str(level), 1, (10, 10, 10))
    level_pos = (300, 5)
    levelstext = font.render(levels.get(level), 1, (10, 10, 10))
    levels_pos = (300, 20)

    arrows_left = 30
    arrowstext = font.render(str(arrows_left), 1, (10, 10, 10))
    arrows_pos = (600, 20)

    player = Player()
    level_finished = 1

    #renderer for sprites
    playersprite = pygame.sprite.RenderUpdates()
    playersprite.add(player)

    collides = pygame.sprite.RenderUpdates()

    arrows = pygame.sprite.RenderUpdates()
    monsters = pygame.sprite.RenderUpdates()

    #ACTION
    while keepgoing:

        #check for gameover
        #if(no_arrows_left <= 0 or hit_by_enemy)

        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                keepgoing = False
                break
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    keepgoing = False
                    break
            if event.type == MOUSEBUTTONDOWN:
                print 'mousebuttondown'

            if event.type == MOUSEBUTTONUP:
                print 'mousebuttonup'

                if (player.is_arrowed and player.is_targeting):
                    player.shoot()
                    arrows.add(Arrow())

            if pygame.mouse.get_pressed()[0]:
                print 'leftbutton'
                if (player.is_arrowed):
                    player.target()

            if pygame.mouse.get_pressed()[2]:
                print 'rightbutton'
                player.reload()

            #collisiondetection
            for m in monsters:
                for a in arrows:
                    #inaccurate for balloons - subtract 70 see Arrow init
                    if pygame.sprite.collide_rect(a, m):
                        #if m.rect.collidepoint(a.get_x, a.get_y):
                        m.set_shot()

        time = pygame.time.get_ticks()

        monsters.draw(screen)
        monsters.update()
        arrows.draw(screen)
        arrows.update()
        playersprite.draw(screen)
        playersprite.update()

        pygame.display.flip()
        screen.blit(bg, (0, 0))
        screen.blit(score, score_pos)
        screen.blit(highscore, highscore_pos)
        screen.blit(leveltext, level_pos)
        screen.blit(levelstext, levels_pos)
        screen.blit(arrowstext, arrows_pos)

        clock.tick(60)

        #arrows out of border deletion
        for i in arrows:
            if i.get_x() > 1000:
                arrows.remove(i)

        #monsters out of boarder deletion
        for m in monsters:
            if m.get_y() > 1000 and m.get_shotstatus() == 1:
                monsters.remove(m)

        if len(monsters) == 0:
            #level+=1
            level_finished = 1

        #levelgeneration only once
        if level_finished:

            level_finished = 0

            if level == 1:
                #15 red balloons
                monsters.add(Balloon('RED', x * 30 + 300, 600) for x in range(15))
            elif level == 2:
                pass
                #3 yellow
                #11 red
            elif level == 3:
                pass
            elif level == 4:
                pass
            elif level == 5:
                pass
            elif level == 6:
                pass
            elif level == 7:
                pass
            elif level == 8:
                pass
            elif level == 9:
                pass


if __name__ == '__main__':
    main()
