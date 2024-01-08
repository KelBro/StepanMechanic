import pygame

red_car = {
    'front': ((265, 250), (266, 201)),
    'back': ((265, 250), (266, 201)),
    'left': ((130, 300), (530, 171)),
    'right': ((130, 300), (530, 171)),
    'top': ((160, 300), (485, 219))
}
white_car = {
    'front': ((260, 280), (280, 188.7)),
    'back': ((260, 280), (280, 188.7)),
    'left': ((130, 300), (530, 164.9)),
    'right': ((130, 300), (530, 164.9)),
    'top': ((200, 300), (400, 172))
}
yellow_car = {
    'front': ((260, 250), (280, 209.7)),
    'back': ((260, 250), (280, 213.2)),
    'left': ((130, 300), (530, 171)),
    'right': ((130, 300), (530, 171)),
    'top': ((160, 300), (485, 219))
}
teacher_car = {
    'front': ((250, 300), (300, 180.3)),
    'back': ((250, 300), (300, 180.6)),
    'left': ((130, 300), (530, 149.5)),
    'right': ((130, 300), (530, 149.5)),
    'top': ((160, 300), (485, 219))
}


class Cars:
    def __init__(self, file, hover_image_path=None):
        global red_car

        cars = []
        car = []
        angle = ['front', 'back', 'left', 'right', 'top']
        for i in angle:
            i = 'front'
            self.image = pygame.image.load('data/' + file + '/' + i + '.png')
            dict0 = {}
            car.append(self.image)
            cars.append(car)
            if 'red_car' == file:
                dict0 = red_car
            elif 'white_car' == file:
                dict0 = white_car
            elif 'yellow_car' == file:
                dict0 = yellow_car
            elif 'teacher_car' == file:
                dict0 = teacher_car
            (x, y), (width, height) = dict0.get(i)
            self.image = pygame.transform.scale(self.image, (width, height))
            self.hover_image = self.image

            if hover_image_path:
                self.hover_image = pygame.image.load(hover_image_path)
                self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

            self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

