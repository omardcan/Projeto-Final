
import pygame
import pygame.locals
from random import randrange

pygame.init()
tela = pygame.display.set_mode((1000, 600),0,32)
pygame.display.set_caption("Space Rock ")
relogio = pygame.time.Clock()
arial = pygame.font.match_font('arial')
#pygame.mixer.music.load('audio_fundo_1.mp3')
#pygame.mixer.music.play(-1)

FPS = 60
temp = 0

branco = (255,255,255)
marrom = (199,111,80)
cinza = (150,150,150)
vermelho = (230,0,0)
preto = (0,0,0)
amarelo = (255,255,0)

score = 0
vidas = 3
vidasAlien = 0

with open ("arquivo_highScore.json","r") as arquivo:
    high = int(arquivo.read())
#======================= CLASSES ====================================
def Escreve(texto,size,fonte,cor,x,y):
    font = pygame.font.Font(fonte,size)
    ts = font.render(texto,True,cor)
    texto_rect = ts.get_rect()
    texto_rect.midtop = (x,y)
    tela.blit(ts,texto_rect)

class Aviao(pygame.sprite.Sprite):
    
    def __init__(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite.__init__(self)
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

class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagem_meteoro.png")
        self.image = pygame.transform.scale(self.image,(110,110))
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = randrange(0,500)
        self.velx =  - randrange(4,7)
    def move(self):
        self.rect.x += self.velx        

class Fundo(pygame.sprite.Sprite):
    def __init__(self,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagem_fundo.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def move(self):
        self.rect.x += -1
        if self.rect.x == -1920:
            self.rect.x = 1920

class Fundo2(pygame.sprite.Sprite):
    def __init__(self,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagem_fundo.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def move(self):
        self.rect.x += -1
        if self.rect.x == -1920:
            self.rect.x = 1920


class Tiros(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,5])
        self.image.fill(vermelho)
        self.rect = self.image.get_rect()
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.rect.x = aviao.rect.x + 11
            self.rect.y = aviao.rect.y + 50
        self.rect.x += 40
        
class Cometa(pygame.sprite.Sprite):
    def __init__(self,imagem_cometa):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem_cometa)
        self.image = pygame.transform.scale(self.image,(180,90))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = randrange(0,500)
        self.velx = -10
    def move(self):
        self.rect.x += self.velx

class Coracao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("heart.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(2000,5000)
        self.rect.y = randrange(0,500)
        
    def move(self):
        self.rect.x -= 3

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagem_alien1.png")
        self.image = pygame.transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = randrange(0,500)
        self.subindo = True
        
    def move(self):
        if self.rect.x >= 700:
            self.rect.x -= 2
        if self.rect.x <= 750:
            if self.rect.y >= 0 and self.subindo:
                self.rect.y -= 5
                if self.rect.y <= 0:
                    self.subindo = False
            if self.rect.y <= 550 and not self.subindo:
                self.rect.y += 5
                if self.rect.y >= 450:
                    self.subindo = True

class Ataque(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,5])
        self.image.fill(vermelho)
        self.rect = self.image.get_rect()
        
    def move(self):
        self.rect.x -= 3

class Foguete(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".png")
        self.image = pygame.transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()


#====================== INICIAÇÃO ===================================

aviao_group = pygame.sprite.Group()
meteoro_group = pygame.sprite.Group()
tiro_group = pygame.sprite.Group()
fundo_group = pygame.sprite.Group()
cometa_group = pygame.sprite.Group()
coracao_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
ataque_group = pygame.sprite.Group()

fundo = Fundo(0,0)
fundo2 = Fundo2(1920,0)
   
aviao = Aviao("imagem_nave.png",40,40)

aviao_group.add(aviao)
fundo_group.add(fundo)
fundo_group.add(fundo2)
timer = 0
timer2 = 0

#======================== MENU INCIAL ==============================
fundoinicial = pygame.image.load("9tKhlA.jpg").convert()

#loopingprincipal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        tela.blit(fundoinicial, (0,0))
    Escreve("Space Rock", 60, arial, branco, 500, 100)
    Escreve("Press SPACE to START",40,arial,branco,700,500)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        
            intro = False
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                intro = False
        
    relogio.tick(60)
    pygame.display.update()
#======================= LOOP PRINCIPAL =============================
rodando = True
while rodando:
    relogio.tick(FPS)
    
    timer += 1
    if timer == 20  :
        aleatorio = randrange(0,100)
        if aleatorio > 10 and aleatorio < 50:
            meteoro = Meteoro()
            meteoro_group.add(meteoro)
        if aleatorio > 50 and aleatorio < 55:
            coracao = Coracao()
            coracao_group.add(coracao)
        if aleatorio > 55 and aleatorio < 60:
            cometa = Cometa("cometa_0_.png")
            cometa_group.add(cometa)
        timer = 0
        
    
    fundo_group.draw(tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            
            if event.key == pygame.K_SPACE:
                tiros = Tiros()
                tiro_group.add(tiros)

    for tiros in tiro_group:
        tiros.move()
        if tiros.rect.x >= 1100:
            tiro_group.remove(tiros)

    if score%100 == 0 and score != 0:
        score += 1
        alien = Alien()
        alien_group.add(alien)
        vidasAlien = 20
    if vidasAlien != 0:
        Escreve("Alien: {}".format(vidasAlien),20,arial,amarelo,580,20)


    for meteoro in meteoro_group:
        meteoro.move()
        if meteoro.rect.x <= -400:
            meteoro_group.remove(meteoro)
    
    for cometa in cometa_group:
        cometa.move()
    
    for coracao in coracao_group:
        coracao.move()
    try:
        alien.move()

    except: ''
    
    aviao.move()
    fundo.move()
    fundo2.move()
    
    try:
        
        mataalien = pygame.sprite.groupcollide(tiro_group,alien_group,True,False)
        for shot in mataalien:
            vidasAlien -= 1
            if vidasAlien <= 0:
                alien_group.remove(alien)
                score += 20
    except:
        ""
    acertou = pygame.sprite.groupcollide(tiro_group,meteoro_group,True, True)
    for matou in acertou:
        score += 10
    
    hit = pygame.sprite.spritecollide(aviao,meteoro_group,True)
    if hit:
        vidas -= 1
        meteoro_group.remove(meteoro)
    
    
    hit_mortal = pygame.sprite.spritecollide(aviao,cometa_group,True)
    if hit_mortal:
        vidas -= 3
        cometa_group.remove(cometa)
    
    pegaVida = pygame.sprite.spritecollide(aviao,coracao_group,True)
    if pegaVida:
        if vidas < 3:
            coracao_group.remove(coracao)
            vidas += 1
    
    
    Escreve("Pontos: {}".format(score),20,arial,amarelo,80,20)
    Escreve("Vidas: {}".format(vidas),20,arial,amarelo,180,20)
    Escreve("High Score: {}".format(high),20,arial,amarelo,100,40)
    if score > high:
        high = score
    
    aviao_group.draw(tela)
    alien_group.draw(tela)
    
    coracao_group.draw(tela)
    cometa_group.draw(tela)
    meteoro_group.draw(tela)
    tiro_group.draw(tela)
    
    

    # Tela GAME OVER
    while vidas <= 0:
        relogio.tick(FPS)
        tela.fill(vermelho)
        
        Escreve("Jogar Novamente: x",50,arial,amarelo,500,200)
        Escreve("Sair: y",50,arial,amarelo,500,260)
        for event in pygame.event.get():    
            if event.key == pygame.K_y:
                with open("arquivo_highScore.json","w") as arquivo:
                    arquivo.write("{}".format(high))
                pygame.quit()
            if event.key == pygame.K_x:
                score = 0
                vidas = 3
                for meteoro in meteoro_group:
                    meteoro_group.remove(meteoro)
                for coracao in coracao_group:
                    coracao_group.remove(coracao)
                try:
                    vidasAlien = 0
                    alien_group.remove(alien)
                except:
                    ''    
        pygame.display.update()

    pygame.display.update()
with open("arquivo_highScore.json","w") as arquivo:
    arquivo.write("{}".format(high))

pygame.quit()


