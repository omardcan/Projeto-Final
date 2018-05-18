import pygame
import sys
from pygame.locals import*

#======================= CLASSES ====================================

class Aviao(pygame.sprite.Sprite):
    
    def _init_(self,imagem_aviao,posx,posy):
        pygame.sprite.Sprite._init_(self)
        self.px =  posx
        self.py = posy
        self.image = self.image.load(imagem_aviao)
        
    def move(self):
        self.rect.x += self.px
        self.rect.y += self.py
        
    
#    def danos():
    
#====================== INICIAÇÃO ===================================
pygame.init()

tela = pygame.display.set_mode((800,600),0,32)

pygame.display.set_caption("Jogo A+")

#fundo = pygame.imagem.load(             ).convert()

relogio = pygame.time.Clock()

branco = (255,255,255)

#======================= LOOP PRINCIPAL =============================
def loop():

    rodando = True
    while rodando:   
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                rodando = False
        
        tela.fill(branco)
        relogio.tick(30)
        pygame.display.update()    
    pygame.quit()

loop()
