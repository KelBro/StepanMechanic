# import sqlite3

import pygame  # импорт библиотеки PyGame
# import sys
from button import ImageButton

pygame.init()  # инициализируем PyGame

WIDTH = 800  # ширина экрана
HEIGHT = 600  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана
pygame.display.set_caption("StepanMechanic")
# Фон меню
fon = pygame.image.load('data/fon.jpg').convert_alpha()
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
fon.set_colorkey((255, 255, 255))
# Фон секретной концовки
game_over_fon = pygame.image.load('data/game_over.jpg').convert_alpha()
game_over_fon = pygame.transform.scale(game_over_fon, (WIDTH, HEIGHT))
game_over_fon.set_colorkey((255, 255, 255))

"""Создание кнопок"""

# Кнопки в главном меню
play_button = ImageButton(WIDTH/2 - (350/2), 225, 350, 122, "Play", "btn01.png", "btn02.png", "click.mp3")
levels_button = ImageButton(WIDTH/2 - (350/2), 350, 350, 122, "Levels", "btn01.png", "btn02.png", "click.mp3")
out_button = ImageButton(WIDTH - 252, 500, 252, 100, "Выйти", "btn01.png", "btn02.png", "click.mp3")
# Кнопки для концовки
menu_button = ImageButton(WIDTH/4.5 - (350/2), 500, 350, 100, "Главное меню", "btn01.png", "btn02.png", "click.mp3")
out1_button = ImageButton(WIDTH - 252, 500, 252, 100, "Выйти", "btn01.png", "btn02.png", "click.mp3")


current_scene = None


def switch_scene(scene):
    global current_scene
    current_scene = scene


def printText(message, x, y, font_color=(0, 0, 0), font_type="PressStart2PRegular.ttf", font_size=38):
    font_type = pygame.font.Font(font_type, font_size)
    text_surface = font_type.render(message, True, font_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def scene1():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        # font = pygame.font.Font("PressStart2PRegular.ttf", 38)
        # text_surface = font.render("СТЕПАН МЕХАНИК", True, (0, 0, 0))
        # text_rect = text_surface.get_rect(center=(400, 50))
        # screen.blit(text_surface, text_rect)
        # text_surface = font.render("ВОЗВРАЖДЕНИЕ", True, (0, 0, 0))
        # text_rect = text_surface.get_rect(center=(400, 130))
        # screen.blit(text_surface, text_rect)
        printText("СТЕПАН МЕХАНИК",  400, 50)
        printText("ВОЗВРАЖДЕНИЕ",  400, 130)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            # elif event.type == pygame.KEYDOWN:
            #     switch_scene(scene2)
            #     running = False

            if event.type == pygame.USEREVENT and event.button == play_button:
                print("Кнопка play была нажата")
                switch_scene(scene2)
                running = False
            if event.type == pygame.USEREVENT and event.button == levels_button:
                print("Кнопка levels была нажата")
            if event.type == pygame.USEREVENT and event.button == out_button:
                print("Кнопка out была нажата")
                running = False
                switch_scene(None)

            play_button.handle_event(event)
            levels_button.handle_event(event)
            out_button.handle_event(event)

        # код для обновления и отрисовки здесь
        play_button.check_hover(pygame.mouse.get_pos())
        play_button.draw(screen)
        levels_button.check_hover(pygame.mouse.get_pos())
        levels_button.draw(screen)
        out_button.check_hover(pygame.mouse.get_pos())
        out_button.draw(screen)

        pygame.display.flip()  # обновляем экран


def scene2():
    running = True
    while running:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    switch_scene(scene3)
                    running = False
        screen.fill((255, 255, 255))
        # код для обновления и отрисовки здесь

        pygame.display.flip()  # обновляем экран


def scene3():
    running = True
    while running:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                switch_scene(end_game_screen)
                running = False
        screen.fill((200, 200, 200))
        # код для обновления и отрисовки здесь

        pygame.display.flip()  # обновляем экран


def end_game_screen():
    game_over = False  # Секретная концовка - False, Выигрыш - True

    # con = sqlite3.connect('StepanMechanic.sqlite')
    # cur = con.cursor()
    # result = cur.execute("""SELECT finished FROM save_game
    #     WHERE finished == 3""").fetchall()
    # n = 0
    # for elem in result:
    #     if elem[0] == 3:
    #         n += 1
    # if n != 3:
    #     game_over = True
    # con.close()
    screen.fill([0, 0, 0])
    if game_over:

        printText('YOU WIN',  400, 200, [255, 255, 0], 'PressStart2PRegular.ttf', 50)
    else:
        screen.blit(game_over_fon, (0, 0))

        printText('!!You Win!!',  400, 400, [255, 0, 0], 'PressStart2PRegular.ttf', 38)
        printText('Кчау',  40, 240, [255, 0, 0], 'PressStart2PRegular.ttf', 10)

    # game_over__menu = True
    running = True
    while running:

        # screen.fill((255, 0, 0))

        # font = pygame.font.Font("PressStart2PRegular.ttf", 38)
        # text_surface = font.render("YOU WIN", True, (0, 0, 0))
        # text_rect = text_surface.get_rect(center=(400, 200))
        # screen.blit(text_surface, text_rect)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                switch_scene(scene1)
                running = False

            if event.type == pygame.USEREVENT and event.button == menu_button:
                print("Кнопка menu была нажата")
                switch_scene(scene1)
                running = False
            if event.type == pygame.USEREVENT and event.button == out1_button:
                print("Кнопка out1 была нажата")
                running = False
                switch_scene(None)

            menu_button.handle_event(event)
            out1_button.handle_event(event)
        # код для обновления и отрисовки здесь
        menu_button.check_hover(pygame.mouse.get_pos())
        menu_button.draw(screen)
        out1_button.check_hover(pygame.mouse.get_pos())
        out1_button.draw(screen)
        pygame.display.flip()  # обновляем экран


switch_scene(scene1)
while current_scene is not None:
    current_scene()

pygame.quit()
