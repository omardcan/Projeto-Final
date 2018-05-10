import pygame
import pygame.locals


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
        self.rect.x = px
        self.rect.y = py
        
    def move(self,velocidade_x,velocidade_y):
        self.rect.x = velocidade_x
        self.rect.y = velocidade_y

'''class Tiros(pygame.sprite.Sprite):
    
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.Surface([4,10])
        self.image.fill(preto)
        self.rect = self.image.get_rect()
        
    def voa(self):
        self.rect.x += 5
 '''       
#====================== INICIAÇÃO ===================================

pygame.init()

tela = pygame.display.set_mode((800, 600),0,32)

pygame.display.set_caption("Jogo A+")

fundo = pygame.image.load("imagem_fundo.jpg").convert()

relogio = pygame.time.Clock()

aviao = Aviao("imagem_aviao.png",40,40)

aviao_group = pygame.sprite.Group()
aviao_group.add(aviao)
#aviao_group.add(Tiros)

#tela.blit(fundo,(0,0))
#======================= LOOP PRINCIPAL =============================

def loop():
    y=0
    rodando = True
    while rodando:
        
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
        
        
                if event.key == pygame.K_SPACE:
                    print('tiros')
                    #fazer tiros
                
        
        relogio.tick(27)
        aviao_group.draw(fundo)
    
        y-=1
        rel_x = y % fundo.get_rect().width
        tela.blit(fundo,(rel_x-fundo.get_rect().width,0))
        if rel_x<800:
            tela.blit(fundo,(rel_x,0))
        #tela.blit(aviao_group,Aviao.move)
        pygame.display.update()    
        pygame.display.flip()
        
        
    pygame.quit()

loop()
