import pygame
from cars import Cars
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
    def __init__(self, screen, w, h, scene):
        self.w = w

        self.h = h
        self.screen = screen
        self.ic = (13, 162, 58)
        self.ac = (23, 204, 58)
        self.scene = scene

    def draw(self, x, y, text, centerx, centery, action=None):
        global current_scene
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.w:
            if y < mouse[1] < y + self.h:
                pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))

                if click[0] == 1:
                    pygame.time.delay(100)
                    if action == 'change':
                        # soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        # pygame.mixer.Sound.play(soundd)
                        current_scene = self.scene
            else:
                pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        else:
            pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        printText(text, self.screen, self.w + (x // centerx), y + (self.h // centery))


def photo(file, w, h, x, y):
    # file = 'data/' + file
    # spray_paint = pygame.image.load(file).convert_alpha()
    # spray_paint = pygame.transform.scale(spray_paint, (w, h))
    # spray_paint.set_colorkey((255, 255, 255))
    screen.blit(BACKGROUND, (x, y))


# Функция для отображения сцены 1
def display_scene1():
    # Загрузка изображения для заднего фона
    photo('fon.jpg', width, height, 0, 0)
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    buttonScene1 = Button(screen, 250, 100, "scene2")
    buttonScene1.draw(250, 250, 'START', 5, 6, 'change')
    pygame.display.flip()


# Функция для отображения сцены 2
def display_scene2():
    # screen.fill((255, 255, 255))
    # Загрузка изображения для заднего фона
    photo('garage.jpg', width, height, 0, 0)


    # Добавление полок для предметов
    pygame.draw.line(screen, (255, 255, 255), [10, 150], [150, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [10, 300], [150, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 150], [790, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 300], [790, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 450], [790, 450], 4)

    car1 = Cars('red_car')
    car1.draw(screen)

    all_sprites.draw(screen)
    cursore_group.update(pygame.mouse.get_pos())
    # pygame.display.flip()


def draw_text(window, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)


# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))


BACKGROUND = pygame.image.load('data/garage.jpg').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (width, height))
BACKGROUND.set_colorkey((255, 255, 255))


# Основной цикл программы
update = False
running = True

button_color = (255, 0, 0)

all_sprites = pygame.sprite.Group()
tool_group = pygame.sprite.Group()
cursore_group = pygame.sprite.Group()

current_scene = "scene1"

# Губка
sponge = Sprite('sponge.png', 20, 50, (110, 110), tool_group, all_sprites)

# Вытягиватель вмятин
dent_puller = Sprite('dent_puller.png', 650, 25, (140, 140), tool_group, all_sprites)

# Краска
f_spray_paint = Sprite('f_spray_paint.png', 630, 290, (170, 170), tool_group, all_sprites)

# Клей
glue = Sprite('glue.png', 650, 170, (150, 150), tool_group, all_sprites)

# Мастерок
trowel = Sprite('trowel.png', 15, 175, (150, 150), tool_group, all_sprites)

pos = 0

cursor = Cursor(0, 0, cursore_group, all_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tool_group.update(event.pos, cursor, event.button)

    if current_scene == "scene1":
        display_scene1()
    elif current_scene == 'scene2':
        pygame.mouse.set_visible(0)
        display_scene2()

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
