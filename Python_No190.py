"""
간단한 슈팅게임 만들기 3
"""

import random
import pygame

BLACK = (0,0,0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 38
enemy_width = 26
enemy_height = 20

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))


def runGame():
    global gampad, clock, fighter, enemy

    #전투기 초기 위치 설정하기
    x = int(pad_width*0,45)
    y = int(pad_height*0.9)
    x_change = 0

    # 적 초기 위치 설정
    enemy_x = random.randrange(0,pad_width-enemy_width)
    enemy_y = 0
    enemy_speed = 3

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
        
        gamepad.fill(BLACK)

        #전투기의 위치를 재조정
        x += x_change
        if x <0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width

        drawObject(fighter,x,y)

        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0,pad_width-enemy_width)
        
        drawObject(enemy,enemy_x,enemy_y)

        pygame.display.update()
        click.tick(60)
    
    pygame.quit()

def initGame():
    global gamepad, clock, fighter, enemy

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    clock = pygame.time.Clock()

initGame()
runGame()
