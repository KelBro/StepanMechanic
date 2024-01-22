import pygame
from button import ImageButton
from Sprites import SpriteTool, Cursor


pygame.init()  # инициализируем PyGame

WIDTH = 800  # ширина экрана
HEIGHT = 600  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана
pygame.display.set_caption("StepanMechanic")

# Фон меню
fon = pygame.image.load('data/fon.jpg').convert_alpha()
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
fon.set_colorkey((255, 255, 255))
fon_scene2 = pygame.image.load('data/garage.jpg').convert_alpha()
fon_scene2 = pygame.transform.scale(fon_scene2, (WIDTH, HEIGHT))
fon_scene2.set_colorkey((255, 255, 255))
# Фон секретной концовки
game_over_fon = pygame.image.load('data/game_over.jpg').convert_alpha()
game_over_fon = pygame.transform.scale(game_over_fon, (WIDTH, HEIGHT))
game_over_fon.set_colorkey((255, 255, 255))

"""Создание кнопок"""

# Кнопки в главном меню
play_button = ImageButton(WIDTH/2 - (350/2), 225, 350, 122, "Play", "btn01.png", "btn02.png", "click.mp3")
levels_button = ImageButton(WIDTH/2 - (350/2), 350, 350, 122, "Levels", "btn01.png", "btn02.png", "click.mp3")
out_button = ImageButton(WIDTH - 252, 500, 252, 100, "Выйти", "btn01.png", "btn02.png", "click.mp3")
# Кнопки для концовки
menu_button = ImageButton(WIDTH/4.5 - (350/2), 500, 350, 100, "Главное меню", "btn01.png", "btn02.png", "click.mp3")
pause_menu_button = ImageButton(WIDTH//3 - 40, HEIGHT // 2, 350, 100, "Главное меню", "btn01.png", "btn02.png", "click.mp3")
continue_menu_button = ImageButton(WIDTH//3 - 40, HEIGHT // 2 - 120, 350, 100, "Вернуться", "btn01.png", "btn02.png", "click.mp3")
out1_button = ImageButton(WIDTH - 252, 500, 252, 100, "Выйти", "btn01.png", "btn02.png", "click.mp3")

"""Спрайты"""

# Группы спрайтов

tool_group = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()
all_sprites_tools = pygame.sprite.Group()


# Спрайты инструментов

# Губка
sponge = SpriteTool('sponge.png', 20, 50, 'sponge', (110, 110), tool_group, all_sprites_tools)
# Вытягиватель вмятин
dent_puller = SpriteTool('dent_puller.png', 650, 25, 'dent_puller', (140, 140), tool_group, all_sprites_tools)
# Краска
f_spray_paint = SpriteTool('f_spray_paint.png', 630, 290, 'f_spray_paint', (170, 170), tool_group, all_sprites_tools)
# Клей
glue = SpriteTool('glue.png', 650, 170, 'glue', (150, 150), tool_group, all_sprites_tools)
# Мастерок
trowel = SpriteTool('trowel.png', 15, 175, 'trowel', (120, 120), tool_group, all_sprites_tools)

cursor = Cursor(0, 0, cursor_group, all_sprites_tools)

current_scene = None