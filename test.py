import pygame
# Инициализация Pygame
pygame.init()


def printText(message, screen, x, y, font_color=(0, 0, 0), font_type='PingPong.otf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, False, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, screen, w, h, scene):
        self.w = w
        self.h = h
        self.screen = screen
        self.ic = (13, 162, 58)
        self.ac = (23, 204, 58)
        self.scene = scene

    def draw(self, x, y, text, centerx, centery, action=None):
        global current_scene
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.w:
            if y < mouse[1] < y + self.h:
                pygame.draw.rect(self.screen, self.ic, (x, y, self.w, self.h))

                if click[0] == 1:
                    pygame.time.delay(100)
                    if action == 'change':
                        # soundd = pygame.mixer.Sound('supermegatreckotkotorogovsevahue.mp3')
                        # pygame.mixer.Sound.play(soundd)
                        current_scene = self.scene
            else:
                pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        else:
            pygame.draw.rect(self.screen, self.ac, (x, y, self.w, self.h))
        printText(text, self.screen, self.w + (x // centerx), y + (self.h // centery))


def sprites(file, w, h, x, y):
    file = 'data/' + file
    spray_paint = pygame.image.load(file).convert_alpha()
    spray_paint = pygame.transform.scale(spray_paint, (w, h))
    spray_paint.set_colorkey((255, 255, 255))
    screen.blit(spray_paint, (x, y))


# Функция для отображения сцены 1
def display_scene1():
    # Загрузка изображения для заднего фона
    sprites('fon.jpg', width, height, 0, 0)
    draw_text(screen, 'СТЕПАН МЕХАНИК', 50, 200, 50)
    draw_text(screen, 'ВОЗРОЖДЕНИЕ', 50, 200, 100)
    buttonScene1 = Button(screen, 250, 100, "scene2")
    buttonScene1.draw(250, 250, 'START', 5, 6, 'change')
    pygame.display.flip()


# Функция для отображения сцены 2
def display_scene2():
    # screen.fill((255, 255, 255))
    # Загрузка изображения для заднего фона
    sprites('garage.jpg', width, height, 0, 0)

    # Добавление полок для предметов
    pygame.draw.line(screen, (255, 255, 255), [10, 150], [150, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [10, 300], [150, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 150], [790, 150], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 300], [790, 300], 4)
    pygame.draw.line(screen, (255, 255, 255), [650, 450], [790, 450], 4)

    # Губка
    sprites('sponge.png', 110, 110, 20, 50)

    # Вытягиватель вмятин
    sprites('dent_puller.png', 140, 140, 650, 25)

    # Краска
    sprites('f_spray_paint.png', 170, 170, 630, 290)

    # Клей
    sprites('glue.png', 150, 150, 650, 170)

    # Мастерок
    sprites('trowel.png', 150, 150, 15, 175)

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if current_scene == "scene1":
        display_scene1()
    else:
        display_scene2()
    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
