from cars import Cars
import pygame
# Инициализация Pygame
pygame.init()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, size=None, *group):
        super().__init__(*group)
        image_path = 'data/' + image_path
        self.image = pygame.image.load(image_path)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, pos, cursor, button):
        # global update, pos
        # if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
        #         self.rect.collidepoint(args[0].pos):
        #     pygame.mouse.set_visible(False)
        #     pos = self.rect.center
        #     self.rect.center = pygame.mouse.get_pos()
        if button != 3:
            if self.rect.collidepoint(pos):
                cursor.image = self.image
        else:
            cursor.image = cursor.img


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
        global current_scene, car1
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        surface = pygame.Surface((150, 400), pygame.SRCALPHA)
        if action != 'change':
            self.ic = (98, 98, 98, 80)
            self.ac = (144, 144, 144)

        if x < mouse[0] < x + self.w:
            if y < mouse[1] < y + self.h:
                if action == 'knopka' or action == 'knopka2' or action == 'knopka3':
                    pygame.draw.rect(surface, self.ic, surface.get_rect())
                    self.screen.blit(surface, (x, y))
                else:
                    pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))

                if click[0] == 1:
                    if action == 'change':
                        # soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        # pygame.mixer.Sound.play(soundd)
                        current_scene = self.scene
                        # вид машины
                    elif action == 'View1':
                        car1 = Cars('red_car', 'left')
                        car1.draw(screen)
                    elif action == 'View2':
                        car1 = Cars('red_car', 'right')
                        car1.draw(screen)
                    elif action == 'View3':
                        car1 = Cars('red_car', 'front')
                        car1.draw(screen)
                    elif action == 'View4':
                        car1 = Cars('red_car', 'back')
                        car1.draw(screen)

            else:
                if action != 'knopka' and action != 'knopka2' and action != 'knopka3':
                    pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        else:
            if action != 'knopka' and action != 'knopka2' and action != 'knopka3':
                pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        printText(text, self.screen, centerx, centery)


def photo(file, w, h, x, y):
    # file = 'data/' + file
    # spray_paint = pygame.image.load(file).convert_alpha()
    # spray_paint = pygame.transform.scale(spray_paint, (w, h))
    # spray_paint.set_colorkey((255, 255, 255))
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
    # Загрузка изображения для заднего фона
    photo('fon', width, height, 0, 0)
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    buttonScene1.draw(250, 200, 'PLAY', 300, 220, 'change')
    buttonScene2.draw(250, 350, 'LEVELS', 300, 370, 'change')
    pygame.display.flip()


# Функция для отображения сцены 2
def display_scene2():
    # screen.fill((255, 255, 255))
    # Загрузка изображения для заднего фона
    photo('garage', width, height, 0, 0)

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

    all_sprites.draw(screen)
    cursore_group.update(pygame.mouse.get_pos())


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

car1 = Cars('red_car', 'front')

# Управление циклом программы
update = False
running = True

button_color = (255, 0, 0)

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

pos = 0
cursor = Cursor(0, 0, cursore_group, all_sprites)

# Запуск игры
while running:
    for event in pygame.event.get():

        # Проверка на выход
        if event.type == pygame.QUIT:
            running = False

        # Проверка на нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            tool_group.update(event.pos, cursor, event.button)

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
