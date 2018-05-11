import pygame
import pygame.locals
import random


branco = (255,255,255)
marrom = (199,111,80)
cinza = (150,150,150)
vermelho = (230,0,0)
preto = (0,0,0)

#======================= CLASSES ====================================

class Aviao(pygame.sprite.Sprite):
    
    def __init__(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(200,100))
        self.rect.x = px
        self.rect.y = py
        
    def move(self,velocidade_x,velocidade_y):
        self.rect.x += velocidade_x
        self.rect.y += velocidade_y

class Balao(pygame.sprite.Sprite):
    def __init__(self,arquivo_imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
    
        
#====================== INICIAÇÃO ===================================

pygame.init()

tela = pygame.display.set_mode((800, 600),0,32)

pygame.display.set_caption("Jogo A+")

fundo = pygame.image.load("imagem_fundo.jpg").convert()

relogio = pygame.time.Clock()

aviao_group = pygame.sprite.Group()
balao_group = pygame.sprite.Group()
    
aviao = Aviao("imagem_aviao.png",40,40)

aviao_group.add(aviao)

#balao = Balao("imagem_balao.png")
#
#aviao_group.add(balao)

for i in range(2):
    balao = Balao("imagem_balao.png")
    balao.rect.x = random.randrange(800)
    balao.rect.y = random.randrange(600)
    balao_group.add(balao)


#======================= LOOP PRINCIPAL =============================
y=0
rodando = True
while rodando:
    
    relogio.tick(30)     
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_s or event.key == pygame.K_DOWN: 
                aviao.move(0,20)
            
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                aviao.move(0,-20)
    
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                aviao.move(20,0)
    
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                aviao.move(-20,0)
    
    
    
    tela.blit(fundo,(0,0))
    y-=1
    rel_x = y % fundo.get_rect().width
    tela.blit(fundo,(rel_x-fundo.get_rect().width,0))
    if rel_x<1920:
        tela.blit(fundo,(rel_x,0))
    aviao_group.draw(tela)        
    balao_group.draw(tela)        
    
    pygame.display.update()    


pygame.quit()
