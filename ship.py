# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:50:02 2020

@author: user
"""
import pygame

class Person():
    
    def __init__(self ,game_settings,screen):
        
        self.screen = screen
        self.game_settings=game_settings
        self.image = pygame.image.load("person.png")
        self.rect =self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx

        #add a switch
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

 

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.game_settings.person_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.game_settings.person_speed_factor
        
        if self.moving_up and self.rect.top >0:
            self.rect.centery -= self.game_settings.person_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.game_settings.person_speed_factor
        

    def blitme(self):
        
        self.screen.blit(self.image , self.rect)
        