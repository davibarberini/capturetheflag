import pygame
import json
from cenario import Cenario
from pygame import FULLSCREEN, QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()

scr = pygame.display.set_mode((1020, 760), FULLSCREEN, 32)

clock = pygame.time.Clock()


"""mapa = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 5, 5, 5, 5, 5, 0, 0, 0, 4, 0, 0, 0, 5, 5, 5, 5, 5, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
mapfile = open("defaultmap.json", "w")
mapfile.write(str(mapa))
mapfile.close()
"""
mapfile = open("defaultmap.json", "r")
mapa = json.load(mapfile)
mapfile.close()

mapsize = 40

dictmap = []


tijolos = [{"nome": "vazio", "indice": 0, "cor": (0, 0, 0)},
           {"nome": "chao", "indice": 1, "cor": (255, 255, 255)},
           {"nome": "gelo", "indice": 2, "cor": (55, 55, 255)},
           {"nome": "spawn", "indice": 3, "cor": (0, 255, 0)},
           {"nome": "flag", "indice": 4, "cor": (255, 0, 0)},
           {"nome": "spike", "indice": 5, "cor": (100, 100, 100)}]


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


def gameloop(playercount):
    cenario = Cenario(scr, dictmap, tijolos, mapa, playercount)
    run = True
    while run:
        clock.tick(120)
        scr.fill((0, 0, 0))

        #update
        cenario.update()
        #draw
        cenario.draw()
        #eventos
        cenario.eventos()

        pygame.display.update()

def mainmenu():
    startimg = pygame.image.load("assets/menu/start.png").convert_alpha()
    mapeditorimg = pygame.image.load("assets/menu/mapeditor.png").convert_alpha()
    playercountimg = pygame.image.load("assets/menu/tutorial.png").convert_alpha()
    startrect = startimg.get_rect()
    playercountrect = playercountimg.get_rect()
    mapeditorrect = mapeditorimg.get_rect()
    start = {"x": 400, "y": 300, "w": startrect.w, "h": startrect.h}
    mapeditor = {"x": 380, "y": 500, "w": mapeditorrect.w, "h": mapeditorrect.h}
    playercountdict = {"x": 380, "y": 600, "w": playercountrect.w, "h": playercountrect.h}
    playercount = 1
    font = pygame.font.SysFont("Arial", 48, True, False)

    run = True
    while run:
        clock.tick(120)

        scr.fill((0, 0, 0))

        #draw
        playercountfont = font.render(str(playercount), True, (255, 255, 0))
        scr.blit(mapeditorimg, (mapeditor["x"], mapeditor["y"]))
        scr.blit(startimg, (start["x"], start["y"]))
        scr.blit(playercountimg, (playercountdict["x"], playercountdict["y"]))
        scr.blit(playercountfont, (playercountdict["x"] + 200, playercountdict["y"]))

        #update
        mouse = pygame.mouse.get_pos()

        #eventos
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if mousecolide(start, mouse):
                        for col in range(mapsize):
                            for lin in range(mapsize):
                                for item in tijolos:
                                    if item["indice"] == mapa[col][lin]:
                                        itemnew = {"indice": item["indice"], "rect":[lin * 25.5, col * 19, 25.5, 19]}
                                        dictmap.append(itemnew)
                        print(dictmap)
                        gameloop(playercount)
                    elif mousecolide(mapeditor, mouse):
                        mapeditorloop()
                    elif mousecolide(playercountdict, mouse):
                        playercount += 1
                        if playercount >= 5:
                            playercount = 1

        pygame.display.update()


def mapeditorloop():
    startimg = pygame.image.load("assets/menu/start.png").convert_alpha()
    startrect = startimg.get_rect()
    start = {"x": 100, "y": 500, "w": startrect.w, "h": startrect.h}
    saveimg = pygame.image.load("assets/menu/tutorial.png").convert_alpha()
    saverect = saveimg.get_rect()
    save = {"x": 100, "y": 600, "w": saverect.w, "h": saverect.h}
    tijoloseditor = []

    clicando = False

    count = 0
    for bloco in tijolos:
        tijoloseditor.append({"nome":bloco["nome"], "indice": bloco["indice"],"cor": bloco["cor"], "rect": [30 + (count * 30), 10, 12.75, 9.5]})
        count += 1

    selected = 0

    run = True
    while run:
        clock.tick(120)
        scr.fill((50, 50, 50))

        #update
        mouse = pygame.mouse.get_pos()
        (xm, ym) = mouse
        colr = int((xm - 300) // 12.75)
        linr = int((ym - 250) // 9.5)


        #draw
        for col in range(mapsize):
            for lin in range(mapsize):
                for bloco in tijolos:
                    if bloco["indice"] == mapa[col][lin]:
                        pygame.draw.rect(scr, bloco["cor"], [300 + (lin * 12.75) , 250 + (col * 9.5), 12.75 , 9.5])

        scr.blit(startimg, (start["x"], start["y"]))
        scr.blit(saveimg, (save["x"], save["y"]))
        for bloco in tijoloseditor:
            pygame.draw.rect(scr, bloco["cor"], bloco["rect"])

        if xm > 300 and ym > 250 and xm < 810 and ym < 630:
            if clicando:
                mapa[linr][colr] = selected
            for bloco in tijoloseditor:
                if selected == bloco["indice"]:
                    xr = (colr * 12.75) + 300
                    yr = (linr * 9.5) + 250
                    pygame.draw.rect(scr, bloco["cor"], [xr, yr, 12.75, 9.5])
        else:
            for bloco in tijoloseditor:
                if selected == bloco["indice"]:
                    pygame.draw.rect(scr, bloco["cor"], [xm, ym, 12.75, 9.5])
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