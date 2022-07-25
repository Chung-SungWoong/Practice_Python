"""
간단한 슈팅게임 만들기1
"""
from time import clock_getres
import pygame

BLACK = (0,0,0)
pad_width = 480
pad_height = 640

def runGame():
    global gampad, clock

    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneFale = True
        
        gamepad.fill(BLACK)
        pygame.display.update()
        click.tick(60)
    
    pygame.quit()

def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('MyGalaga')
    clock = pygame.time.Clock()

initGame()
runGame()