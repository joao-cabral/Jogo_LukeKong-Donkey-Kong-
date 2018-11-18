import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Luke Kong")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 700))
fonte = pygame.font.SysFont('Arial', 30, True, False)

luke_direita = pygame.transform.scale(pygame.image.load("luke.png"), (29, 50))
luke_esquerda = pygame.transform.flip(pygame.transform.scale(pygame.image.load("luke.png"), (29, 50)), True, False)

luke_pulo_direita = pygame.transform.scale(pygame.image.load("luke.png"), (29, 50))
luke_pulo_esquerda = pygame.transform.flip(pygame.transform.scale(pygame.image.load("luke.png"), (29, 50)), True, False)

luke_subir_direita = pygame.transform.scale(pygame.image.load("luke.png"), (29, 50))
luke_subir_esquerda = pygame.transform.flip(pygame.transform.scale(pygame.image.load("luke.png"), (29, 50)), True, False)

mal_vader_frente = pygame.transform.scale(pygame.image.load("mal_vader_frente.png"), (50, 90))

mal_vader_direita = pygame.transform.scale(pygame.image.load("mal_vader_movimento.png"), (50, 90))
mal_vader_esquerda = pygame.transform.flip(pygame.transform.scale(pygame.image.load("mal_vader_movimento.png"), (50, 90)), True, False)

mal_vader_ataque = pygame.transform.scale(pygame.image.load("darth_vader_ataque.png"), (100, 90))

zero_imagem = pygame.image.load("zero.png")

python_parado = pygame.transform.scale(pygame.image.load("python.png"), (100, 100))
python_ajuda = pygame.transform.scale(pygame.image.load("python.png"), (100, 100))

dez_imagem = pygame.transform.scale(pygame.image.load("dez.png"), (50, 50))

pygame.mixer.music.load("Som/HoraDeBrincar.ogg")

subir = luke_subir_direita

movimento = [mal_vader_direita, mal_vader_esquerda]
atacando = mal_vader_ataque

imagem_python = [python_parado, python_ajuda]

plataforma_imagem = pygame.image.load("plataforma.jpg")

menu_vezzi = pygame.image.load("inicial.jpg")

class Plataforma:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        
        def draw(self):
                screen.blit(plataforma_imagem, (self.x, self.y))
                                
class Luke:
        def __init__(self):
                self.x = 75
                self.y = 580
                self.img = luke_direita
                self.phase = "still"
                self.dir = "right"
                self.anim_time = 0
                self.anim_num = 1
                self.level = plataforma_lvl1
                self.level_num = 1
                self.jump_start = 0
                self.caindo = False
                self.lose_dir = 0
                self.lost = False
                self.flash_time_end = time.time() + 1
                self.zero = False
        
        def movimento(self):
                if (pressed_keys[K_RIGHT]) and (not pressed_keys[K_SPACE]) and (not self.phase == "jump") and (not self.phase == "jump_right") and (not self.phase == "jump_left") and (not self.phase == "climb"):
                        self.phase = "move_right"
                        self.dir = "right"
                        self.x += 5
                elif (pressed_keys[K_LEFT]) and (not pressed_keys[K_SPACE]) and (not self.phase == "jump") and (not self.phase == "jump_right") and (not self.phase == "jump_left") and (not self.phase == "climb"):
                        self.phase = "move_left"
                        self.dir = "left"
                        self.x -= 5
                        
                elif (not self.caindo) and (pressed_keys[K_SPACE]) and (not pressed_keys[K_RIGHT]) and (not pressed_keys[K_LEFT]) and (not self.phase == "jump") and (not self.phase == "jump_right") and (not self.phase == "jump_left") and (not self.phase == "climb"):
                        self.phase = "jump"
                        self.jump_start = time.time()
                elif (not self.caindo) and(pressed_keys[K_SPACE]) and (pressed_keys[K_RIGHT]):
                        self.phase = "jump_right"
                        self.jump_start = time.time()
                elif (not self.caindo) and (pressed_keys[K_SPACE]) and (pressed_keys[K_LEFT]) and (not self.phase == "jump") and (not self.phase == "jump_right") and (not self.phase == "jump_left") and (not self.phase == "climb"):
                        self.phase = "jump_left"
                        self.jump_start = time.time()
                
                '''elif (not self.phase == "jump") and (not self.phase == "jump_right") and (not self.phase == "jump_left") and (not self.phase == "climb"):
                        self.phase = "still"'''
                
                if self.phase == "jump":
                        if time.time() < self.jump_start + .40:
                                self.y -= 4
                        else:
                                self.phase = "still"
                                
                if self.phase == "jump_right":
                        if time.time() < self.jump_start + .40:
                                self.x += 4
                                self.y -= 4
                        else:
                                self.phase = "still"
                if self.phase == "jump_left":
                        if time.time() < self.jump_start + .40:
                                self.x -= 4
                                self.y -= 4
                        else:
                                self.phase = "still"
                
                if self.x <= 0:
                        self.x = 0
                if self.x >= 771:
                        self.x = 771
                
        
        def animacao(self):
                if self.phase == "still" and self.dir == "right":
                        self.img = luke_direita
                        self.anim_num = 1
                if self.phase == "still" and self.dir == "left":
                        self.img = luke_esquerda
                        self.anim_num = 1
                
                if self.phase == "move_right" :
                        self.img = luke_direita
                        self.anim_num += 1
                        if self.anim_num == 2:
                                self.anim_num = 0
                        self.anim_time = time.time()
                
                if self.phase == "move_left" :
                        self.img = luke_esquerda
                        self.anim_num += 1
                        if self.anim_num == 2:
                                self.anim_num = 0
                        self.anim_time = time.time()
                
                if self.phase == "climb":
                        self.img = subir
                        self.anim_num += 1
                        if self.anim_num == 2:
                                self.anim_num = 0
                        self.anim_time = time.time()
                
                if self.phase == "jump" or self.phase == "jump_right" or self.phase == "jump_left":
                        if self.dir == "right":
                                self.img = luke_pulo_direita
                        elif self.dir == "left":
                                self.img = luke_pulo_esquerda
        
        def gravidade(self):
                self.y += 2
                self.plataforma_tocada = 0
                for plataforma in self.level:
                        if pygame.Rect(plataforma.x, plataforma.y, 50, 20).colliderect(self.x, self.y, 29, 50):
                                self.plataforma_tocada += 1
                if self.plataforma_tocada > 0:
                        self.y -= 5
                        self.caindo = False
                else:
                        self.caindo = True
        def escalar(self):
                if (pressed_keys[K_UP]) and (not self.caindo) and (not self.phase == "jump") and (not self.phase == "jump_right") and (not self.phase == "jump_left") and (not self.phase == "climb"):
                        for escada in escadas:
                                if pygame.Rect(self.x + 12.5, self.y, 25, 75).colliderect(escada.x, escada.y, 60, escada.escada_comprimento):
                                        self.phase = "climb"
                                        self.escada_base = self.y
                                        self.escada_escalada = escada
                if self.phase == "climb":
                        if self.y < self.escada_base - (self.escada_escalada.escada_comprimento + 25):
                                self.phase = "still"
                                self.level_num += 1
                                self.level = plataforma_lvls[self.level_num - 1]
                        else:
                                self.y -= 5
        
        def hit_zero(self):
                for zero in zeros:
                        if pygame.Rect(self.x + 12.5, self.y, 25, 25).colliderect(zero.x + 5, zero.y + 10, 25, 25):
                                return True
        
        def perder(self):
                self.y += 5
                self.lose_dir += 5
                rotated = pygame.transform.rotate(luke_pulo_esquerda, self.lose_dir)
                screen.blit(rotated, (self.x, self.y))
        
        def ganhar(self):
                self.dir = "left"
                if self.x > 110 and darth_vezzi.y > 600:
                        self.x -= 3
                        self.phase = "move_left"
                else:
                        self.phase = "still"
                if not self.zero and self.x < 120:
                        self.zero = Dez()
                        
        def draw(self):
                if time.time() > self.flash_time_end or time.time()%0.1 < 0.05:
                        screen.blit(self.img, (self.x, self.y))

class Escada:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        
        def draw(self):
                self.escada_comprimento = 60
                for i in range(int(self.escada_comprimento/10.0)):
                        pygame.draw.line(screen, (150, 150, 255), (self.x, self.y + (i+1)*10), (self.x + 40, self.y + (i+1)*10), 5)

class Darth_vezzi:
        def __init__(self):
                self.x = 300
                self.y = 20
                self.img = mal_vader_frente
                self.phase = "still"
                self.phase_start = time.time()
                self.phases = ["pound", "push"]
                self.phase_comprimeto = random.randrange(5, 20)/60
                self.last_anim = time.time()
                self.current_anim = 0
                self.lose_dir = 0
                self.lost = False
        
        def pick_move(self):
                if self.phase == "still" and time.time() > self.phase_start + self.phase_comprimeto:
                        self.phase = self.phases[random.randrange(2)]
                        self.phase_start = time.time()
                        self.phase_comprimeto = random.randrange(5, 20)/50
                        self.last_anim = time.time()
                        self.current_anim = 0
                        
                elif self.phase == "pound" and time.time() > self.phase_start + self.phase_comprimeto:
                        self.phase = "still"
                        self.phase_start = time.time()
                        self.phase_comprimeto = random.randrange(5, 20)/50
                        
                elif self.phase == "push" and time.time() > self.phase_start + 1:
                        self.phase = "still"
                        self.phase_start = time.time()
                        self.phase_comprimeto = random.randrange(5, 20)/50
        
        def animacao(self):
                if self.phase == "still":
                        self.img = mal_vader_frente
                
                elif self.phase == "pound" and time.time() > self.last_anim + 0.25:
                        self.current_anim += 1
                        if self.current_anim == 2:
                                self.current_anim = 0
                        self.img = movimento[self.current_anim]
                        self.last_anim = time.time()
                
                elif self.phase == "push" and time.time() > self.last_anim + 0.5:
                        zeros.append(Zero())
                        self.current_anim += 1
                        if self.current_anim == 2:
                                self.phase = "still"
                        else:
                                self.img = atacando
                                self.last_anim = time.time()
        
        def perder(self):
                self.y += 5
                self.lose_dir += 5
                rotated = pygame.transform.rotate(mal_vader_direita, self.lose_dir)
                screen.blit(rotated, (self.x, self.y))
        
        def draw(self):
                screen.blit(self.img, (self.x, self.y))

class Zero:
        def __init__(self):
                self.x = 350
                self.y = 30
                self.dir = 0
                self.level = plataforma_lvl6
                self.level_num = 6
                self.roll_dir = 1
        
        def move(self):
                if self.roll_dir == 1:
                        self.x += 3
                        self.dir -= 5
                elif self.roll_dir == -1:
                        self.x -= 3
                        self.dir += 5
                        
                elif self.roll_dir == 0:
                        self.plataforma_tocada = 0
                        for plataforma in self.level:
                                if pygame.Rect(plataforma.x, plataforma.y, 50, 1).colliderect(self.x, self.y, 36, 51):
                                        self.plataforma_tocada += 1
                        if self.plataforma_tocada > 0:
                                if self.level_num == 1 or  self.level_num == 3 or  self.level_num == 5:
                                        self.roll_dir = -1
                                        self.x -= 3
                                elif self.level_num == 2 or  self.level_num == 4 or  self.level_num == 6:
                                        self.roll_dir = 1
                                        self.x += 3
                
                if self.x >= 650 and self.roll_dir == 1:
                        self.roll_dir = 0
                        self.level_num -= 1
                elif self.x <= 0 and self.roll_dir == -1:
                        self.roll_dir = 0
                        self.level_num -= 1
                
                self.level = plataforma_lvls[self.level_num - 1]
        
        def cair(self):
                self.y += 2
                self.plataforma_tocada = 0
                for plataforma in self.level:
                        if pygame.Rect(plataforma.x, plataforma.y, 50, 1).colliderect(self.x, self.y, 50, 36):
                                self.plataforma_tocada += 1
                if self.plataforma_tocada > 0:
                        self.y -= 5
        
        def fim_tela(self):
                return self.y > 700
        
        def draw(self):
                rotated = pygame.transform.rotate(zero_imagem, self.dir)
                screen.blit(rotated, (self.x, self.y))

class Phyton:
        def __init__(self):
                self.x = 20
                self.y = 15
                self.anim_num = 0
                self.anim_start = 0
                
        def animate(self):
                if time.time() > self.anim_start + 0.5:
                        self.anim_num += 1
                        if self.anim_num == 2:
                                self.anim_num = 0
                                self.anim_start = time.time()
                                
                if self.anim_num == 1:
                        screen.blit(fonte.render("Não Falte!", True, (255, 255, 255)), (100, 15))
        def draw(self):
                screen.blit(imagem_python[self.anim_num], (self.x, self.y))
class Dez:
        def __init__(self):
                self.x = 90
                self.y = 30
        
        def draw(self):
                self.y -= 1
                screen.blit(dez_imagem, (self.x, self.y))
                
plataforma_lvl1 = (Plataforma(0, 680), Plataforma(50, 680), Plataforma(100, 680),
                Plataforma(150, 680), Plataforma(200, 680), Plataforma(250, 680),
                Plataforma(300, 680), Plataforma(350, 676), Plataforma(400, 672),
                Plataforma(450, 668), Plataforma(500, 664), Plataforma(550, 660),
                Plataforma(600, 656), Plataforma(650, 652), Plataforma(700, 648),
                Plataforma(750, 644))

plataforma_lvl2 = (Plataforma(0, 520), Plataforma(50, 524), Plataforma(100, 528),
                Plataforma(150, 532), Plataforma(200, 536), Plataforma(250, 540),
                Plataforma(300, 544), Plataforma(350, 548), Plataforma(400, 552),
                Plataforma(450, 556), Plataforma(500, 560), Plataforma(550, 564),
                Plataforma(600, 568), Plataforma(650, 572))

plataforma_lvl3 = (Plataforma(100, 460), Plataforma(150, 456), Plataforma(200, 452),
                Plataforma(250, 448), Plataforma(300, 444), Plataforma(350, 440),
                Plataforma(400, 436), Plataforma(450, 432), Plataforma(500, 428),
                Plataforma(550, 424), Plataforma(600, 420), Plataforma(650, 416),
                Plataforma(700, 412), Plataforma(750, 408))

plataforma_lvl4 = (Plataforma(0, 296), Plataforma(50, 300), Plataforma(100, 304),
                Plataforma(150, 308), Plataforma(200, 312), Plataforma(250, 316),
                Plataforma(300, 320), Plataforma(350, 324), Plataforma(400, 328),
                Plataforma(450, 332), Plataforma(500, 336), Plataforma(550, 340),
                Plataforma(600, 344), Plataforma(650, 348))

plataforma_lvl5 = (Plataforma(100, 236), Plataforma(150, 232), Plataforma(200, 228),
                Plataforma(250, 224), Plataforma(300, 220), Plataforma(350, 216),
                Plataforma(400, 212), Plataforma(450, 208), Plataforma(500, 204),
                Plataforma(550, 200), Plataforma(600, 196), Plataforma(650, 192),
                Plataforma(700, 188), Plataforma(750, 184))

plataforma_lvl6 = (Plataforma(0, 110), Plataforma(50, 110), Plataforma(100, 110),
                Plataforma(150, 110), Plataforma(200, 110), Plataforma(250, 110),
                Plataforma(300, 110), Plataforma(350, 110), Plataforma(400, 110),
                Plataforma(450, 110), Plataforma(500, 110), Plataforma(550, 110),
                Plataforma(600, 110))

plataforma_lvls = (plataforma_lvl1, plataforma_lvl2, plataforma_lvl3, plataforma_lvl4, plataforma_lvl5, plataforma_lvl6)

luke = Luke()

escadas = (Escada(650, 580), Escada(100, 460),
           Escada(650, 348), Escada(100, 236), Escada(600, 130))

darth_vezzi = Darth_vezzi()

zeros = []

phyton = Phyton()

luke.hit_zero()
def botao(mensagem, x, y, largura, altura, cor1, cor2, pos_letra, acao = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x+largura > mouse[0] > x and y + altura > mouse[1] > y:
                pygame.draw.rect(screen, cor1, (x, y, largura, altura))
                if click[0] == 1 and acao != None:
                        if acao == 'caguei':
                                intro = False
                                return intro
                        elif acao == 'quit':
                                pygame.quit()
                                quit()
        else:
                pygame.draw.rect(screen, cor2, (x, y, largura, altura))

        screen.blit(fonte.render(mensagem, True, (0, 0, 0)), pos_letra)
        
def game_intro(intro):
        
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		screen.blit(menu_vezzi, (0,0))
		screen.blit(fonte.render("A luta contra os zeros", True, (0, 0, 0)), (250, 540))
		
		if 150 + 100 > mouse[0] > 150 and 600 + 50 > mouse[1] > 600:
			pygame.draw.rect(screen, [0,255, 0], (150, 600, 100, 50))
			if click[0] == 1 and 150 + 100 > mouse[0] > 150 and 600 + 50 > mouse[1] > 600:
				intro = False
				return False
		elif click[0] == 1 and 550 + 100 > mouse[0] > 550 and 600 + 50 > mouse[1] > 600:
			pygame.quit()
			quit()
		else:
			pygame.draw.rect(screen, [0,200,0], (150, 600, 100, 50,))

		screen.blit(fonte.render("Ir a aula", True, (0, 0, 0)), (153, 600))

		if 550 + 100 > mouse[0] > 550 and 600 + 50 > mouse[1] > 600:
			pygame.draw.rect(screen, [255,0, 0], (550, 600, 100, 50))
		elif click[0] == 1 and 550 + 100 > mouse[0] > 550 and 600 + 50 > mouse[1] > 600:
			pygame.quit()
			quit()
		else:
			pygame.draw.rect(screen, [200,0,0], (550, 600, 100, 50,))

		screen.blit(fonte.render("Trancar", True, (0, 0, 0)), (555, 600))
			
		pygame.display.update()
		clock.tick(15)

intro = True
re = game_intro(intro)
if re == False:
        pygame.mixer.music.play(-1)
        
while True:
        
        clock.tick(60)
        
        screen.fill((0, 0, 0))
        
        pressed_keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        quit()
        
        for plataforma_lvl in plataforma_lvls:
                for plataforma in plataforma_lvl:
                        plataforma.draw()
        
        for escada in escadas:
                escada.draw()
        
        i = 0
        while i < len(zeros):
                zeros[i].move()
                zeros[i].cair()
                zeros[i].draw()
                if zeros[i].fim_tela():
                        del zeros[i]
                        i -= 1
                        
                i += 1
        
        if luke.level_num == 6:
                darth_vezzi.lost = True
                
        if not darth_vezzi.lost:
                darth_vezzi.pick_move()
                darth_vezzi.animacao()
                darth_vezzi.draw()
        
        elif darth_vezzi.lost:
                darth_vezzi.perder()
        
        if not darth_vezzi.y > 151:
                phyton.animate()
                phyton.draw()
        else:
                phyton.img = python_parado
                phyton.draw()
        
        if luke.hit_zero():
                luke.lost = True
        
        if not luke.lost:
                if not luke.level_num == 6:
                        luke.movimento()
                        luke.gravidade()
                        luke.escalar()
                        luke.animacao()
                        luke.hit_zero()
                
                elif luke.level_num == 6:
                        luke.ganhar()
                        luke.animacao()
                        if luke.zero and luke.zero.y <= -50:
                                luke = Luke()
                                phyton = Phyton()
                                darth_vezzi = Darth_vezzi()
                                zeros = []
                        
                luke.draw()
                
        elif luke.lost:
                luke.perder()
        
        if luke.y >= 800:
                luke = Luke()
        
        if luke.zero:
                luke.zero.draw()
                
        pygame.display.update ()
