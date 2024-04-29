# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:46:08 2020

@author: user
"""

import pygame


class Button():
    def __init__(self,ai_setttings,screen,msg): 

        self.screen=screen
        self.screen_rect=screen.get_rect()  
        self.width,self.height=150,50  
        self.button_color=(72,61,150)  
        self.text_color=(255,255,255)  
        self.font=pygame.font.SysFont(None,40)     
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center  
        self.deal_msg(msg) 
  
    def deal_msg(self,msg):       

        self.msg_img=self.font.render(msg,True,self.text_color,self.button_color) 
        self.msg_img_rect=self.msg_img.get_rect()  
        self.msg_img_rect.center=self.rect.center  
  
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect) 
        self.screen.blit(self.msg_img,self.msg_img_rect)