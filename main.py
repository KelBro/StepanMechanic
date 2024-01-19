import pygame
pygame.init()

# Создаем окно
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                # Обработка нажатия левой кнопки мыши
                print("Левая кнопка мыши нажата")

    pygame.display.flip()

pygame.quit()
