# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:38:36 2020

@author: user
"""


import pygame

class Word():
    
    def __init__(self,ai_settings, screen ):
        
        self.ai_settings = ai_settings
        self.screen = screen

        self.font = pygame.font.SysFont("simhei",72)
        
    
    def blitme(self):

        self.text = self.font.render("SCORE "+str(self. ai_settings.score),True,(255,255,255),(0,250,250))

        self.screen.blit(self.text,(20,20))
