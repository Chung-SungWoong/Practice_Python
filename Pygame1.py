"""
핀볼 게임 이식하기 processing -> Python
"""

import pygame

Background = (0,0,0)
window_width = 500
window_height = 700

def runGame():
    global gamepad,clock

    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True

        gamepad.fill(Background)
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()


def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('Pin ball')
    clock = pygame.time.Clock()

initGame()
runGame()


