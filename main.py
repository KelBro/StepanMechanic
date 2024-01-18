import pygame
import sys

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
width, height = 400, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Секундомер')

# Шрифт
font = pygame.font.Font(None, 36)

# Переменные для секундомера
is_running = False
start_time = 0
elapsed_time = 0

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Нажатие пробела
                if is_running:
                    is_running = False  # Остановка секундомера
                    # elapsed_time += pygame.time.get_ticks() - start_time
                else:
                    is_running = True  # Запуск секундомера
                    start_time = pygame.time.get_ticks() - elapsed_time

    # Отрисовка
    window.fill(WHITE)
    if is_running:
        elapsed_time = pygame.time.get_ticks() - start_time
    text = font.render(f'Время: {elapsed_time // 1000}.{(elapsed_time % 1000)//10} с', True, BLACK)
    window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()

pygame.quit()
sys.exit()
