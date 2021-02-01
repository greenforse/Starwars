import pygame
pygame.init()
import random
win=pygame.display.set_mode((600,800))
pygame.display.set_caption("Rocket Batle")
Rocket=pygame.image.load("rocket_2.jpg")
def ataka(x,y,wirina,speed):
    GREEN = (0, 225, 0)
    for i in range (4):
        coord_fly_y-=speed
        pygame.draw.circle(win,GREEN,(x,y),10)
        pygame.display.update()
def ataka_1(x,y,wirina,speed):
    vistrel=False
    WHITE = (255, 255, 255)
    RED = (225, 0, 50)
    GREEN = (0, 225, 0)
    BLUE = (0, 0, 225)
    if vistrel==False:
        coord_fly_x=x+wirina//2
        coord_fly_y=y-10
        vistrel=True
    if vistrel:
        coord_fly_y-=speed_snaryad
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),10)
        pygame.display.update()
        #if cel[0]>300:
        #    coord_fly_x+=speed_1
        #else:
        #    coord_fly_x-=speed_1
        ##if cel[1]>400:
        ##    coord_fly_y+=speed_2
        ##else:
        #coord_fly_y-=speed_2
        #pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),10)
        #pygame.display.update()
        if coord_fly_y<=0:
            vistrel=False
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
x=300
y=700
wirina=30
dlina=50
speed=3
speed_snaryad=20
coord_fly_x=x+wirina//2
coord_fly_y=y
run=True
count_blur=0
vistrel=False
speed_1=0
speed_2=0
count_vistrel=0
vrag_1=False
vrag_2=False
speed_vrag=1
popadenie_1=False
snaryad_vraga_x=0
snaryad_vraga_y=0
snaryad_vraga=False
speed_snaryad_1=5
snaryad_vraga_x_1=0
snaryad_vraga_y_1=0
snaryad_vraga_1=False
count_pop=0
delitel_1=200
delitel_2=300
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(win, RED, event.pos, 10)
                cel=event.pos
                print(cel)
                coord_fly_x=x+wirina//2
                coord_fly_y=y-10
                speed_1=(cel[0]-coord_fly_x) //(cel[1]-coord_fly_y)
                if speed_1<1:
                    speed_1=1
                speed_2=(cel[1]-coord_fly_y)//(cel[0]-coord_fly_x)
                if speed_2<1:
                    speed_2=1
                vistrel=True
                pygame.display.update()
    #if vistrel:
    #coord_fly_x=x+wirina//2
    #coord_fly_y=y-10
    #coord_fly_x+=speed_1
    #coord_fly_y+=speed_2
    #pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),10)
    #pygame.display.update()
    #win.blit(Rocket,(x,y))
    pygame.draw.rect(win,(0,0,255),(x,y,wirina,dlina))
    pygame.display.update()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
    if keys[pygame.K_RIGHT] and x<600-10-wirina:
        x+=speed
    if keys[pygame.K_DOWN] and y<800-10-dlina:
        y+=speed
    if keys[pygame.K_UP] and y>400:
        y-=speed
    if keys[pygame.K_SPACE] and vistrel==False:
        coord_fly_x=x+wirina//2
        coord_fly_y=y-10
        vistrel=True
    if vistrel:
        coord_fly_y-=speed_snaryad
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),5)
        pygame.display.update()
        if coord_fly_y<1:
            vistrel=False
    if vrag_1==False:
        x_vrag_1=random.randint(0,600)
        y_vrag_1=random.randint(0,400)
        pygame.draw.rect(win,(GREEN),(x_vrag_1,y_vrag_1,30,30))
        pygame.display.update()
        naprx=1
        napry=1
        vrag_1=True
    if vrag_1:
        x_vrag_1+=speed_vrag * naprx
        y_vrag_1+=speed_vrag * napry
        pygame.draw.rect(win,(GREEN),(x_vrag_1,y_vrag_1,30,30))
        pygame.display.update()
        if x_vrag_1>600-30:
            naprx=-1
        if x_vrag_1<1:
            naprx=1
        if y_vrag_1<1:
            napry=1
        if y_vrag_1>400:
            napry=-1
    if coord_fly_x > x_vrag_1 and coord_fly_x < x_vrag_1+30 and coord_fly_y > y_vrag_1 and coord_fly_y < y_vrag_1 + 30:
        vrag_1=False
        vistrel=False
        count_pop+=1
        if count_pop%5==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=3
            delitel_1-=15
            delitel_2-=15
    if vrag_2==False:
        x_vrag_2=random.randint(0,600)
        y_vrag_2=random.randint(0,400)
        pygame.draw.rect(win,(255,255,0),(x_vrag_2,y_vrag_2,30,30))
        pygame.display.update()
        naprx_2=1
        napry_2=1
        vrag_2=True
    if vrag_2:
        x_vrag_2+=speed_vrag * naprx_2
        #y_vrag_2+=speed_vrag * napry
        pygame.draw.rect(win,(255,255,0),(x_vrag_2,y_vrag_2,30,30))
        pygame.display.update()
        if x_vrag_2>600-30:
            naprx_2=-1
        if x_vrag_2<1:
            naprx_2=1
        if y_vrag_2<1:
            napry_2=1
        if y_vrag_2>400:
            napry_2=-1
    if coord_fly_x > x_vrag_2 and coord_fly_x < x_vrag_2+30 and coord_fly_y > y_vrag_2 and coord_fly_y < y_vrag_2 + 30:
        vrag_2=False
        vistrel=False
        delitel_1-=15
        delitel_2-=15
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        count_pop+=1
        if count_pop%5==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=3
    if count_blur%delitel_1==0:
        snaryad_vraga_x=x_vrag_1
        snaryad_vraga_y=y_vrag_1
        snaryad_vraga=True
    if snaryad_vraga:
        snaryad_vraga_y+=speed_snaryad_1
        pygame.draw.circle(win,RED,(snaryad_vraga_x,snaryad_vraga_y),5)
        pygame.display.update()
    if count_blur%delitel_2==0:
        snaryad_vraga_x_1=x_vrag_2
        snaryad_vraga_y_1=y_vrag_2
        snaryad_vraga_1=True
    if snaryad_vraga_1:
        snaryad_vraga_y_1+=speed_snaryad_1
        pygame.draw.circle(win,RED,(snaryad_vraga_x_1,snaryad_vraga_y_1),5)
        pygame.display.update()
    if snaryad_vraga_x > x and snaryad_vraga_x < x + wirina and snaryad_vraga_y > y and snaryad_vraga_y < y + dlina or snaryad_vraga_x_1 > x and snaryad_vraga_x_1 < x + wirina and snaryad_vraga_y_1 > y and snaryad_vraga_y_1 < y + dlina:
        run=False
    count_blur+=1
    #if count_blur%2==0:
    win.fill((0,0,0))
    