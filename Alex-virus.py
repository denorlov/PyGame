import pygame
import time
from tkinter import *
from tkinter import messagebox

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption('ERR_Sys.win10')
font = pygame.font.SysFont("Segoe UI", 20)
font2 = pygame.font.SysFont("Segoe UI", 30)
err1 = font2.render('Критическая ошибка!', 1, (0, 0, 0, 0))
err2 = font.render('Угроза безопасности.', 1, (0, 0, 0, 0))
err3 = font.render('Код ошибки: 0x800F0922', 1, (0, 0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0.10)
            screen = pygame.display.set_mode((500, 300))
            pygame.display.set_caption('ERR_Sys.win10')
    white = [255, 255, 255]
    screen.fill(white)
    screen.blit(err1, (20, 10))
    screen.blit(err2, (20, 70))
    screen.blit(err3, (20, 100))

    pygame.display.update()