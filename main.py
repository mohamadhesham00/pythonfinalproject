import pygame
pygame.init()
grey=(192,192,192)
red=(139,0,0)
green=(0,255,0)
black=(0,0,0)
blue = (25, 25, 112)
windowSize=[600,600]
gameDisplay= pygame.display.set_mode((windowSize))
xx=230
yy=506
steps=0
font =pygame.font.SysFont(None,100)
def worl_message(msg,color):
    window.fill(black)
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,(100,250))

def main():

    pygame.init()
    gameDisplay = pygame.display.set_mode(windowSize)
    pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            pygame.quit()
            exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if i.type == pygame.KEYDOWN:
                yy -= 46
                steps += 1
        if key[pygame.K_DOWN]:
            if i.type == pygame.KEYDOWN:
                yy += 46
                steps+=1
        if key[pygame.K_RIGHT]:
            if i.type == pygame.KEYDOWN:
                xx += 46
                steps += 1
        if key[pygame.K_LEFT]:
            if i.type == pygame.KEYDOWN:
                xx -= 46
                steps += 1
    window = pygame.display.set_mode(windowSize)
    window.fill(black)

    x = 0
    y = 0
    t = 0

    n=13
    for i in range(13):
        for j in range (13):
            m = 0
            x=0
            if i==0 :
                while m <13:
                    pygame.draw.rect(window, blue, [ 0+ x, 0, 45, 45])
                    x+=46
                    m+=1
            elif i == 12:
                while m < 13:
                    pygame.draw.rect(window, blue, [0 + x, 552, 45, 45])
                    x += 46
                    m += 1
            elif i == 6:
                pygame.draw.rect(window, blue, [0 + x, y, 45, 45])
                for l in range(11):
                    pygame.draw.rect(window, grey, [46 + x, y, 45, 45])
                    x += 46
                pygame.draw.rect(window, green, [x + 46, y, 45, 45])
            elif i != 0 and i != 12 and i != 6:
                pygame.draw.rect(window, blue, [0 + x, y, 45, 45])
                for l in range(11):
                    pygame.draw.rect(window, grey, [46 + x, y, 45, 45])
                    x += 46
                pygame.draw.rect(window, blue, [x + 46, y, 45, 45])

            elif i!=0 and i !=12:
                pygame.draw.rect(window, blue, [0+ x, y, 45, 45])
                for l in range(11):
                    pygame.draw.rect(window, grey, [46 + x, y, 45, 45])
                    x+=46
                pygame.draw.rect(window, blue, [ x+46, y, 45, 45])
        y+=46
    catimag = pygame.image.load("CAT.png")
    window.blit(pygame.transform.scale(catimag, (45, 45)), (460, 368))

    mouseimag = pygame.image.load("mouse.png")
    window.blit(pygame.transform.scale(mouseimag, (45, 45)), (xx, yy))
    if (xx == 0) or (yy == 0) or (yy == 552) or (xx == 552 and yy != 276) or (steps>=20) or(xx==460 and yy==368):
        worl_message("GAME OVER",red)
    if(xx==552 and yy==276):
        worl_message("you win",red)
    pygame.display.update()
