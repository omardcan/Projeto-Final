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
cor = (199,111,80)
cor2 = (150,150,150)


#======================= LOOP PRINCIPAL =============================

def loop():

    rodando = True
    while rodando:   
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                rodando = False

             if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_s or event.key == pygame.K_DOWN: 
                    aviao.move_ip(0,20)
                
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    aviao.move_ip(0,-20)
                    
        
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    aviao.move_ip(20,0)
        
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    aviao.move_ip(-20,0)
        
        
                if event.key == pygame.K_SPACE:
                    print('tiros')
                    #fazer tiros



        
        tela.fill(branco)
        relogio.tick(30)
        
        
        # aviao e balao sao representados por retangulos ainda
        pygame.draw.rect(tela,cor,aviao)
        pygame.draw.rect(tela,cor2,balao)
        
        
        pygame.display.update()    
    pygame.quit()

loop()
