# import sqlite3
import pygame  # импорт библиотеки PyGame
# import sys
from button import ImageButton
from peremennie import *

pygame.init()  # инициализируем PyGame


def switch_scene(scene):
    global current_scene
    current_scene = scene


def printText(message, x, y, font_size=38, font_color=(0, 0, 0), font_type="PressStart2PRegular.ttf"):
    font_type = pygame.font.Font(font_type, font_size)
    text_surface = font_type.render(message, True, font_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def scene1():
    global play_musik, current_lvl
    game_musik.stop()
    gameover_musik.stop()
    if play_musik:
        musik.play(-1)
        play_musik = 0
    running = True
    while running:
        screen.blit(fon, (0, 0))

        printText("СТЕПАН МЕХАНИК",  400, 50)
        printText("ВОЗРАЖДЕНИЕ",  400, 130)

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)

            if event.type == pygame.USEREVENT and event.button == play_button:
                switch_scene(scene2)
                current_lvl = max_lvl
                running = False
            elif event.type == pygame.USEREVENT and event.button == levels_button:
                switch_scene(scene3)
                running = False
            elif event.type == pygame.USEREVENT and event.button == out_button:
                running = False
                switch_scene(None)

            play_button.handle_event(event)
            levels_button.handle_event(event)
            out_button.handle_event(event)
        pos = pygame.mouse.get_pos()
        # код для обновления и отрисовки здесь
        play_button.draw(screen, pos)
        levels_button.draw(screen, pos)
        out_button.draw(screen, pos)

        pygame.display.flip()  # обновляем экран


def scene2():
    global angle, angles, current_lvl, color_car, cars, car0, play_musik
    musik.stop()
    if not play_musik:
        play_musik = 1
        game_musik.play(-1)
    running = True
    is_running = True
    start_time = pygame.time.get_ticks()
    elapsed_time = 0

    while running and current_scene is not None:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    switch_scene(end_game_screen)
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    if not pause():
                        running = False
                    start_time = pygame.time.get_ticks() - elapsed_time
                elif event.key == pygame.K_LSHIFT:
                    konec_lvl(elapsed_time)
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                tool_group.update(event.pos, cursor, event.button)
            if event.type == pygame.USEREVENT and event.button == front_button:
                angle = angles[0]
            elif event.type == pygame.USEREVENT and event.button == back_button:
                angle = angles[1]
            elif event.type == pygame.USEREVENT and event.button == left_button:
                angle = angles[2]
            elif event.type == pygame.USEREVENT and event.button == right_button:
                angle = angles[3]

            front_button.handle_event(event)
            back_button.handle_event(event)
            left_button.handle_event(event)
            right_button.handle_event(event)

        if is_running:
            elapsed_time = pygame.time.get_ticks() - start_time
        color_car = cars[current_lvl]
        screen.blit(fon_scene2, (0, 0))
        pygame.draw.line(screen, (255, 255, 255), [10, 150], [150, 150], 4)
        pygame.draw.line(screen, (255, 255, 255), [10, 300], [150, 300], 4)
        pygame.draw.line(screen, (255, 255, 255), [650, 150], [790, 150], 4)
        pygame.draw.line(screen, (255, 255, 255), [650, 300], [790, 300], 4)
        pygame.draw.line(screen, (255, 255, 255), [650, 450], [790, 450], 4)
        pos = pygame.mouse.get_pos()
        front_button.draw(screen, pos)
        back_button.draw(screen, pos)
        left_button.draw(screen, pos)
        right_button.draw(screen, pos)

        car1 = Cars(color_car, angle)
        car1.draw(screen)
        all_sprites_tools.draw(screen, pos)
        cursor_group.update(pos)
        text = font.render(f'Время: {elapsed_time // 1000}.{(elapsed_time % 1000) // 10} с', True, (150, 150, 150))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 150))
        # код для обновления и отрисовки здесь

        pygame.display.flip()  # обновляем экран


def scene3():
    global current_lvl
    running = True
    screen.blit(level_fon, (0, 0))
    while running:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    switch_scene(scene1)
                    running = False
            if event.type == pygame.USEREVENT and event.button == level_menu_button:
                switch_scene(scene1)
                running = False
            elif event.type == pygame.USEREVENT and event.button == lvl_1_button:
                switch_scene(scene2)
                current_lvl = 1
                running = False
            elif event.type == pygame.USEREVENT and event.button == lvl_2_button:
                switch_scene(scene2)
                current_lvl = 2
                running = False
            elif event.type == pygame.USEREVENT and event.button == lvl_3_button:
                switch_scene(scene2)
                current_lvl = 3
                running = False
            lvl_1_button.handle_event(event)
            lvl_2_button.handle_event(event)
            lvl_3_button.handle_event(event)
            level_menu_button.handle_event(event)

        pos = pygame.mouse.get_pos()
        level_menu_button.draw(screen, pos)
        lvl_1_button.draw(screen, pos)

        if max_lvl < 2:
            printText("Рекорд:", 225, 340, 21, (125, 150, 0))
            printText(f"{result_lvl1 / 1000}c", 225, 380, 21, (125, 150, 160))

            pygame.draw.rect(screen, (151, 151, 151), (350, 60, 150, 500))
            printText("закрыто", 425, 300, 21, (255, 0, 0))
            pygame.draw.rect(screen, (151, 151, 151), (550, 60, 150, 500))
            printText("закрыто", 625, 300, 21, (255, 0, 0))

        elif max_lvl < 3:
            lvl_2_button.draw(screen, pos)
            printText("Рекорд:", 425, 340, 21, (125, 150, 0))
            printText(f"{result_lvl2 / 1000}c", 425, 380, 21, (125, 150, 160))
            pygame.draw.rect(screen, (151, 151, 151), (550, 60, 150, 500))
            printText("закрыто", 625, 300, 21, (255, 0, 0))
        else:
            lvl_2_button.draw(screen, pos)
            lvl_3_button.draw(screen, pos)
            printText("Рекорд:", 425, 340, 21, (125, 150, 0))
            printText(f"{result_lvl2 / 1000}c", 425, 380, 21, (125, 150, 160))
            printText("Рекорд:", 625, 340, 21, (125, 150, 0))
            printText(f"{result_lvl3 / 1000}c", 625, 380, 21, (125, 150, 160))
            if result_lvl2 != 0:
                if result_lvl2 < 20000:
                    gold.update(380, 400)
                elif result_lvl2 < 40000:
                    silver.update(380, 400)
                else:
                    bronza.update(380, 400)
            if result_lvl3 != 0:
                if result_lvl3 < 20000:
                    gold.update(580, 400)
                elif result_lvl3 < 40000:
                    silver.update(580, 400)
                else:
                    bronza.update(580, 400)
        if result_lvl1 != 0:
            if result_lvl1 < 20000:
                gold.update(180, 400)
            elif result_lvl1 < 40000:
                silver.update(180, 400)
            else:
                bronza.update(180, 400)
        printText("Рекорд:", 225, 340, 21, (125, 150, 0))
        printText(f"{result_lvl1 / 1000}c", 225, 380, 21, (125, 150, 160))

        pygame.display.flip()


def konec_lvl(time):
    global max_lvl, current_lvl, result_lvl1, result_lvl2, result_lvl3, lvl_1flag, lvl_2flag, lvl_3flag
    running = True
    surface = pygame.Surface((500, 300), pygame.SRCALPHA)
    pygame.draw.rect(surface, (206, 209, 205, 245), surface.get_rect())
    screen.blit(surface, (150, 150))
    if max_lvl == current_lvl and max_lvl != 3:
        max_lvl += 1
    if lvl_1flag:
        if current_lvl == 1:
            lvl_1flag = False
            result_lvl1 = time
    elif lvl_2flag:
        if current_lvl == 2:
            result_lvl2 = time
            lvl_2flag = False
    elif lvl_3flag:
        if current_lvl == 3:
            result_lvl3 = time
            lvl_3flag = False
    else:
        if current_lvl == 1 and result_lvl1 > time:
            result_lvl1 = time
        elif current_lvl == 2 and result_lvl2 > time:
            result_lvl2 = time
        elif current_lvl == 3 and result_lvl3 > time:
            result_lvl3 = time
    time_sec = f'{time // 1000}.{(time % 1000) // 10}с'
    printText(f"Время:{time_sec}", 520, 180, 20)
    while running:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current_lvl += 1
                    return False
                elif event.key == pygame.K_ESCAPE:
                    switch_scene(scene1)
                    current_lvl += 1
                    return False
            if event.type == pygame.USEREVENT and event.button == konec_lvl_menu_button:
                switch_scene(scene1)
                return False
            elif event.type == pygame.USEREVENT and event.button == restart_button:
                return False
            elif event.type == pygame.USEREVENT and event.button == next_button:
                if current_lvl != 3:
                    current_lvl += 1
                    return False
                else:
                    switch_scene(end_game_screen)
                    return False
            konec_lvl_menu_button.handle_event(event)
            restart_button.handle_event(event)
            next_button.handle_event(event)
        pos = pygame.mouse.get_pos()
        konec_lvl_menu_button.draw(screen, pos)
        restart_button.draw(screen, pos)
        next_button.draw(screen, pos)
        if time < 20000:
            gold.update(470, 225)
        elif time < 40000:
            silver.update(470, 225)
        else:
            bronza.update(470, 225)
        pygame.display.flip()


def pause():
    running = True
    surface = pygame.Surface((500, 300), pygame.SRCALPHA)
    pygame.draw.rect(surface, (206, 209, 205, 245), surface.get_rect())
    screen.blit(surface, (150, 150))
    while running:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    switch_scene(scene2)
                    return True
            if event.type == pygame.USEREVENT and event.button == pause_menu_button:
                switch_scene(scene1)
                return False
            elif event.type == pygame.USEREVENT and event.button == continue_menu_button:
                switch_scene(scene2)
                return True

            pause_menu_button.handle_event(event)
            continue_menu_button.handle_event(event)
        # код для обновления и отрисовки здесь
        pos = pygame.mouse.get_pos()
        continue_menu_button.draw(screen, pos)
        pause_menu_button.draw(screen, pos)
        pygame.display.flip()  # обновляем экран


def end_game_screen():
    game_musik.stop()
    gameover_musik.play(-1)
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
        printText('YOU WIN',  400, 200, 50, (255, 255, 0), 'PressStart2PRegular.ttf')
    else:
        screen.blit(game_over_fon, (0, 0))

        printText('!!You Win!!',  400, 400, 38, (255, 0, 0), 'PressStart2PRegular.ttf')
        printText('Кчау',  40, 240, 10, (255, 0, 0), 'PressStart2PRegular.ttf')

    # game_over__menu = True
    running = True
    while running:

        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:  # если тип события выход из игры, то
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    switch_scene(scene1)
                    running = False

            if event.type == pygame.USEREVENT and event.button == menu_button:
                switch_scene(scene1)
                running = False
            elif event.type == pygame.USEREVENT and event.button == out1_button:
                running = False
                switch_scene(None)

            menu_button.handle_event(event)
            out1_button.handle_event(event)
        pos = pygame.mouse.get_pos()
        # код для обновления и отрисовки здесь
        menu_button.draw(screen, pos)
        out1_button.draw(screen, pos)
        pygame.display.flip()  # обновляем экран


switch_scene(scene1)
while current_scene is not None:
    current_scene()

pygame.quit()
