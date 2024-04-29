# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:47:41 2020

@author: user
"""


import sys
import pygame
from settings import Settings
from ship import Person
import game_function as gf
from pygame.sprite import Group
from word import Word


ai_settings=Settings()

def run_game():
    
    pygame.init()
    
    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("DRUNK MAN")
    
 
    ship=Person(ai_settings,screen)

    aliens = Group() 
    waters = Group()
    potions = Group()
    toxics = Group()
    
    clock = pygame.time.Clock()
    scores = Word(ai_settings , screen)
    
    while ai_settings.is_play :
        clock.tick(60)
        gf.check_events(ai_settings , screen , ship  )
        ship.update()#update ship moving        
        aliens.update()
        waters.update()
        potions.update()
        toxics.update()

        gf.spawn_alien(ai_settings ,screen,aliens,waters,potions,toxics,clock)
        gf.check_collider (aliens,waters,potions,toxics, ship ,ai_settings)

        gf.update_screen(ai_settings,screen,ship,aliens,waters,potions,toxics,scores)

   




run_game()

