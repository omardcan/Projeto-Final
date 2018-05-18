import pygame
import pygame.locals

#======================= CLASSES ====================================

class Aviao(pygmae.sprite.Sprite):
    def __init__(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect() 
        self.rect.x = px
        self.rect.y = py
    def move(self,velocidade_x,velocidade_y):
        self.rect.x += velocidade_x
        self.rect.y += velocidade_y
    
#====================== INICIAÇÃO ===================================
pygame.init()

tela = pygame.display.set_mode((800,600),0,32)

pygame.display.set_caption("Jogo A+")

fundo = pygame.image.load("imagem_fundo.jpg").convert()

relogio = pygame.time.Clock()

branco = (255,255,255)

marrom = (199,111,80)
cinza = (150,150,150)
vermelho = (230,0,0)

aviao = Aviao("imagem_nave.jpeg",40,40)
aviao_group = pygame.sprite.Group()
aviao_group.add(aviao)

#======================= LOOP PRINCIPAL =============================
def loop():

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
        
        tela.blit(fundo,(0,0))
        aviao_group.draw(fundo)
        pygame.display.update()    
        pygame.display.flip()
    pygame.quit()
loop()
