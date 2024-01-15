import pygame

# # Инициализация Pygame
# pygame.init()
#
# # Установка размеров окна
# window_width = 500
# window_height = 400
# window = pygame.display.set_mode((window_width, window_height))
#
# # Загрузка изображений для кнопки
# button_up = pygame.image.load('eprst.jpg')
# button_down = pygame.image.load('knopka.png')
#
# # Загрузка звука для кнопки
# click_sound = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
#
# # Функция для отображения кнопки
# def draw_button(x, y, image):
#     window.blit(image, (x, y))
#
# # Основной цикл игры
# running = True
# button_pressed = False
# x, y = 10, 10  # Начальные координаты кнопки
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             if x < mouse_x < x + button_up.get_width() and y < mouse_y < y + button_up.get_height():
#                 button_pressed = True
#                 click_sound.play()
#         elif event.type == pygame.MOUSEBUTTONUP:
#             button_pressed = False
#
#     # Отображение кнопки в зависимости от того, нажата она или нет
#     if button_pressed:
#         draw_button(x, y, button_down)
#     else:
#         draw_button(x, y, button_up)
#
#     # Обновление экрана
#     pygame.display.flip()
#
# # Завершение работы Pygame
# pygame.quit()


# def printText(message, screen, x, y, font_color=(0, 0, 0), font_type='PingPong.otf', font_size=50):
#     font_type = pygame.font.Font(font_type, font_size)
#     text = font_type.render(message, False, font_color)
#     screen.blit(text, (x, y))
#
#
# class Button:
#     def __init__(self, screen, w, h):
#         self.w = w
#         self.h = h
#         self.screen = screen
#         self.ic = (13, 162, 58)
#         self.ac = (23, 204, 58)
#
#     def draw(self, x, y, text, centerx, centery, action=None):
#         mouse = pygame.mouse.get_pos()
#         click = pygame.mouse.get_pressed()
#
#         if x < mouse[0] < x + self.w:
#             if y < mouse[1] < y + self.h:
#                 pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))
#
#                 if click[0] == 1:
#                     print('hui')
#                     pygame.time.delay(100)
#                     if action == 'change':
#
#             else:
#                 pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
#         else:
#             pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
#         printText(text, self.screen, self.w + (x // centerx), y + (self.h // centery)