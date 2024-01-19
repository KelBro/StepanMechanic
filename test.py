from cars import Cars
import pygame

# Инициализация Pygame
pygame.init()


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

    def draw(self, x, y, text, centerx, centery, action=None):
        global current_scene, car1, to_defect, flag_pause, is_running, start_time, color_car, cars
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
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

                angle = 'front'
                if click[0] == 1:
                    if action == 'change':
                        # soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        # pygame.mixer.Sound.play(soundd)

                        if not flag_pause:
                            flag_pause = True
                        else:
                            current_scene = self.scene
                    elif action == 'menu':
                        current_scene = self.scene
                        flag_pause = False
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
    else:
        screen.blit(BACKGROUND, (x, y))


# Функция для отображения сцены 1
def display_scene1():
    global flag_pause, is_running, start_time, elapsed_time
    # Загрузка изображения для заднего фона
    photo('fon', width, height, 0, 0)
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    pygame.time.Clock().tick(25)
    buttonScene1.draw(250, 200, 'PLAY', 300, 220, 'change')
    buttonScene2.draw(250, 350, 'LEVELS', 300, 370, 'change')
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

    car1.draw(screen)

    button_view1.draw(150, 20, 'Left', 170, 25, 'View1')
    button_view2.draw(275, 20, 'Right', 285, 25, 'View2')
    button_view3.draw(400, 20, 'Top', 430, 25, 'View3')
    button_view4.draw(525, 20, 'Behind', 528, 25, 'View4')

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
    screen.fill((200, 220, 220))

    photo('knopka', 150, 400, 100, 120)
    photo('knopka2', 150, 400, 350, 120)
    photo('knopka3', 150, 400, 575, 120)

    button_lvl1.draw(100, 120, 'ONE', 125, 250, 'knopka')
    button_lvl2.draw(350, 120, 'TWO', 375, 250, 'knopka2')
    button_lvl3.draw(575, 120, 'THREE', 580, 250, 'knopka3')
    button_menu.draw(10, 10, 'MENU', 20, 6, 'change')


def draw_text(window, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)


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
        button_start.draw(220, 225, 'RESUME', 310, 225, 'resume')
        button_meenu.draw(220, 330, 'MENU', 335, 330, 'menu')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            flag_pause = False
        pygame.display.update()
    pygame.time.Clock().tick(25)


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

# Кнопки

knopka = pygame.image.load('data/knopka2.png').convert_alpha()
knopka = pygame.transform.scale(knopka, (150, 400))
knopka.set_colorkey((255, 255, 255))

knopka2 = pygame.image.load('data/knopka3.jpg').convert_alpha()
knopka2 = pygame.transform.scale(knopka2, (150, 400))
knopka2.set_colorkey((255, 255, 255))

knopka3 = pygame.image.load('data/knopka.png').convert_alpha()
knopka3 = pygame.transform.scale(knopka3, (150, 400))
knopka3.set_colorkey((255, 255, 255))

car1 = Cars('yellow_car', 'front')
cars = ['teacher_car', 'red_car', 'white_car', 'yellow_car']
lvl = 'тренировочный уровень'

# Управление циклом программы
update = False
running = True

button_color = (255, 0, 0)
flag_pause = True

clock = pygame.time.Clock()

current_group = pygame.sprite.Group()
group_changes = False

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

# Кнопки переключения вида машины
button_view1 = Button(screen, 110, 80, "scene2")
button_view2 = Button(screen, 110, 80, "scene2")
button_view3 = Button(screen, 110, 80, "scene2")
button_view4 = Button(screen, 110, 80, "scene2")

# Кнопки лвлов
button_lvl1 = Button(screen, 150, 400, "scene3")
button_lvl2 = Button(screen, 150, 400, "scene3")
button_lvl3 = Button(screen, 150, 400, "scene3")
button_menu = Button(screen, 150, 50, "scene1")

# Сцены
buttonScene1 = Button(screen, 250, 100, "scene2")
buttonScene2 = Button(screen, 250, 100, "scene3")
current_scene = "scene1"

button_start = Button(screen, 360, 80, "resumeP")
button_meenu = Button(screen, 360, 80, "scene1")

# Группы спрайтов
all_sprites = pygame.sprite.Group()
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

is_running = True
start_time = 0
elapsed_time = 0
# Запуск игры
while running:
    change_alpha = False
    for event in pygame.event.get():
        # Проверка на выход
        if event.type == pygame.QUIT:
            running = False
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

# Завершение работы Pygame
pygame.quit()
