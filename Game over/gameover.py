import os
import sys

import pygame


# def set_colorkey(colorkey):
#     image = pygame.image.load('image.png.png')
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
screen = pygame.display.set_mode((600, 300))

#image =set_colorkey(-1)
screen.fill((255, 255, 255))
image = pygame.image.load('image.png')
image = image.convert_alpha()
pygame.display.set_caption('Game over')
run = True
screen.fill((0, 0, 255))
screen.blit(image, (-600, 0))
pygame.display.flip()
x = -600
fps = 200
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
        pygame.key.get_pressed()
    if x < 0:
        x+=1
        screen.fill((0, 0, 255))
        screen.blit(image, (x, 0))
        pygame.display.flip()

    clock.tick(fps)
pygame.quit()