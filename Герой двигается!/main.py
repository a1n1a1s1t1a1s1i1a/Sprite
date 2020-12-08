import os
import sys

import pygame


def set_colorkey(colorkey):
    image = pygame.image.load('creature.png')
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))

image =set_colorkey(-1)
screen.fill((255, 255, 255))
image = pygame.transform.scale(image, (100, 100))
image = image.convert_alpha()
pygame.display.set_caption('Герой двигается!')
run = True
screen.blit(image, (10, 10))
x = 10
y = 10
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
        pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 0.01
    elif keys[pygame.K_RIGHT]:
        x += 0.01
    elif keys[pygame.K_UP]:
        y-=0.01
    elif keys[pygame.K_DOWN]:
        y+=0.01
    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))

    pygame.display.flip()
pygame.quit()