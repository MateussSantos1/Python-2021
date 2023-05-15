import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

colisao = pygame.mixer.Sound('smwcoin.wav')
colisao.set_volume(1)
largura = 640
altura = 480
x_cobra = largura / 2
y_cobra = altura / 2
lista_cobra = []

x_maca = randint(40,600)
y_maca = randint(50,430)
pontos = 0
fonte = pygame.font.SysFont("arial", 40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY vai ser uma lista contendo os valores de x e y
        #XeY = [x,y]
        #XeY[0] = x
        #XeY [1] = y
        pygame.draw.rect(tela, (00,255,0),( XeY[0], XeY[1],20,20 ) )

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))
    mensagem = 'Pontos: {}'.format(pontos)
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''

    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 20

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    '''append vai ARMAZENAR os valores ATUAIS de x cobra'''
    lista_cabeca.append(y_cobra)


    lista_cobra.append(lista_cabeca)
    '''essaai vai armazenar os valores atuais, e tambem os que ja foram dados'''

    aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado, (450,40))
    pygame.display.update()

