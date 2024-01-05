import pygame

# Инициализация Pygame
pygame.init()

# Определение цветов
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Установка размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Установка начального цвета кнопки
button_color = RED
current_scene = "scene1"

# Функция для отрисовки кнопки
def draw_button(color):
    pygame.draw.rect(screen, color, (300, 200, 200, 100))

# Функция для отображения сцены 1
def display_scene1():
    font = pygame.font.Font(None, 36)
    text = font.render("Scene 1", True, (0, 0, 0))
    screen.blit(text, (350, 300))

# Функция для отображения сцены 2
def display_scene2():
    font = pygame.font.Font(None, 36)
    text = font.render("Scene 2", True, (0, 0, 0))
    screen.blit(text, (350, 300))

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 300:
                button_color = GREEN
                if current_scene == "scene1":
                    current_scene = "scene2"
                else:
                    current_scene = "scene1"
        if event.type == pygame.MOUSEBUTTONUP:
            button_color = RED

    screen.fill((255, 255, 255))
    draw_button(button_color)

    # Добавляем код для перехода на другую сцену
    if current_scene == "scene1":
        display_scene1()
    elif current_scene == "scene2":
        display_scene2()

    pygame.display.flip()

pygame.quit()
