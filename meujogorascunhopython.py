import pygame
from pygame.locals import *
from sys import exit
import os


diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'animation-master')
diretorio_sons = os.path.join(diretorio_imagens, 'animation-master')
pygame.init()

largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mario Run')


sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'marionovo500x588.png')).convert_alpha()

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_mario = []
        for i in range (3):
            img = sprite_sheet.subsurface((i*32,0),(500,588))
            self.imagens_mario.append(img)
        self.index_lista = 0
        self.image = self.imagens_mario[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)



    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_mario[int(self.index_lista)]

todas_as_sprites = pygame.sprite.Group()
mario   = Mario()
todas_as_sprites.add(mario)

imagem_fundo = pygame.image.load('animation-master//foto11.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagem_fundo, (0, 0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()



