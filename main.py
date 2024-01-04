import pygame
import os
import sys
from button import Button


FPS = 50
pygame.init()

pygame.display.set_caption('menu')
size = WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode(size)
but_sound = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')

# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     # если файл не существует, то выходим
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     return image


# def start_screen():
#     intro_text = ["СТЕПАН МЕХАНИК-ПЕРЕКУПЩИК",
#                   "ВЕРСИЯ 347593459874982"
#                   ]
#

clock = pygame.time.Clock()
    # fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    # screen.blit(fon, (0, 0))
    # font = pygame.font.Font(None, 30)
    # text_coord = 30
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('black'))
    #     intro_rect = string_rendered.get_rect()
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     intro_rect.x = 300
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)
running = True
green_buttoN = Button(WIDTH/2-(252/2), 200, 100, 74, '', 'knopka.png', 'supermegatreckotkotorogovsevahue.mp3')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(FPS)


# start_screen()
