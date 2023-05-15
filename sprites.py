import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
PRETO = (0,0,0)
BRANCO = (255,255,255)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites =[]
        self.sprites.append(pygame.image.load('animation-master/spritemario_0.png'))
        self.sprites.append(pygame.image.load('animation-master/spritemario_1.png'))
        self.sprites.append(pygame.image.load('animation-master/spritemario_2.png'))
        self.sprites.append(pygame.image.load('animation-master/spritemario_3.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (800, 445))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 200
        self.animar = False
    def atacar(self):
        self.animar = True
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

imagem_fundo = pygame.image.load('animation-master/eohfundomario.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura,altura))
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((BRANCO))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()
    tela.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()
