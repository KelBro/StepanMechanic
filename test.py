import sqlite3
from cars import Cars
import pygame

# Инициализация Pygame
pygame.init()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y):
        super().__init__(all_sprites2)
        self.frames = []
        self.cur_frame = 0
        self.x = x
        self.y = y

        self.count = -1

        self.image1 = pygame.image.load(image1)
        self.image1 = pygame.transform.scale(self.image1, (80, 80))
        self.image1.set_colorkey((255, 255, 255))

        self.image2 = pygame.image.load(image2)
        self.image2 = pygame.transform.scale(self.image2, (80, 80))
        self.image2.set_colorkey((255, 255, 255))

        self.frames.append(self.image1)
        self.frames.append(self.image2)

    def update(self):
        if self.count == -1:
            self.image = self.frames[self.cur_frame]
            screen.blit(self.image, (self.x, self.y))
        self.count += 1
        if self.count == 35:
            if not self.cur_frame:
                self.cur_frame = 1
            else:
                self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            screen.blit(self.image, (self.x, self.y))
            self.count = 0



class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, size=None, *group, alpha=256):
        super().__init__(*group)
        image_path = 'data/' + image_path
        self.image_orig = pygame.image.load(image_path)
        self.image_orig.set_colorkey([0, 0, 0])
        self.image = self.image_orig.copy()
        self.image.set_alpha(alpha)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, pos, cursor, button):
        # присваивание интрумента к курсору
        if button != 3:
            if self.rect.collidepoint(pos):
                cursor.image = self.image
                # if sponge.image == self.image:
                #     print(self.image)

        # очистка курсора от инструмента
        else:
            cursor.image = cursor.img

    def update_defects(self, change_alpha):  # удаление дефекта с машины
        if change_alpha:
            if self.image.get_alpha() < 255:
                new_alpha = min(255, self.image.get_alpha() + 1)
                self.image.set_alpha(new_alpha)


class Cursor(pygame.sprite.Sprite):

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.img = pygame.image.load('data/arrow.png')
        self.image = self.img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()

    def update(self, pos):
        if self.image != self.img:
            self.rect.x = pos[0] - self.size[0] - 20
            self.rect.y = pos[1] - self.size[1] - 20
        else:
            self.rect.x = pos[0]
            self.rect.y = pos[1]


def printText(message, screen, x, y, font_color=(0, 0, 0), font_type='PingPong.otf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, False, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, screen, w, h, scene=None):
        self.w = w

        self.h = h
        self.screen = screen
        self.ic = (13, 162, 58)
        self.ac = (23, 204, 58)
        self.scene = scene

    def draw(self, x, y, text, centerx, centery, click, action=None):
        global current_scene, car1, to_defect, flag_pause, is_running, start_time, flag_pause2, timeclick, b, elapsed_time, score, selected_level, color_car, cars, game_over__menu
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] and not timeclick:
            timeclick = 1
        elif not click[0]:
            timeclick = 0
        surface = pygame.Surface((150, 400), pygame.SRCALPHA)
        if action != 'change':
            self.ic = (98, 98, 98, 80)
            self.ac = (144, 144, 144)
        if x < mouse[0] < x + self.w:
            if y < mouse[1] < y + self.h:

                # проверка на переход по уровням в меню
                if action == 'knopka' or action == 'knopka2' or action == 'knopka3':
                    pygame.draw.rect(surface, self.ic, surface.get_rect())
                    self.screen.blit(surface, (x, y))
                else:
                    pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))

                cars = ['teacher_car', 'red_car', 'white_car', 'yellow_car']
                color_car = cars[0]
                angle = 'front'
                if click[0] == 1:
                    if action == 'change':
                        # soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        # pygame.mixer.Sound.play(soundd)
                        b = 0
                        current_scene = self.scene
                        game_over__menu = False
                    elif action == 'knopka':
                        selected_level = self.scene
                        current_scene = 'scene2'
                    elif action == 'menu':
                        current_scene = self.scene
                        flag_pause = False
                        flag_pause2 = False
                        timeclick = 1
                        b = 0
                    elif action == 'continue':
                        selected_level += 1
                        score = 0
                        start_time = pygame.time.get_ticks()
                        elapsed_time = 0
                        flag_pause2 = False
                    elif action == 'restart':
                        start_time = pygame.time.get_ticks()
                        elapsed_time = 0
                        flag_pause2 = False
                        score = 0
                        current_scene = self.scene
                    elif action == 'resume':
                        flag_pause = False
                        is_running = True  # Запуск секундомера
                        start_time = pygame.time.get_ticks() - elapsed_time

                    else:  # вид машины
                        if action == 'View1':  # слева
                            angle = 'left'
                            if color_car == 'red_car':
                                to_defect = 'red_left'
                            elif color_car == 'white_car':
                                to_defect = 'white_left'
                            elif color_car == 'yellow_car':
                                to_defect = 'yellow_left'
                            else:
                                to_defect = 0

                        elif action == 'View2':  # справа
                            angle = 'right'
                            to_defect = 0
                            if color_car == 'yellow_car':
                                to_defect = 'yellow_right'
                            else:
                                to_defect = 0

                        elif action == 'View3':  # спереди
                            angle = 'front'
                            if color_car == 'teacher_car':
                                to_defect = 'teacher_front'
                            elif color_car == 'red_car':
                                to_defect = 'red_front'
                            else:
                                to_defect = 0

                        elif action == 'View4':  # сзади
                            angle = 'back'
                            if color_car == 'yellow_car':
                                to_defect = 'yellow_back'
                            elif color_car == 'white_car':
                                to_defect = 'white_back'
                            else:
                                to_defect = 0
                    if action == 'View4' or action == 'View3' or action == 'View2' or action == 'View1':
                        car1 = Cars(color_car, angle)
                        car1.draw(screen)

            else:
                if action != 'knopka' and action != 'knopka2' and action != 'knopka3':
                    pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        else:
            if action != 'knopka' and action != 'knopka2' and action != 'knopka3':
                pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        printText(text, self.screen, centerx, centery)
        if action == 'View4' or action == 'View3' or action == 'View2' or action == 'View1':

            if to_defect == 'red_left' and action == 'View1':
                red_left_group.draw(screen)
            if to_defect == 'white_left' and action == 'View1':
                white_left_group.draw(screen)
            if to_defect == 'yellow_left' and action == 'View1':
                yellow_left_group.draw(screen)

            if to_defect == 'yellow_right' and action == 'View2':
                yellow_right_group.draw(screen)

            if to_defect == 'teacher_front' and action == 'View3':
                # print(1, 2, 3)
                teacher_front_group.draw(screen)
            if to_defect == 'red_front' and action == 'View3':
                red_front_group.draw(screen)

            if to_defect == 'white_back' and action == 'View4':
                white_back_group.draw(screen)
            if to_defect == 'yellow_back' and action == 'View4':
                yellow_back_group.draw(screen)


def photo(file, w, h, x, y):
    if file == 'fon':
        screen.blit(fon, (x, y))
    elif file == 'knopka':
        screen.blit(knopka, (x, y))
    elif file == 'knopka2':
        screen.blit(knopka2, (x, y))
    elif file == 'knopka3':
        screen.blit(knopka3, (x, y))
    elif file == 'game_over':
        screen.blit(game_over_fon, (x, y))
    else:
        screen.blit(BACKGROUND, (x, y))


# Функция для отображения сцены 1
def display_scene1():
    global flag_pause, is_running, start_time, elapsed_time, b
    # Загрузка изображения для заднего фона
    photo('fon', width, height, 0, 0)
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    buttonScene1.draw(250, 200, 'PLAY', 300, 220, click,  'change')
    if b != 7:
        b += 1
    else:
        buttonScene2.draw(250, 350, 'LEVELS', 300, 370, click,  'change')
    is_running = True  # Запуск секундомера
    start_time = pygame.time.get_ticks() - elapsed_time
    elapsed_time = 0
    pygame.display.flip()


# Функция для отображения сцены 2
def display_scene2():
    global is_running, start_time, elapsed_time, color_car, lvl
    # screen.fill((255, 255, 255))
    # Загрузка изображения для заднего фона
    photo('garage', width, height, 0, 0)
    font = pygame.font.Font(None, 36)
    if is_running:
        elapsed_time = pygame.time.get_ticks() - start_time
    text = font.render(f'Время: {elapsed_time // 1000}.{(elapsed_time % 1000) // 10} с', True, (0, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, 200))
    # Добавление полок для предметов
    pygame.draw.line(screen, (255, 255, 255), [10, 150], [150, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [10, 300], [150, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 150], [790, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 300], [790, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 450], [790, 450], 4)

    button_view1.draw(150, 20, 'Left', 170, 25, click, 'View1')
    button_view2.draw(275, 20, 'Right', 285, 25, click, 'View2')
    button_view3.draw(400, 20, 'Top', 430, 25, click, 'View3')
    button_view4.draw(525, 20, 'Behind', 528, 25, click, 'View4')

    if selected_level == 1:
        car1.draw(screen)
    elif selected_level == 2:
        pass
    elif selected_level == 3:
        pass

    # проверка на уровень

    if lvl == 'тренировочный уровень':
        lvl = '1 уровень'
        color_car = cars[0]
    elif lvl == '1 уровень':
        lvl = '2 уровень'
        color_car = cars[1]
    elif lvl == '2 уровень':
        lvl = '3 уровень'
        color_car = cars[2]
    elif lvl == '3 уровень':
        color_car = cars[3]

    all_sprites.draw(screen)
    cursore_group.update(pygame.mouse.get_pos())
    pygame.display.flip()


def display_scene3():
    global b
    screen.fill((200, 220, 220))

    photo('knopka', 150, 400, 100, 120)
    photo('knopka2', 150, 400, 350, 120)
    photo('knopka3', 150, 400, 575, 120)

    button_lvl1.draw(100, 120, 'ONE', 125, 250, click, 'knopka')
    if maxlvl == 2:
        if b != 7:
            b += 1
        else:
            button_lvl2.draw(350, 120, 'TWO', 375, 250, click, 'knopka')
        pygame.draw.rect(screen, (98, 98, 98), (575, 120, 150, 400))
        draw_text(screen, 'LOCKED', 30, 600, 275, (255, 0, 0))
    elif maxlvl == 3:
        button_lvl2.draw(350, 120, 'TWO', 375, 250, click, 'knopka')
        button_lvl3.draw(575, 120, 'THREE', 580, 250, click, 'knopka')
    else:
        pygame.draw.rect(screen, (98, 98, 98), (350, 120, 150, 400))
        pygame.draw.rect(screen, (98, 98, 98), (575, 120, 150, 400))
        draw_text(screen, 'LOCKED', 30, 375, 275, (255, 0, 0))
        draw_text(screen, 'LOCKED', 30, 600, 275, (255, 0, 0))
    button_menu.draw(10, 10, 'MENU', 20, 6, click, 'change')


def end_game_screen():
    global button_menu, game_over__menu
    game_over = False       # Секретная концовка - False, Выигрыш - True

    con = sqlite3.connect('StepanMechanic.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT finished FROM save_game 
    WHERE finished == 3""").fetchall()
    n = 0
    for elem in result:
        if elem[0] == 3:
            n += 1
    if n != 3:
        game_over = True
    con.close()
    screen.fill([0, 0, 0])
    if game_over:
        printText('You Win', screen, 200, 150, [255, 255, 0], 'PressStart2PRegular.ttf', 50)
    else:
        photo('game_over', width, height, 0, 0)

        printText('!!You Win!!', screen,  70, 440, [255, 0, 0], 'PressStart2PRegular.ttf', 60)
        printText('Кчау', screen,  40, 240, [255, 0, 0], 'PressStart2PRegular.ttf', 10)

    game_over__menu = True
    while game_over__menu:
        for event in pygame.event.get():
            # Проверка на выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Переход в главное меню
        button_menu.draw(10, 10, 'MENU', 20, 6, 'change')
        # keys = pygame.key.get_pressed()
        pygame.display.update()
    pygame.display.flip()


def draw_text(window, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)


def game_over1():
    global flag_pause2, click, maxlvl
    surface = pygame.Surface((500, 300), pygame.SRCALPHA)
    pygame.draw.rect(surface, (206, 209, 205, 245), surface.get_rect())
    screen.blit(surface, (150, 150))
    printText('GAME_OVER', screen, 325, 150)
    flag_pause2 = True
    if selected_level > maxlvl:
        maxlvl += 1
    while flag_pause2:
        for event in pygame.event.get():
            # Проверка на выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button_restart.draw(180, 225, 'RESTART', 180, 225, click, 'restart')
        button_continue.draw(420, 330, 'NEXT', 465, 330, click, 'continue')
        buttonmenu.draw(180, 330, 'MENU', 210, 330, click, 'menu')
        print(elapsed_time)
        if elapsed_time < 5000:
            gold.update()
        elif elapsed_time < 10000:
            silver.update()
        else:
            bronza.update()
        pygame.display.update()
    click = (False, False, False)


def pause():
    global flag_pause, last_click_time, is_running, start_time
    is_running = False
    flag_pause = True
    surface = pygame.Surface((500, 300), pygame.SRCALPHA)
    pygame.draw.rect(surface, (160, 123, 90, 230), surface.get_rect())
    screen.blit(surface, (150, 150))
    printText('PAUSE', screen, 325, 150)

    while flag_pause:
        for event in pygame.event.get():
            # Проверка на выход
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button_start.draw(220, 225, 'RESUME', 310, 225, click, 'resume')
        button_meenu.draw(220, 330, 'MENU', 335, 330, click, 'menu')
        keyss = pygame.key.get_pressed()
        pygame.display.update()


# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Загрузка изображений

# Задний фон
BACKGROUND = pygame.image.load('data/garage.jpg').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (width, height))
BACKGROUND.set_colorkey((255, 255, 255))

# Передний фон
fon = pygame.image.load('data/fon.jpg').convert_alpha()
fon = pygame.transform.scale(fon, (width, height))
fon.set_colorkey((255, 255, 255))

# Фон секретной концовки
game_over_fon = pygame.image.load('data/game_over.jpg').convert_alpha()
game_over_fon = pygame.transform.scale(game_over_fon, (width, height))
game_over_fon .set_colorkey((255, 255, 255))

# Кнопки

# Дизайн в меню Лвлов

# 1 лвл
knopka = pygame.image.load('data/knopka2.png').convert_alpha()
knopka = pygame.transform.scale(knopka, (150, 400))
knopka.set_colorkey((255, 255, 255))

# 2 лвл
knopka2 = pygame.image.load('data/knopka3.jpg').convert_alpha()
knopka2 = pygame.transform.scale(knopka2, (150, 400))
knopka2.set_colorkey((255, 255, 255))

# 3 лвл
knopka3 = pygame.image.load('data/knopka.png').convert_alpha()
knopka3 = pygame.transform.scale(knopka3, (150, 400))
knopka3.set_colorkey((255, 255, 255))


# Кнопки в сцене 2

car1 = Cars('yellow_car', 'front')
cars = ['teacher_car', 'red_car', 'white_car', 'yellow_car']
lvl = 'тренировочный уровень'

# Кнопки переключения вида машины
button_view1 = Button(screen, 110, 80, "scene2")
button_view2 = Button(screen, 110, 80, "scene2")
button_view3 = Button(screen, 110, 80, "scene2")
button_view4 = Button(screen, 110, 80, "scene2")


# Кнопки в лвлах

clock = pygame.time.Clock()

current_group = pygame.sprite.Group()
group_changes = False

# Кнопки лвлов
button_lvl1 = Button(screen, 150, 400, 1)
button_lvl2 = Button(screen, 150, 400, 2)
button_lvl3 = Button(screen, 150, 400, 3)
button_menu = Button(screen, 150, 50, "scene1")

# Кнопки в сцене 1

# Сцены
buttonScene1 = Button(screen, 250, 100, "scene2")
buttonScene2 = Button(screen, 250, 100, "scene3")
current_scene = "scene1"

# Пауза
button_start = Button(screen, 360, 80, "resumeP")
button_meenu = Button(screen, 360, 80, "scene1")

# Промежуточное окно
buttonmenu = Button(screen, 200, 80, "scene1")
button_restart = Button(screen, 200, 80, "scene2")
button_continue = Button(screen, 200, 80, "next")


# группы дефектов для машин
defect_group = []

# тестовая машина
teacher_front_group = pygame.sprite.Group()  # спереди: грязь
dirt = Sprite('dirt.png', 336, 400, (120, 80), teacher_front_group)
defect_group.append(teacher_front_group)

# красная машина
red_left_group = pygame.sprite.Group(defect_group)  # слева: грязь
dirt1 = Sprite('dirt 1.png', 335, 350, (130, 100), red_left_group)
defect_group.append(red_left_group)

red_front_group = pygame.sprite.Group(defect_group)  # справа: ржавчина
rust0 = Sprite('rust.png', 336, 364, (115, 115), red_front_group)
# ground_coat = Sprite('ground coat0.png', 340, 354, (110, 90), red_front_group)
defect_group.append(red_front_group)

# белая машина
white_left_group = pygame.sprite.Group(defect_group)  # слева:ржавчина
rust1 = Sprite('rust1.png', 420, 374, (90, 90), white_left_group)
ground_coat = Sprite('ground coat.png', 420, 374, (90, 90), white_left_group)
defect_group.append(white_left_group)

white_back_group = pygame.sprite.Group(defect_group)  # сзади: шина
tire = Sprite('tire puncture.png', 290, 440, (35, 19), white_back_group)
defect_group.append(white_back_group)

# жёлтая машина
yellow_left_group = pygame.sprite.Group(defect_group)  # слева: шина
tire1 = Sprite('tire puncture.png', 499, 440, (35, 19), yellow_left_group)
defect_group.append(yellow_left_group)

yellow_right_group = pygame.sprite.Group(defect_group)  # справа:грязь
dirt2 = Sprite('dirt.png', 336, 360, (120, 80), yellow_right_group)
defect_group.append(yellow_right_group)

yellow_back_group = pygame.sprite.Group(defect_group)  # сзади: ржавчина1
rust2 = Sprite('rust1.png', 300, 334, (120, 120), yellow_back_group)
ground_coat1 = Sprite('ground coat.png', 310, 334, (90, 90), yellow_back_group)
defect_group.append(yellow_back_group)

# стартовый вид машины
to_defect = 'teacher_front'

# Группы спрайтов
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
tool_group = pygame.sprite.Group()
cursore_group = pygame.sprite.Group()

# Спрайты

# Губка
sponge = Sprite('sponge.png', 20, 50, (110, 110), tool_group, all_sprites)
# Вытягиватель вмятин
dent_puller = Sprite('dent_puller.png', 650, 25, (140, 140), tool_group, all_sprites)
# Краска
f_spray_paint = Sprite('f_spray_paint.png', 630, 290, (170, 170), tool_group, all_sprites)
# Клей
glue = Sprite('glue.png', 650, 170, (150, 150), tool_group, all_sprites)
# Мастерок
trowel = Sprite('trowel.png', 15, 175, (120, 120), tool_group, all_sprites)


# Назначение машины

# Управление циклом программы
update = False
running = True
flag_pause = True

button_color = (255, 0, 0)

# приспособление инструментов
usage = {
    sponge.image: (dirt, dirt1),
    trowel.image: (rust0, rust0, rust2),
    glue.image: (tire, tire1),
    f_spray_paint: (ground_coat, ground_coat1)
}

pos = 0
cursor = Cursor(0, 0, cursore_group, all_sprites)
last_click_time = 0

# # флаги групп спрайтов дефектов
# flag = {teacher_front_group: 0,
#         red_left_group: 1,
#         red_front_group: 2,
#         white_left_group: 3,
#         white_back_group: 4,
#         yellow_left_group: 5,
#         yellow_right_group: 6,
#         yellow_back_group: 7
#         }

flag_pause2 = True
is_running = True
start_time = 0
elapsed_time = 0
score = 0
selected_level = 1
click = (False, False, False)
b = 7
maxlvl = 1
# Звёзды

gold = AnimatedSprite('data/star_gold.png', 'data/star_gold_state2.png', 470, 225)
silver = AnimatedSprite('data/star_silver.png', 'data/star_silver_state2.png', 470, 225)
bronza = AnimatedSprite('data/star_bronza.png', 'data/star_bronza_state2.png', 470, 225)
timeclick = 0
# Запуск игры
while running:
    change_alpha = False
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            # Проверка на выход
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    game_over = True
            # Проверка на нажатие кнопки мыши

            if current_scene == 'scene2':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tool_group.update(event.pos, cursor, event.button)
                    if event.button == 1:
                        for index, group in enumerate(defect_group):
                            for sprite in group:
                                if sprite.rect.collidepoint(event.pos):
                                    current_group = group
                                    change_alpha = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        change_alpha = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()

            # screen.fill()
            # Обновление и отрисовка спрайтов в текущей группе

            # current_group.sprites()[0].update_defects(change_alpha)
            # print(defect_group[current_group])

            pygame.display.flip()
            clock.tick(60)  # Ограничение FPS

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and current_scene == 'scene2':
            pause()
            flag_pause = False
        elif score == 18 and current_scene == 'scene2':
            game_over1()
            score = 0
            flag_pause = False
        elif keys[pygame.K_0]:
            score += 1

        # Переключение сцен
        if current_scene == "scene1":
            display_scene1()
        elif current_scene == 'scene2':
            pygame.mouse.set_visible(1)
            display_scene2()
        elif current_scene == 'scene3':
            display_scene3()

        # Обновление экрана
        pygame.display.flip()
        click = (False, False, False)

    end_game_screen()

    # while game_over:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()


# Завершение работы Pygame
pygame.quit()
