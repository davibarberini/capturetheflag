import player
import pygame
from pygame import *

class Cenario(object):
    def __init__(self, scr, dictmap, tijolos, mapa, playercount):
        self.scr = scr
        self.playercount = playercount
        self.plyrect = [0, 0, 12.5, 19]
        self.plyspawn = [0, 0, 12.5, 19]
        if self.playercount > 1:
            self.ply2rect = [0, 0, 12.5, 19]
            self.ply2spawn = [0, 0, 12.5, 19]
        if self.playercount > 2:
            self.ply3rect = [0, 0, 12.5, 19]
            self.ply3spawn = [0, 0, 12.5, 19]
        if self.playercount > 3:
            self.ply4rect = [0, 0, 12.5, 19]
            self.ply4spawn = [0, 0, 12.5, 19]
        self.flagrect = [0, 0, 6.5, 10]
        self.count = 1
        self.dictmap = dictmap
        for bloco in self.dictmap:
            if bloco["indice"] == 3:
                if self.count == 1:
                    self.plyrect[0] = bloco["rect"][0]
                    self.plyrect[1] = bloco["rect"][1]
                    self.plyspawn[0] = bloco["rect"][0]
                    self.plyspawn[1] = bloco["rect"][1]
                    self.count += 1
                elif self.count == 2 and self.playercount > 1:
                    self.ply2rect[0] = bloco["rect"][0]
                    self.ply2rect[1] = bloco["rect"][1]
                    self.ply2spawn[0] = bloco["rect"][0]
                    self.ply2spawn[1] = bloco["rect"][1]
                    self.count += 1
                elif self.count == 3 and self.playercount > 2:
                    self.ply3rect[0] = bloco["rect"][0]
                    self.ply3rect[1] = bloco["rect"][1]
                    self.ply3spawn[0] = bloco["rect"][0]
                    self.ply3spawn[1] = bloco["rect"][1]
                    self.count += 1
                elif self.count == 4 and self.playercount > 3:
                    self.ply4rect[0] = bloco["rect"][0]
                    self.ply4rect[1] = bloco["rect"][1]
                    self.ply4spawn[0] = bloco["rect"][0]
                    self.ply4spawn[1] = bloco["rect"][1]
                    self.count = 1
            elif bloco["indice"] == 4:
                self.flagrect[0] = bloco["rect"][0]
                self.flagrect[1] = bloco["rect"][1]
        self.ply = player.Player(self.plyrect, (0, 0, 255), self.scr, [K_RIGHT, K_LEFT, K_UP], self.plyspawn)
        if self.playercount > 1:
            self.ply2 = player.Player(self.ply2rect, (0, 255, 0), self.scr, [K_d, K_a, K_w], self.ply2spawn)
        if self.playercount > 2:
            self.ply3 = player.Player(self.ply3rect, (255, 0, 0), self.scr, [K_n, K_v, K_g], self.ply3spawn)
        if self.playercount > 3:
            self.ply4 = player.Player(self.ply4rect, (255, 255, 0), self.scr, [K_l, K_j, K_i], self.ply4spawn)
        self.flag = Flag(self.flagrect, (0, 255, 255), self.scr)
        self.tijolos = tijolos
        self.mapa = mapa

    def update(self):
        self.ply.update()
        if self.flag.owner == 1:
            self.flag.rect[0] = self.ply.rect[0] + 5
            self.flag.rect[1] = self.ply.rect[1] - 10
            self.ply.score += 1
        self.ply.colisao(self.dictmap)
        ply1Rect = pygame.Rect(self.ply.rect)
        flagRect = pygame.Rect(self.flag.rect)
        if ply1Rect.colliderect(flagRect):
            self.flag.owner = 1
        if self.playercount > 1:
            self.ply2.update()
            if self.flag.owner == 2:
                self.flag.rect[0] = self.ply2.rect[0] + 5
                self.flag.rect[1] = self.ply2.rect[1] - 10
                self.ply2.score += 1
            self.ply2.colisao(self.dictmap)
            ply2Rect = pygame.Rect(self.ply2.rect)
            if ply2Rect.colliderect(flagRect):
                self.flag.owner = 2
            if ply1Rect.colliderect(ply2Rect):
                if self.ply2.vulnerable:
                    if self.flag.owner == 2:
                        self.flag.owner = 1
                        self.ply.vulnerable = False
                if self.ply.vulnerable:
                    if self.flag.owner == 1:
                        self.flag.owner = 2
                        self.ply2.vulnerable = False

        if self.playercount > 2:
            self.ply3.update()
            if self.flag.owner == 3:
                self.flag.rect[0] = self.ply3.rect[0] + 5
                self.flag.rect[1] = self.ply3.rect[1] - 10
                self.ply3.score += 1
            self.ply3.colisao(self.dictmap)
            ply3Rect = pygame.Rect(self.ply3.rect)
            ply2Rect = pygame.Rect(self.ply2.rect)
            if ply3Rect.colliderect(flagRect):
                self.flag.owner = 3
            if ply1Rect.colliderect(ply3Rect):
                if self.ply3.vulnerable:
                    if self.flag.owner == 3:
                        self.flag.owner = 1
                        self.ply.vulnerable = False
                if self.ply.vulnerable:
                    if self.flag.owner == 1:
                        self.flag.owner = 3
                        self.ply3.vulnerable = False
            elif ply2Rect.colliderect(ply3Rect):
                if self.ply3.vulnerable:
                    if self.flag.owner == 3:
                        self.flag.owner = 2
                        self.ply2.vulnerable = False
                if self.ply2.vulnerable:
                    if self.flag.owner == 2:
                        self.flag.owner = 3
                        self.ply3.vulnerable = False
        if self.playercount > 3:
            self.ply4.update()
            if self.flag.owner == 4:
                self.flag.rect[0] = self.ply4.rect[0] + 5
                self.flag.rect[1] = self.ply4.rect[1] - 10
                self.ply4.score += 1
            self.ply4.colisao(self.dictmap)
            ply4Rect = pygame.Rect(self.ply4.rect)
            ply3Rect = pygame.Rect(self.ply3.rect)
            ply2Rect = pygame.Rect(self.ply2.rect)
            if ply4Rect.colliderect(flagRect):
                self.flag.owner = 4
            if ply1Rect.colliderect(ply4Rect):
                if self.ply4.vulnerable:
                    if self.flag.owner == 4:
                        self.flag.owner = 1
                        self.ply.vulnerable = False
                if self.ply.vulnerable:
                    if self.flag.owner == 1:
                        self.flag.owner = 4
                        self.ply4.vulnerable = False
            elif ply2Rect.colliderect(ply4Rect):
                if self.ply4.vulnerable:
                    if self.flag.owner == 4:
                        self.flag.owner = 2
                        self.ply2.vulnerable = False
                if self.ply2.vulnerable:
                    if self.flag.owner == 2:
                        self.flag.owner = 4
                        self.ply4.vulnerable = False
            elif ply3Rect.colliderect(ply4Rect):
                if self.ply4.vulnerable:
                    if self.flag.owner == 4:
                        self.flag.owner = 3
                        self.ply3.vulnerable = False
                if self.ply3.vulnerable:
                    if self.flag.owner == 3:
                        self.flag.owner = 4
                        self.ply4.vulnerable = False

    def draw(self):
        for col in range(40):
            for lin in range(40):
                for bloco in self.tijolos:
                    if bloco["indice"] == self.mapa[col][lin]:
                        if bloco["indice"] == 3:
                            pygame.draw.rect(self.scr, (0, 0, 0), [lin * 25.5, col * 19, 25.5, 19])
                        elif bloco["indice"] == 4:
                            pygame.draw.rect(self.scr, (0, 0, 0), [lin * 25.5, col * 19, 25.5, 19])
                        else:
                            pygame.draw.rect(self.scr, bloco["cor"], [lin * 25.5, col * 19, 25.5, 19])
        self.scr.blit(self.ply.scoreimg, (10, 10))
        self.ply.draw()
        if self.playercount > 1:
            self.scr.blit(self.ply2.scoreimg, (260, 10))
            self.ply2.draw()
        if self.playercount > 2:
            self.ply3.draw()
            self.scr.blit(self.ply3.scoreimg, (510, 10))
        if self.playercount > 3:
            self.ply4.draw()
            self.scr.blit(self.ply4.scoreimg, (760, 10))
        self.flag.draw()

    def eventos(self, e):
        if self.playercount > 3:
            player.eventos(self.playercount, self.ply, e, self.ply2, self.ply3, self.ply4)
        elif self.playercount > 2:
            player.eventos(self.playercount, self.ply, e, self.ply2, self.ply3)
        elif self.playercount > 1:
            player.eventos(self.playercount, self.ply, e, self.ply2)
        else:
            player.eventos(self.playercount, self.ply, e)


class Flag(object):
    def __init__(self, rect, cor, scr):
        self.rect = rect
        self.cor = cor
        self.scr = scr
        self.owner = 0

    def draw(self):
        pygame.draw.rect(self.scr, self.cor, self.rect, 0)
