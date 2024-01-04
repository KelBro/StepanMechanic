# import pygame
#
#
# class Button:
#     def __init__(self, x, y, widht, height, text, image_path, hover_image_path=None, sound_path=None):
#         self.x = x
#         self.y = y
#         self.widht = widht
#         self.height = height
#         self.text = text
#
#         self.image = pygame.image.load(image_path)
#         self.image = pygame.transform.scale(self.image, (widht, height))
#         self.hover_image = self.image
#         if hover_image_path:
#             self.hover_image = pygame.image.load(hover_image_path)
#             self.hover_image = pygame.transform.scale(self.hover_image, (widht, height))
#         self.rect = self.image.get_rect(topleft=(x, y))
#         self.sound = None
#         if sound_path:
#             self.sound = pygame.mixer.Sound(sound_path)
#         self.is_hovered = False
#
#     def draw(self, screen):
#         current_image = self.hover_image if self.is_hovered else self.image
#         screen.blit(current_image, self.rect.topleft)
#
#         font = pygame.font.Font(None, 36)
#         text_surface = font.render(self.text, True, (255, 255, 255))
#         text_rect = text_surface.get_rect(center=self.rect.center)
#         screen.blit(text_surface, text_rect)
#
#     def check_hover(self, mouse_pos):
#         self.is_hovered = self.rect.collidedict(mouse_pos)
#
#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
#             if self.sound:
#                 self.sound.play()
#             pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
#
#
import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров окна
window_width = 1300
window_height = 1300
window = pygame.display.set_mode((window_width, window_height))

# Загрузка изображений для кнопки
button_up = pygame.image.load('eprst.jpg')
button_down = pygame.image.load('knopka.png')

# Загрузка звука для кнопки
click_sound = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')

# Функция для отображения кнопки
def draw_button(x, y, image):
    window.blit(image, (x, y))

# Основной цикл игры
running = True
button_pressed = False
x, y = 100, 100  # Начальные координаты кнопки
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x < mouse_x < x + button_up.get_width() and y < mouse_y < y + button_up.get_height():
                button_pressed = True
                click_sound.play()
        elif event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False

    # Отображение кнопки в зависимости от того, нажата она или нет
    if button_pressed:
        draw_button(x, y, button_down)
    else:
        draw_button(x, y, button_up)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()

