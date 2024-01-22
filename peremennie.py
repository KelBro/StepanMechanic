import pygame
from button import ImageButton
from Sprites import SpriteTool, Cursor, AnimatedSprite
from cars import Cars

pygame.init()  # инициализируем PyGame

WIDTH = 800  # ширина экрана
HEIGHT = 600  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана
pygame.display.set_caption("StepanMechanic")

"""Фоны"""

# Фон меню
fon = pygame.image.load('data/fon.jpg').convert_alpha()
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
fon.set_colorkey((255, 255, 255))
# Фон игры
fon_scene2 = pygame.image.load('data/garage.jpg').convert_alpha()
fon_scene2 = pygame.transform.scale(fon_scene2, (WIDTH, HEIGHT))
fon_scene2.set_colorkey((255, 255, 255))
# Фон секретной концовки
game_over_fon = pygame.image.load('data/game_over.jpg').convert_alpha()
game_over_fon = pygame.transform.scale(game_over_fon, (WIDTH, HEIGHT))
game_over_fon.set_colorkey((255, 255, 255))
# Фон лвлов
level_fon = pygame.image.load('data/fonlevels.PNG').convert_alpha()
level_fon = pygame.transform.scale(level_fon, (WIDTH, HEIGHT))
level_fon.set_colorkey((255, 255, 255))

"""Создание кнопок"""

# Кнопки в главном меню
play_button = ImageButton(WIDTH/2 - (350/2), 225, 350, 122, "Play", "btn01.png", "btn02.png", "click.mp3")
levels_button = ImageButton(WIDTH/2 - (350/2), 350, 350, 122, "Levels", "btn01.png", "btn02.png", "click.mp3")
out_button = ImageButton(WIDTH - 252, 500, 252, 100, "Выйти", "btn01.png", "btn02.png", "click.mp3")
# Кнопки для концовки
menu_button = ImageButton(WIDTH/4.5 - (350/2), 500, 350, 100, "Главное меню", "btn01.png", "btn02.png", "click.mp3")
out1_button = ImageButton(WIDTH - 252, 500, 252, 100, "Выйти", "btn01.png", "btn02.png", "click.mp3")
# Кнопки поворота машины
front_button = ImageButton(WIDTH * 1/8 - 15, 15, 170, 70, "Front", "btn01.png", "btn02.png", "click.mp3")
back_button = ImageButton(WIDTH * 2.5/8 - 10, 15, 170, 70, "Back", "btn01.png", "btn02.png", "click.mp3")
left_button = ImageButton(WIDTH * 4/8, 15, 170, 70, "Left", "btn01.png", "btn02.png", "click.mp3")
right_button = ImageButton(WIDTH * 5.5/8 + 5, 15, 170, 70, "Right", "btn01.png", "btn02.png", "click.mp3")
# Кнопки для паузы
pause_menu_button = ImageButton(WIDTH//3 - 40, HEIGHT // 2, 350, 100, "Главное меню", "btn01.png", "btn02.png", "click.mp3")
continue_menu_button = ImageButton(WIDTH//3 - 40, HEIGHT // 2 - 120, 350, 100, "Вернуться", "btn01.png", "btn02.png", "click.mp3")
# Кнопки промежуточного меню
restart_button = ImageButton(WIDTH//3 - 100, HEIGHT // 2 - 50, 250, 100, "Рестарт", "btn01.png", "btn02.png", "click.mp3")
next_button = ImageButton(WIDTH//3 - 100, HEIGHT // 2 - 140, 250, 100, "Следующий", "btn01.png", "btn02.png", "click.mp3")
konec_lvl_menu_button = ImageButton(WIDTH//3 - 95, HEIGHT // 2 + 40, 150, 100, "Меню", "btn01.png", "btn02.png", "click.mp3")
# Кнопки в выборе лвла
level_menu_button = ImageButton(20, 20, 130, 90, "Меню", "btn01.png", "btn02.png", "click.mp3")
lvl_1_button = ImageButton(150, 60, 150, 500, "Часть 1", "knopka2.png", "lvl1activiti.jpg", "click.mp3")
lvl_2_button = ImageButton(350, 60, 150, 500, "Часть 2", "knopka3.jpg", "lvl2activiti.jpg", "click.mp3")
lvl_3_button = ImageButton(550, 60, 150, 500, "Часть 3", "knopka.png", "lvl3activiti.jpg", "click.mp3")

"""Машинки"""

# список цветов машин по уровню
cars = ['teacher_car', 'red_car', 'white_car', 'yellow_car']
angles = ['front', 'back', 'left', 'right']
color = 0
color_car = cars[color]
angle = angles[0]
car0 = Cars(color_car, angle)

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
# Курсор
cursor = Cursor(0, 0, cursor_group, all_sprites_tools)
# Звёзды
gold = AnimatedSprite('data/star_gold.png', 'data/star_gold_state2.png')
silver = AnimatedSprite('data/star_silver.png', 'data/star_silver_state2.png')
bronza = AnimatedSprite('data/star_bronza.png', 'data/star_bronza_state2.png')

"""Музончик"""

musik = pygame.mixer.Sound('data/mp3')
game_musik = pygame.mixer.Sound('data/gamemp3')
gameover_musik = pygame.mixer.Sound('data/overmp3')
pygame.mixer.music.set_endevent(102)

"""Переменные"""

# Рекорды по уровням
result_lvl1 = 0.00
result_lvl2 = 0.00
result_lvl3 = 0.00
lvl_1flag = True
lvl_2flag = True
lvl_3flag = True

# Просто переменные
font = pygame.font.Font(None, 36)
current_lvl = 1
max_lvl = 1
current_scene = None
play_musik = 1
