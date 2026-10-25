import pygame
import sys
from pathlib import Path

pygame.mixer.init()
diratual = Path(__file__).resolve().parent

def musica():

    pygame.mixer.music.load(str(fr"{diratual}\sound\trilha-sonora.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def music_ganhador():
    som_vitoria = pygame.mixer.Sound(fr"{diratual}\sound\vencedor.mp3")
    canal = pygame.mixer.Channel(1)
    canal.set_volume(0.5)
    canal.play(som_vitoria)
    
def botoes_music():
    som_botoes = pygame.mixer.Sound(fr"{diratual}\sound\botoes.mp3")
    canal = pygame.mixer.Channel(2)
    canal.set_volume(0.5)
    canal.play(som_botoes)
    
  



musica