# import sqlite3
# import sys
import cars
from peremennie import *
import pygame  # импорт библиотеки PyGame

pygame.init()

musik = pygame.mixer.Sound('data/mp3')
game_musik = pygame.mixer.Sound('data/gamemp3')
gameover_musik = pygame.mixer.Sound('data/overmp3')


def switch_scene(scene):
    global current_scene
    current_scene = scene


def printText(message, x, y, font_color=(0, 0, 0), font_type="PressStart2PRegular.ttf", font_size=38):
    font_type = pygame.font.Font(font_type, font_size)
    text_surface = font_type.render(message, True, font_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def scene1():
    game_musik.stop()
    gameover_musik.stop()
    musik.play()
    running = True
    while running:
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
                switch_scene(scene2)
                running = False
            elif event.type == pygame.USEREVENT and event.button == levels_button:
                print("Кнопка levels была нажата")
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
    musik.stop()
    game_musik.play()
    running = True

    pygame.display.flip()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                tool_group.update(event.pos, cursor, event.button)
        screen.blit(fon_scene2, (0, 0))
        pygame.draw.line(screen, (255, 255, 255), [10, 150], [150, 150], 4)
        pygame.draw.line(screen, (255, 255, 255), [10, 300], [150, 300], 4)
        pygame.draw.line(screen, (255, 255, 255), [650, 150], [790, 150], 4)
        pygame.draw.line(screen, (255, 255, 255), [650, 300], [790, 300], 4)
        pygame.draw.line(screen, (255, 255, 255), [650, 450], [790, 450], 4)
        all_sprites_tools.draw(screen, pygame.mouse.get_pos())
        cursor_group.update(pygame.mouse.get_pos())

        pygame.display.flip()  # обновляем экран


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
    gameover_musik.play()
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
