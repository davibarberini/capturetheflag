import pygame
import json
from pygame import FULLSCREEN, QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()

scr = pygame.display.set_mode((1020, 760), 0, 32)

clock = pygame.time.Clock()


mapfile = open("defaultmap.json", "r")
mapa = json.load(mapfile)
mapfile.close()



tijolos = [{"nome": "chao", "indice": 1, "cor": (255, 255, 255)},
           {"nome": "vazio", "indice": 0, "cor": (0, 0, 0)}]


def mousecolide(dict, mousepos, rect = False):
    if rect:
        dictrect = pygame.Rect(dict["rect"])
        if dictrect.collidepoint(mousepos):
            return True
        else:
            return False
    else:
        dictrect = pygame.Rect([dict["x"], dict["y"], dict["w"], dict["h"]])
        if dictrect.collidepoint(mousepos):
            return True
        else:
            return False


def gameloop():
    run = True
    while run:
        clock.tick(120)
        scr.fill((0, 0, 0))

        for col in range(20):
            for lin in range(20):
                for bloco in tijolos:
                    if bloco["indice"] == mapa[col][lin]:
                        pygame.draw.rect(scr, bloco["cor"], [lin * 51, col * 38, 51, 38])

        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False

        pygame.display.update()

def mainmenu():
    startimg = pygame.image.load("assets/menu/start.png").convert_alpha()
    mapeditorimg = pygame.image.load("assets/menu/mapeditor.png").convert_alpha()
    startrect = startimg.get_rect()
    mapeditorrect = mapeditorimg.get_rect()
    start = {"x": 400, "y": 300, "w": startrect.w, "h": startrect.h}
    mapeditor = {"x": 380, "y": 500, "w": mapeditorrect.w, "h": mapeditorrect.h}

    run = True
    while run:
        clock.tick(120)

        scr.fill((0, 0, 0))

        #draw
        scr.blit(mapeditorimg, (mapeditor["x"], mapeditor["y"]))
        scr.blit(startimg, (start["x"], start["y"]))

        #update
        mouse = pygame.mouse.get_pos()

        #eventos
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if mousecolide(start, mouse):
                        gameloop()
                    elif mousecolide(mapeditor, mouse):
                        mapeditorloop()

        pygame.display.update()


def mapeditorloop():
    startimg = pygame.image.load("assets/menu/start.png").convert_alpha()
    startrect = startimg.get_rect()
    start = {"x": 100, "y": 500, "w": startrect.w, "h": startrect.h}
    saveimg = pygame.image.load("assets/menu/tutorial.png").convert_alpha()
    saverect = startimg.get_rect()
    save = {"x": 100, "y": 600, "w": startrect.w, "h": startrect.h}
    tijoloseditor = []

    clicando = False

    count = 0
    for bloco in tijolos:
        tijoloseditor.append({"nome":bloco["nome"], "indice": bloco["indice"],"cor": bloco["cor"], "rect": [30 + (count * 30), 10, 25.5, 19]})
        count += 1

    selected = 0

    run = True
    while run:
        clock.tick(120)
        scr.fill((0, 0, 255))

        #update
        mouse = pygame.mouse.get_pos()
        (xm, ym) = mouse
        colr = int((xm - 300) // 25.5)
        linr = int((ym - 250) // 19)


        #draw
        for col in range(20):
            for lin in range(20):
                for bloco in tijolos:
                    if bloco["indice"] == mapa[col][lin]:
                        pygame.draw.rect(scr, bloco["cor"], [300 + (lin * 25.5) , 250 + (col * 19), 25.5 , 19])

        scr.blit(startimg, (start["x"], start["y"]))
        scr.blit(saveimg, (save["x"], save["y"]))
        for bloco in tijoloseditor:
            pygame.draw.rect(scr, bloco["cor"], bloco["rect"])

        if xm > 300 and ym > 250 and xm < 810 and ym < 630:
            if clicando:
                mapa[linr][colr] = selected
            for bloco in tijoloseditor:
                if selected == bloco["indice"]:
                    xr = (colr * 25.5) + 300
                    yr = (linr * 19) + 250
                    pygame.draw.rect(scr, bloco["cor"], [xr, yr, 25.5, 19])
        else:
            for bloco in tijoloseditor:
                if selected == bloco["indice"]:
                    pygame.draw.rect(scr, bloco["cor"], [xm, ym, 25.5, 19])
        #eventos
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if mousecolide(start, mouse):
                        run = False
                    elif mousecolide(save, mouse):
                        mapfile = open("defaultmap.json", "w")
                        mapfile.write(str(mapa))
                        mapfile.close()
                    for bloco in tijoloseditor:
                        if mousecolide(bloco, mouse, True):
                            selected = bloco["indice"]
                    if xm > 300 and ym > 250 and xm < 810 and ym < 630:
                        clicando = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    clicando = False

        pygame.display.update()

mainmenu()