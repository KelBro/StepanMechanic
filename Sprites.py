import peremennie
import pygame


class Cursor(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.img = pygame.image.load('data/arrow.png')
        self.image = self.img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()

    def update(self, pos):
        if self.image != self.img:
            self.rect.x = pos[0] - self.size[0] - 20
            self.rect.y = pos[1] - self.size[1] - 20
        else:
            self.rect.x = pos[0]
            self.rect.y = pos[1]


class SpriteTool(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, tool_type, size=None, *group):
        super().__init__(*group)
        self.tool_type = tool_type
        image_path = 'data/' + image_path
        self.image = pygame.image.load(image_path)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, pos, cursor, button):
        # присваивание интрумента к курсору
        if button != 3:
            if self.rect.collidepoint(pos):
                cursor.image = self.image
                cursor.tool = self.tool_type
                # if sponge.image == self.image:
                #     print(self.image)

        # очистка курсора от инструмента
        else:
            cursor.image = cursor.img


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, image1, image2, *group):
        super().__init__(*group)
        self.frames = []
        self.cur_frame = 0
        self.count = -1

        self.image1 = pygame.image.load(image1)
        self.image1 = pygame.transform.scale(self.image1, (80, 80))
        self.image1.set_colorkey((255, 255, 255))

        self.image2 = pygame.image.load(image2)
        self.image2 = pygame.transform.scale(self.image2, (80, 80))
        self.image2.set_colorkey((255, 255, 255))

        self.frames.append(self.image1)
        self.frames.append(self.image2)

    def update(self, x, y):
        if self.count < 0:
            peremennie.screen.blit(self.image1, (x, y))
        self.count += 1
        if self.cur_frame:
            peremennie.screen.blit(self.image1, (x, y))
        else:
            peremennie.screen.blit(self.image2, (x, y))
        if self.count == 20:
            if not self.cur_frame:
                self.cur_frame = 1
                peremennie.screen.blit(self.image1, (x, y))
                self.count = 0
            else:
                self.cur_frame = 0
                peremennie.screen.blit(self.image2, (x, y))
                self.count = 0


class SpriteDefects(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, alpha=256, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/' + image_path)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, change_alpha):  # удаление дефекта с машины
        if change_alpha:
            if self.image.get_alpha() < 255:
                new_alpha = min(255, self.image.get_alpha() + 1)
                self.image.set_alpha(new_alpha)
