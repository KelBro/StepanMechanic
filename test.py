# import pygame
#
# # Инициализация Pygame
# pygame.init()
#
# # Определение цветов
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
#
# # Установка размеров окна
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # Установка начального цвета кнопки
# button_color = RED
# current_scene = "scene1"
#
# # Функция для отрисовки кнопки
# def draw_button(color):
#     pygame.draw.rect(screen, color, (300, 200, 200, 100))
#
# # Функция для отображения сцены 1
# def display_scene1():
#     font = pygame.font.Font(None, 36)
#     text = font.render("Scene 1", True, (0, 0, 0))
#     screen.blit(text, (350, 300))
#
# # Функция для отображения сцены 2
# def display_scene2():
#     font = pygame.font.Font(None, 36)
#     text = font.render("Scene 2", True, (0, 0, 0))
#     screen.blit(text, (350, 300))
#
# # Основной игровой цикл
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 300:
#                 button_color = GREEN
#                 if current_scene == "scene1":
#                     current_scene = "scene2"
#                 else:
#                     current_scene = "scene1"
#         if event.type == pygame.MOUSEBUTTONUP:
#             button_color = RED
#
#     screen.fill((255, 255, 255))
#     draw_button(button_color)
#
#     # Добавляем код для перехода на другую сцену
#     if current_scene == "scene1":
#         display_scene1()
#     elif current_scene == "scene2":
#         display_scene2()
#
#     pygame.display.flip()
#
# pygame.quit()

import pygame
# Инициализация Pygame
pygame.init()


def printText(message, screen, x, y, font_color=(0, 0, 0), font_type='PingPong.otf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, False, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, screen, w, h):
        self.w = w
        self.h = h
        self.screen = screen
        self.ic = (13, 162, 58)
        self.ac = (23, 204, 58)

    def draw(self, x, y, text, centerx, centery, action=None):
        global current_scene
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.w:
            if y < mouse[1] < y + self.h:
                pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))

                if click[0] == 1:
                    print('hui')
                    pygame.time.delay(100)
                    if action == 'change':
                        soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        pygame.mixer.Sound.play(soundd)
                        current_scene = 'scene2'

            else:
                pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        else:
            pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        printText(text, self.screen, self.w + (x // centerx), y + (self.h // centery))


# Функция для отображения сцены 1
def display_scene1():
    # Загрузка изображения для заднего фона
    background_image = pygame.image.load('data/fon.jpg')
    background_image = pygame.transform.scale(background_image, (width, height))
    # Рисование заднего фона
    screen.blit(background_image, (0, 0))
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    buttonScene1 = Button(screen, 250, 100)
    buttonScene1.draw(250, 250, 'START', 5, 6, 'change')
    pygame.display.flip()


# Функция для отображения сцены 2
def display_scene2():
    # screen.fill((255, 255, 255))
    # Загрузка изображения для заднего фона
    background_image = pygame.image.load('data/garage.jpg')
    background_image = pygame.transform.scale(background_image, (width, height))
    # Рисование заднего фона
    screen.blit(background_image, (0, 0))

    # Добавление полок для предметов
    pygame.draw.line(screen, (255, 255, 255), [10, 150], [150, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [10, 300], [150, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 150], [790, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 300], [790, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 450], [790, 450], 4)

    # Губка
    spray_paint = pygame.image.load('data/sponge.png').convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (110, 110))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (20, 50))

    # Вытягиватель вмятин
    spray_paint = pygame.image.load('data/dent_puller.png').convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (140, 140))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (650, 25))

    # Краска
    spray_paint = pygame.image.load('data/f_spray_paint.png').convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (170, 170))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (630, 290))

    # Клей
    spray_paint = pygame.image.load('data/glue.png').convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (150, 150))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (650, 170))

    # Мастерок
    spray_paint = pygame.image.load('data/trowel.png').convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (150, 150))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (15, 175))


    draw_text(screen, 'pizdec', 50, 350, 250)
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

button_color = (255, 0, 0)

current_scene = "scene1"



# soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
# pygame.mixer.Sound.play(soundd)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if current_scene == "scene1":
        display_scene1()
    else:
        display_scene2()
    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()

