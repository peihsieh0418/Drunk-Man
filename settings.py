# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:46:10 2020

@author: user
"""
import random 
#setting
class Settings():
    
    def __init__(self):
        

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,250,250)

        
        self.person_speed_factor = 10
    


        self.alien_timer = 0 
        self.alien_count = 100 
        self.alien_spawn_time = random.uniform(1,2) 
        self.alien_cur_count = 0 

        self.water_timer = 0  
        self.water_count = 100
        self.water_spawn_time = random.uniform(1,1.5)
        self.water_cur_count = 0 

        self.potion_timer = 0      
        self.potion_count = 50 
        self.potion_spawn_time = random.uniform(1,2)
        self.potion_cur_count = 0 
        
        self.toxic_timer = 0 
        self.toxic_count = 50
        self.toxic_spawn_time = random.uniform(1,2) 
        self.toxic_cur_count = 0 

        
        
        self.score = 0 
        self.add_score = 20 
        self.add_score2 = 10
        self.add_score3 = -20
        
        self.is_play=True
