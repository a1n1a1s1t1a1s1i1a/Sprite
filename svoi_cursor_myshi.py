import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
image=pygame.image.load('strel.png')
image = pygame.transform.scale(image, (100, 100))
image = image.convert_alpha()
pygame.display.set_caption('Свой курсор мыши')
run = True
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if pygame.mouse.get_focused():
                screen.fill((0, 0, 0))
                screen.blit(image, (x, y))
                pygame.mouse.set_visible(False)
            else:
                screen.fill((0, 0, 0))
                pygame.mouse.set_visible(True)
    pygame.display.flip()
pygame.quit()