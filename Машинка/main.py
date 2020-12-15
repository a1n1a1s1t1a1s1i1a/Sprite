import os
import sys

import pygame

pygame.init()


screen = pygame.display.set_mode((600, 95))

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("car2.png")
        # и размеры
        self.rect = self.image.get_rect()
        # добавим спрайт в группу
        all_sprites.add(self)
        self.flag = True

    def action(self):
        if (elem.rect.x == 460):
            elem.image = pygame.transform.flip(elem.image, 1, 0)
            self.flag = False

        if (elem.rect.x == -5 and self.flag is False):
            elem.image = pygame.transform.flip(elem.image, 1, 0)
            self.flag = True

        if self.flag:
            elem.rect.x += 1
        else:
            elem.rect.x -= 1


all_sprites = pygame.sprite.Group()


pygame.display.set_caption('Машинка')


all_sprites.draw(screen)
car = Car()
fps = 200

run = True
clock = pygame.time.Clock()
while run:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    for elem in all_sprites:
        elem.action()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()







