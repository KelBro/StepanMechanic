# import sqlite3

import pygame  # импорт библиотеки PyGame
# import sys
from button import ImageButton
from cars import Cars

pygame.init()  # инициализируем PyGame

WIDTH = 800  # ширина экрана
HEIGHT = 600  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана
pygame.display.set_caption("StepanMechanic")

"""Изображения"""
# Фон меню
fon = pygame.image.load('data/fon.jpg').convert_alpha()
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
fon.set_colorkey((255, 255, 255))
# Фон игры
garage = pygame.image.load('data/garage.jpg').convert_alpha()
garage = pygame.transform.scale(garage, (WIDTH, HEIGHT))
garage.set_colorkey((255, 255, 255))
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
# Кнопки поворота машины
front_button = ImageButton(WIDTH * 1/8 - 15, 15, 170, 70, "Front", "btn01.png", "btn02.png", "click.mp3")
back_button = ImageButton(WIDTH * 2.5/8 - 10, 15, 170, 70, "Back", "btn01.png", "btn02.png", "click.mp3")
left_button = ImageButton(WIDTH * 4/8, 15, 170, 70, "Left", "btn01.png", "btn02.png", "click.mp3")
right_button = ImageButton(WIDTH * 5.5/8 + 5, 15, 170, 70, "Right", "btn01.png", "btn02.png", "click.mp3")


# список цветов машин по уровню
cars = ['teacher_car', 'red_car', 'white_car', 'yellow_car']
angles = ['front', 'back', 'left', 'right']
color = 0
color_car = cars[color]
angle = angles[0]
car0 = Cars(color_car, angle)
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

        printText("СТЕПАН МЕХАНИК",  400, 50)
        printText("ВОЗВРАЖДЕНИЕ",  400, 130)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)

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
    global angle, angles, color, color_car, cars, car0
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(garage, (0, 0))
        # font = pygame.font.Font(None, 36)
        # if is_running:
        #     elapsed_time = pygame.time.get_ticks() - start_time
        # text = font.render(f'Время: {elapsed_time // 1000}.{(elapsed_time % 1000) // 10} с', True, (0, 0, 0))
        # screen.blit(text, (width // 2 - text.get_width() // 2, 200))
        # Добавление полок для предметов
        pygame.draw.line(screen, (180, 180, 180), [10, 150], [150, 150], 4)
        pygame.draw.line(screen, (180, 180, 180), [10, 300], [150, 300], 4)
        pygame.draw.line(screen, (180, 180, 180), [650, 150], [790, 150], 4)
        pygame.draw.line(screen, (180, 180, 180), [650, 300], [790, 300], 4)
        pygame.draw.line(screen, (180, 180, 180), [650, 450], [790, 450], 4)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if color_car == cars[3]:
                        switch_scene(scene3)
                        running = False
                    else:
                        color += 1
                        color_car = cars[color]
                if event.key == pygame.K_ESCAPE:
                    switch_scene(scene3)
                    running = False

            if event.type == pygame.USEREVENT and event.button == front_button:
                print("Кнопка front была нажата")
                angle = angles[0]
            elif event.type == pygame.USEREVENT and event.button == back_button:
                print("Кнопка back была нажата")
                angle = angles[1]
            elif event.type == pygame.USEREVENT and event.button == left_button:
                print("Кнопка left была нажата")
                angle = angles[2]
            elif event.type == pygame.USEREVENT and event.button == right_button:
                print("Кнопка right была нажата")
                angle = angles[3]


            front_button.handle_event(event)
            back_button.handle_event(event)
            left_button.handle_event(event)
            right_button.handle_event(event)
        # код для обновления и отрисовки здесь
        front_button.check_hover(pygame.mouse.get_pos())
        front_button.draw(screen)
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen)
        left_button.check_hover(pygame.mouse.get_pos())
        left_button.draw(screen)
        right_button.check_hover(pygame.mouse.get_pos())
        right_button.draw(screen)

        car1 = Cars(color_car, angle)
        car1.draw(screen)

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
