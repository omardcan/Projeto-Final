pygame.init()
tela = pygame.display.set_mode((1000, 600),0,32)
pygame.display.set_caption("Space Rock ")
relogio = pygame.time.Clock()
arial = pygame.font.match_font('arial')
pygame.mixer.music.load('audio_fundo_1.mp3')
pygame.mixer.music.play(-1)



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
timer = 0

with open ("arquivo_highScore.json","r") as arquivo:
    high = int(arquivo.read())

#======================= CLASSES ====================================

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
#====================== INICIAÇÃO ===================================
pygame.init()

tela = pygame.display.set_mode((800,600),0,32)

pygame.display.set_caption("Jogo A+")

fundo = pygame.image.load("imagem_fundo.jpg").convert()

relogio = pygame.time.Clock()
balao_group = pygame.sprite.Group()
balao = Balao("imagem_balao.png")

aviao = Aviao("imagem_nave.jpeg",40,40)
aviao_group = pygame.sprite.Group()
aviao_group.add(aviao)

for i in range(2):
    balao = Balao("imagem_balao.png")
    balao = Balao("imagem_balao.png",random.randrange(750,800),random.randrange(600))
    balao_group.add(balao)
#======================= LOOP PRINCIPAL =============================
def Play():
    y=0
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
                for i in range(2):
                    cometa = Cometa("cometa_{}_.png".format(i))
                cometa_group.add(cometa)
            timer = 0
            
        
        fundo_group.draw(tela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
                
                if event.key == pygame.K_SPACE:
                    tiros = Tiros()
                    aviao_group.add(tiros)
                    tiro_group.add(tiros)
        for tiros in tiro_group:
            tiros.move()
            if tiros.rect.x >= 1100:
                tiro_group.remove(tiros)
        if score == 10:
            score += 1
            alien = Alien()
            alien_group.add(alien)
        
        for meteoro in meteoro_group:
            meteoro.move()
            if meteoro.rect.x <= -400:
                meteoro_group.remove(meteoro)
                
        aviao_group.draw(tela)
        alien_group.draw(tela)
        coracao_group.draw(tela)
        cometa_group.draw(tela)
        meteoro_group.draw(tela)
        tiro_group.draw(tela)
        
        pygame.display.update()
    with open("arquivo_highScore.json","w") as arquivo:
        arquivo.write("{}".format(high))
    
    pygame.quit()

Play()                
