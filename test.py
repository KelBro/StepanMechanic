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


# Функция для отрисовки кнопки
def draw_button(color):
    pygame.draw.rect(screen, color, (300, 200, 200, 100))


# Функция для отображения сцены 1
def display_scene1():
    # Загрузка изображения для заднего фона
    background_image = pygame.image.load('data/fon.jpg')
    background_image = pygame.transform.scale(background_image, (width, height))
    # Рисование заднего фона
    screen.blit(background_image, (0, 0))
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    draw_button(button_color)
    draw_text(screen, 'pohui', 100, 300, 185)
    pygame.display.flip()


# Функция для отображения сцены 2
def display_scene2():
    screen.fill((255, 255, 255))
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
soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
pygame.mixer.Sound.play(soundd)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 300:
                button_color = (0, 255, 0)
                if current_scene == "scene1":
                    current_scene = "scene2"
                else:
                    current_scene = "scene1"
        if event.type == pygame.MOUSEBUTTONUP:
            button_color = (255, 0, 0)
    # Добавляем код для перехода на другую сцену
    if current_scene == "scene1":
        display_scene1()
    elif current_scene == "scene2":
        display_scene2()

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()

