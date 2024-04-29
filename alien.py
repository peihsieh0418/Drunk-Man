# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:41:43 2020

@author: user
"""



import pygame
from pygame.sprite import Sprite 
import random 

class Alien(Sprite):
    
    def __init__(self, ai_settings, screen):
        
        super(Alien , self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
       
        self.image = pygame.image.load("beer.png")
        
        
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,screen.get_rect().width-25)
        self.rect.centery = random.randint(0,400)
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += random.uniform(0.5,2)
        self.rect.y = self.y 

    def blitme(self):
        self.screen.blit(self.image , self.rect)
        
class Water(Sprite):
    
    def __init__(self, ai_settings, screen):
        
        super(Water , self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
       
        self.image = pygame.image.load("water.png")
        
        
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,screen.get_rect().width-25)
        self.rect.centery = random.randint(0,400)
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += random.uniform(0.5,2)
        self.rect.y = self.y 

    def blitme(self):
        self.screen.blit(self.image , self.rect)
        
        
class Potion(Sprite):
    
    def __init__(self, ai_settings, screen):
        
        super(Potion , self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
       
        self.image = pygame.image.load("potion.png")
        
        
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,screen.get_rect().width-25)
        self.rect.centery = random.randint(200,screen.get_rect().height)
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += random.uniform(0.5,2)
        self.rect.y = self.y 

    def blitme(self):
        self.screen.blit(self.image , self.rect)

class Toxic(Sprite):
    
    def __init__(self, ai_settings, screen):
        
        super(Toxic , self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
       
        self.image = pygame.image.load("toxic.png")
        
        
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,screen.get_rect().width-25)
        self.rect.centery = random.randint(200,screen.get_rect().height)
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= random.uniform(1,2.5)
        self.rect.y = self.y 

    def blitme(self):
        self.screen.blit(self.image , self.rect)