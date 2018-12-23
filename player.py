import pygame
from pygame import KEYDOWN, KEYUP, QUIT, K_ESCAPE
from pygame import *

class Player(object):
    def __init__(self, rect, cor, scr, keys):
        self.rect = rect
        self.cor = cor
        self.velx = 0
        self.vely = 0
        self.scr = scr
        self.keys = keys
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 40, True, False)
        self.vulnerable = True
        self.countvulnerable = 0
        self.slow = False
        self.slow2 = False

    def update(self):
        self.scoreimg = self.font.render("Score: " + str(self.score), True, self.cor)
        self.prect = pygame.Rect(self.rect)
        if self.slow2:
            if self.velx > 0:
                self.velx -= 0.05
            elif self.velx < 0:
                self.velx += 0.05
        if self.velx == 0:
            self.slow2 = False
            self.slow = False
        self.rect[0] += self.velx
        self.rect[1] += self.vely
        self.vely += 0.2
        if not self.vulnerable:
            if self.countvulnerable > 100:
                self.vulnerable = True
                self.countvulnerable = 0
            self.countvulnerable += 1

    def draw(self):
        pygame.draw.rect(self.scr, self.cor, self.rect, 0)

    def colisao(self, dictmap):
        self.dictmap = dictmap
        for b in self.dictmap:
            if b["indice"] == 1:
                if self.prect.colliderect(b["rect"]):
                    self.vely = 0
                    self.rect[1] -= 1
                    if self.velx != 5 and self.velx != -5:
                        self.velx = 0
                    self.slow2 = False
                    self.slow = False
            elif b["indice"] == 2:
                if self.prect.colliderect(b["rect"]):
                    self.vely = 0
                    self.slow = True

        # if ply.rect[1] > 700:
        #   ply.rect[1] = 700
        if self.rect[0] > 980:
            self.rect[0] = 980
        elif self.rect[0] < 0:
            self.rect[0] = 0




"""def eventoss(ply):

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == ply.keys[0]:
                ply.velx = 5
            elif e.key == ply.keys[1]:
                ply.velx = -5
            elif e.key == ply.keys[2]:
                ply.vely = -6
            elif e.key == K_ESCAPE:
                from main import mainmenu
                mainmenu()
        elif e.type == KEYUP:
            if e.key == ply.keys[0] and ply.velx > 0:
                ply.velx = 0
            elif e.key == ply.keys[1] and ply.velx < 0:
                ply.velx = 0
"""

def eventos(ply, ply2, ply3, ply4):

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                ply.velx = 5
            elif e.key == K_LEFT:
                ply.velx = -5
            elif e.key == K_UP:
                ply.vely = -6
            elif e.key == K_d:
                ply2.velx = 5
            elif e.key == K_a:
                ply2.velx = -5
            elif e.key == K_w:
                ply2.vely = -6
            elif e.key == K_l:
                ply3.velx = 5
            elif e.key == K_j:
                ply3.velx = -5
            elif e.key == K_i:
                ply3.vely = -6
            elif e.key == K_n:
                ply4.velx = 5
            elif e.key == K_v:
                ply4.velx = -5
            elif e.key == K_g:
                ply4.vely = -6
            elif e.key == K_ESCAPE:
                from main import mainmenu
                mainmenu()
        elif e.type == KEYUP:
            if e.key == K_RIGHT and ply.velx > 0:
                if not ply.slow:
                    ply.velx = 0
                else:
                    ply.slow2 = True
            elif e.key == K_LEFT and ply.velx < 0:
                if not ply.slow:
                    ply.velx = 0
                else:
                    ply.slow2 = True
            elif e.key == K_d and ply2.velx > 0:
                if not ply2.slow:
                    ply2.velx = 0
                else:
                    ply2.slow2 = True
            elif e.key == K_a and ply2.velx < 0:
                if not ply2.slow:
                    ply2.velx = 0
                else:
                    ply2.slow2 = True
            elif e.key == K_l and ply3.velx > 0:
                if not ply3.slow:
                    ply3.velx = 0
                else:
                    ply3.slow2 = True
            elif e.key == K_j and ply3.velx < 0:
                if not ply3.slow:
                    ply3.velx = 0
                else:
                    ply3.slow2 = True
            elif e.key == K_n and ply4.velx > 0:
                if not ply4.slow:
                    ply4.velx = 0
                else:
                    ply4.slow2 = True
            elif e.key == K_v and ply4.velx < 0:
                if not ply4.slow:
                    ply4.velx = 0
                else:
                    ply4.slow2 = True

