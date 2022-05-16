'''
21
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
'''
import pygame
pygame.init()
pygame.mixer.music.load(
    'C:\Intel\Sinny & 7vvch - Petrunko (Numb_ Slowed Remix) (320 kbps).mp3')
pygame.mixer.music.play()
pygame.event.wait()
