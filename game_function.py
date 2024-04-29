# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:16:24 2020

@author: user
"""


import sys
import pygame
from alien import Alien
from alien import Water
from alien import Potion
from alien import Toxic


def check_keydown_event(event , ai_settings , screen , ship ):
    if event.key==pygame.K_ESCAPE:
        pygame.quit()
    
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True             
    
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True  
    elif event.key==pygame.K_UP:
        ship.moving_up=True  
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True  


        
        
def check_keyup_event(event, ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False
        
#check key event
def check_events(ai_settings , screen , ship ):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #press esc to quit
        elif event.type==pygame.KEYDOWN:
            check_keydown_event(event , ai_settings , screen , ship )
            
        elif event.type==pygame.KEYUP:
            check_keyup_event(event, ship)

def update_screen(ai_settings,screen,ship,aliens,waters,potions,toxics,scores):
    screen.fill(ai_settings.bg_color)#fill the screen


    
    for alien in aliens.sprites():
        alien.blitme()
    for water in waters.sprites():
        water.blitme()
    for potion in potions.sprites():
        potion.blitme()
    for toxic in toxics.sprites():
        toxic.blitme()        

   
    scores.blitme()
        
    ship.blitme()        
    pygame.display.flip()


        
        
def spawn_alien(ai_settings ,screen,aliens,waters,potions,toxics,clock):
  
    if clock.get_fps()>0: 
        if  ai_settings.alien_cur_count < ai_settings.alien_count:
            ai_settings.alien_timer += (1.0 /clock.get_fps())
            if ai_settings.alien_timer > ai_settings.alien_spawn_time :
                alien = Alien(ai_settings , screen )
                aliens.add(alien)
                ai_settings.alien_timer = 0
                ai_settings.alien_cur_count += 1 
    
    if clock.get_fps()>0: 
        if  ai_settings.water_cur_count < ai_settings.water_count:
            ai_settings.water_timer += (1.0 /clock.get_fps())
            if ai_settings.water_timer > ai_settings.water_spawn_time :
                water = Water(ai_settings , screen )
                waters.add(water)
                ai_settings.water_timer = 0
                ai_settings.water_cur_count += 1 
  
    if clock.get_fps()>0: 
        if  ai_settings.potion_cur_count < ai_settings.potion_count:
            ai_settings.potion_timer += (1.0 /clock.get_fps())
            if ai_settings.potion_timer > ai_settings.potion_spawn_time :
                potion = Potion(ai_settings , screen )
                potions.add(potion)
                ai_settings.potion_timer = 0
                ai_settings.potion_cur_count += 1 
                
    if clock.get_fps()>0: 
        if  ai_settings.toxic_cur_count < ai_settings.toxic_count:
            ai_settings.toxic_timer += (1.0 /clock.get_fps())
            if ai_settings.toxic_timer > ai_settings.toxic_spawn_time :
                toxic = Toxic(ai_settings , screen )
                toxics.add(toxic)
                ai_settings.toxic_timer = 0
                ai_settings.toxic_cur_count += 1 

def check_collider(aliens,waters,potions,toxics, ship ,ai_settings):

    if pygame.sprite.spritecollide(ship,aliens,aliens ):
        ai_settings.score += ai_settings.add_score
   
    if pygame.sprite.spritecollide(ship,waters,waters ):
        ai_settings.score += ai_settings.add_score2
  
    if pygame.sprite.spritecollide(ship,potions,potions ):
        ai_settings.score += ai_settings.add_score3
  
    if pygame.sprite.spritecollideany(ship,toxics):
        ai_settings.is_play= False
        pygame.quit()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        