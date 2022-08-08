"""
핀볼 게임 이식하기 processing -> Python
"""

import pygame

Background = (0,0,0)
window_width = 500
window_height = 700
player_width = 10
player_height = 5

def DrawPlayer(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def runGame():
    global gamepad,clock, player

    x = int(window_width* 0.5)
    y = int(window_height*0.9)
    x_change = 0

    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
            
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gamepad.fill(Background)

        x += x_change
        if x < 0:
            x = 0
        elif x > window_width - player_width:
            x = window_width - player_width
        
        DrawPlayer(player,x,y)

        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()


def initGame():
    global gamepad, clock, player

    pygame.init()
    gamepad = pygame.display.set_mode((window_width,window_height))
    player = pygame.image.load('fighter.png')
    pygame.display.set_caption('Pin ball')
    clock = pygame.time.Clock()

initGame()
runGame()


