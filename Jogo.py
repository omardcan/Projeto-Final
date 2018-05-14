import pygame
import pygame.locals
import random

pygame.init()
tela = pygame.display.set_mode((1000, 600),0,32)
pygame.display.set_caption("Jogo A+")
relogio = pygame.time.Clock()
arial = pygame.font.match_font('arial')

branco = (255,255,255)
marrom = (199,111,80)
cinza = (150,150,150)
vermelho = (230,0,0)
preto = (0,0,0)
amarelo = (255,255,0)

score = 0
vidas = 3

#======================= CLASSES ====================================
def Escreve(texto,size,fonte,cor,x,y):
    font = pygame.font.Font(fonte,size)
    ts = font.render(texto,True,cor)
    texto_rect = ts.get_rect()
    texto_rect.midtop = (x,y)
    tela.blit(ts,texto_rect)

class Aviao(pygame.sprite.Sprite):
    
    def _init_(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(self.image,(170,100))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

    def move(self):
        self.velx = 0
        self.vely = 0
        key = pygame.key.get_pressed()
        if self.rect.x >= 0:
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.velx = -8
        if self.rect.x <= 820:
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.velx = 8
        if self.rect.y > 0:
            if key[pygame.K_UP] or key[pygame.K_w]:
                self.vely = -10 
        if self.rect.y <= 500:
            if key[pygame.K_DOWN] or key[pygame.K_s]:
                self.vely = 10
        self.rect.x += self.velx
        self.rect.y += self.vely

class Balao(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load("imagem_balao.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800,5000)
        self.rect.y = random.randrange(0,500)
        self.velx =  - random.randrange(4,7)
    def move(self):
        self.rect.x += self.velx
        if self.rect.x == 200:
            self.rect.x = 600
        

class Fundo(pygame.sprite.Sprite):
    def _init_(self,px,py,x2,y2):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load("imagem_fundo.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def move(self):
        self.rect.x += -1
        if self.rect.x == -1120:
            self.rect.x = 0

class Tiros(pygame.sprite.Sprite):
    
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.Surface([10,5])
        self.image.fill(cinza)
        self.rect = self.image.get_rect()
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.rect.x = aviao.rect.x + 120
            self.rect.y = aviao.rect.y + 50
        self.rect.x += 30
        
class Meteoro(pygame.sprite.Sprite):
    def _init_(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800)
        self.rect.y = random.randrange(0,500)
        self.velx =   - random.randrange(3,5)
    def move(self):
        self.rect.x += self.velx


    
#====================== INICIAÇÃO ===================================

aviao_group = pygame.sprite.Group()
balao_group = pygame.sprite.Group()
tiro_group = pygame.sprite.Group()
fundo_group = pygame.sprite.Group()

fundo = pygame.image.load("imagem_fundo.jpg").convert()
#fundo = Fundo(0,0)
tiros = Tiros()   
aviao = Aviao("imagem_nave.png",40,40)

for i in range(20):
    balao = Balao()
    balao_group.add(balao)


aviao_group.add(aviao)
balao_group.add(balao)
#fundo_group.add(fundo)

#======================= LOOP PRINCIPAL =============================
y=0
rodando = True
while rodando:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aviao_group.add(tiros)
                tiro_group.add(tiros)
    
    for balao in balao_group:
        balao.move()
    aviao.move()
    tiros.move()
    
    
    acertou = pygame.sprite.groupcollide(balao_group,tiro_group,True,True)
    for matou in acertou:
        balao = Balao()
        balao_group.add(balao)
        score +=1 
    hit = pygame.sprite.spritecollide(aviao,balao_group,True)
    if hit:
        vidas -= 1
        balao_group.remove(balao)
        if vidas == 0:
            rodando = False

    
    tela.blit(fundo,(0,0))
    y-=2
    rel_x = y % fundo.get_rect().width
    tela.blit(fundo,(rel_x-fundo.get_rect().width,0))
    if rel_x<1920:
        tela.blit(fundo,(rel_x,0))
        
    Escreve("Pontos: {}".format(score),20,arial,amarelo,80,20)
    Escreve("Vidas: {}".format(vidas),20,arial,amarelo,180,20)
    aviao_group.draw(tela)         
    balao_group.draw(tela)          
    tiro_group.draw(tela)
    pygame.display.update()    
pygame.quit()
