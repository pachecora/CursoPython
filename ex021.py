#! /home/morpheus/Documentos/CursoPython/venv/bin/python3

# Tocando um mp3

import pygame

# pygame.init()
# pygame.mixer.music.load("GoodLife.mp3")


# from pygame import mixer

# mixer.init() 

# mixer.music.load('GoodLife.mp3')

# mixer.music.play()

# import time

# time.sleep(360)

pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()
