import pygame
from cars import Cars
# Инициализация Pygame
pygame.init()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, size=None):
        super().__init__()
        image_path = 'data/' + image_path
        self.image = pygame.image.load(image_path)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass  # Метод для обновления спрайта, если это необходимо


class Button:
    def __init__(self, screen, w, h, name=None):
        self.w = w
        self.h = h
        self.screen = screen
        self.ic = (13, 162, 58)
        self.ac = (23, 204, 58)
        self.name = name

    def draw(self, x, y, text=None, centerx=None, centery=None, action=None):
        global Current_Scene
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.w:
            if y < mouse[1] < y + self.h:
                if text != '':
                    pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))

                if click[0] == 1:
                    pygame.time.delay(100)
                    if action == 'change':
                        # soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        # pygame.mixer.Sound.play(soundd)
                        Current_Scene = self.name
                    else:
                        sprite = get_sprite_by_name(all_sprites, self.name)
                        sprite_rect = sprite.get_rect()
                        sprite_rect.center = (mouse[0], mouse[1])
            else:
                if text != '':
                    pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        else:
            pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        if text != '':
            print_text(text, self.screen, self.w + (x // centerx), y + (self.h // centery))


def get_sprite_by_name(group, name):
    for sprite in group:
        if sprite.name == name:
            return sprite
    return None


def print_text(message, screen, x, y, font_color=(0, 0, 0), font_type='PingPong.otf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, False, font_color)
    screen.blit(text, (x, y))


def photo(file, w, h, x, y):
    file = 'data/' + file
    spray_paint = pygame.image.load(file).convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (w, h))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (x, y))


# Функция для отображения сцены 1
def display_scene1():
    # Загрузка изображения для заднего фона
    photo('fon.jpg', width, height, 0, 0)
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    Button_Scene_Change.draw(250, 250, 'START', 5, 6, 'change')
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

    # Губка
    sponge_button.draw(20, 50)

    # Вытягиватель вмятин
    dent_puller_button.draw(650, 25)

    # Краска
    f_spray_paint_button.draw(630, 290)

    # Клей
    glue_button.draw(650, 170)

    # Мастерок
    trowel_button.draw(15, 175)

    all_sprites.draw(screen)
    car1 = Cars('red_car')
    car1.draw(screen)

    pygame.display.flip()


def draw_text(window, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)


# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Основной цикл программы
update = False
running = True

Button_Color = (255, 0, 0)

Current_Scene = "scene1"

# Иницилиализация спрайтов
sponge = Sprite('sponge.png', 20, 50, (110, 110))
sponge.name = "sponge"
dent_puller = Sprite('dent_puller.png', 650, 25, (140, 140))
dent_puller.name = "dent_puller"
f_spray_paint = Sprite('f_spray_paint.png', 630, 290, (170, 170))
f_spray_paint.name = "f_spray_paint"
glue = Sprite('glue.png', 650, 170, (150, 150))
glue.name = "glue"
trowel = Sprite('trowel.png', 15, 175, (150, 150))
trowel.name = "trowel"

all_sprites = pygame.sprite.Group()
all_sprites.add(sponge, dent_puller, f_spray_paint, glue, trowel)

# Иницилиализация кнопок
Button_Scene_Change = Button(screen, 250, 100, "scene2")
trowel_button = Button(screen, 150, 150, "trowel")
glue_button = Button(screen, 150, 150, "glue")
f_spray_paint_button = Button(screen, 170, 170, "f_spray_paint")
dent_puller_button = Button(screen, 140, 140, "dent_puller")
sponge_button = Button(screen, 110, 110, "sponge")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if Current_Scene == "scene1":
        display_scene1()
    elif Current_Scene == 'scene2':
        display_scene2()
    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
