import pygame
pygame.init()
import random
win=pygame.display.set_mode((600,800))
pygame.display.set_caption("Rocket Batle")
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK= (0,0,0)
x=300
y=700
wirina=70
dlina=70
speed=5
speed_snaryad=20
coord_fly_x=x+wirina//2
coord_fly_y=y
coord_fly_x_1=x+wirina//2
coord_fly_y_1=y
vistrel_1=False
vistrel_2=False
run=True
count_blur=0
vistrel=False
speed_1=0
speed_2=0
count_vistrel=0
vrag_1=False
vrag_2=False
vrag_3=False
speed_vrag=1
popadenie_1=False
snaryad_vraga_x=0
snaryad_vraga_y=0
snaryad_vraga=False
speed_snaryad_1=5
snaryad_vraga_x_1=0
snaryad_vraga_y_1=0
snaryad_vraga_1=False
snaryad_vraga_2=False
count_pop=0
delitel_1=300
delitel_2=400
Rocket=pygame.image.load("Korabl_2.jpg")
Rocket_1 = pygame.transform.scale(Rocket, (wirina, dlina))
Rocket_1.set_colorkey(WHITE)
jpeg_vrag=pygame.image.load("Vrag_8.jpg")
jpeg_vrag_1 = pygame.transform.scale(jpeg_vrag, (70,70 ))
jpeg_vrag_1.set_colorkey(WHITE)
jpeg_vrag=pygame.image.load("Vrag_9.jpg")
jpeg_vrag_2 = pygame.transform.scale(jpeg_vrag, (70,70 ))
jpeg_vrag_2.set_colorkey(WHITE)
jpeg_vrag=pygame.image.load("Vrag_7.jpg")
jpeg_vrag_3 = pygame.transform.scale(jpeg_vrag, (70,70 ))
jpeg_vrag_3.set_colorkey(BLACK)
Fon=pygame.image.load("Fon_1.jpg")
Fon_1 = pygame.transform.scale(Fon, (600,800))
Fon=pygame.image.load("Fon_2.jpg")
Fon_2 = pygame.transform.scale(Fon, (600,800))
wait_respawn=0
wait_respawn_1=0
wait_respawn_2=0
wait_snaryad=0
wait_snaryad_1=0
wait_snaryad_2=0
while run:
    pygame.time.delay(20)
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
    win.blit((Fon_1),(0,0))
    win.blit((Rocket_1),(x,y))
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
    if keys[pygame.K_SPACE] and vistrel==False :
        if vistrel==False:
            coord_fly_x=x+wirina//2
            coord_fly_y=y-10
            vistrel=True
        if vistrel_1==False:
            coord_fly_x_1=x+wirina//2
            coord_fly_y_1=y-10
            vistrel_1=True
    if vistrel:
        coord_fly_y-=speed_snaryad
        pygame.draw.circle(win,(255,255,0),(coord_fly_x,coord_fly_y),5)
        pygame.display.update()
        if coord_fly_y<1:
            vistrel=False
    if vistrel_1 and coord_fly_y<400:
        coord_fly_y_1-=speed_snaryad
        pygame.draw.circle(win,(255,255,0),(coord_fly_x_1,coord_fly_y_1),5)
        pygame.display.update()
        if coord_fly_y_1<400:
            vistrel_2=True
    if vistrel_2:
        coord_fly_y_1-=speed_snaryad
        pygame.draw.circle(win,(255,255,0),(coord_fly_x_1,coord_fly_y_1),5)
        pygame.display.update()
        if coord_fly_y_1<1:
            vistrel_1=False
            vistrel_2=False
    if vrag_1==False and pygame.time.get_ticks()- wait_respawn > 700 :
        x_vrag_1=random.randint(0,600)
        y_vrag_1=random.randint(0,400)
        win.blit(jpeg_vrag_1,(x_vrag_1,y_vrag_1))
        #pygame.draw.rect(win,(GREEN),(x_vrag_1,y_vrag_1,30,30))
        pygame.display.update()
        naprx=1
        napry=1
        vrag_1=True
    if vrag_1:
        x_vrag_1+=speed_vrag * naprx
        y_vrag_1+=speed_vrag * napry
        win.blit(jpeg_vrag_1,(x_vrag_1,y_vrag_1))
        #pygame.draw.rect(win,(GREEN),(x_vrag_1,y_vrag_1,30,30))
        pygame.display.update()
        if x_vrag_1>600-30:
            naprx=-1
        if x_vrag_1<1:
            naprx=1
        if y_vrag_1<1:
            napry=1
        if y_vrag_1>400:
            napry=-1
    if coord_fly_x > x_vrag_1 and coord_fly_x < x_vrag_1+70 and coord_fly_y > y_vrag_1 and coord_fly_y < y_vrag_1 + 70:
        wait_respawn = pygame.time.get_ticks()
        x_vrag_1=-100
        vrag_1=False
        vistrel=False
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        if count_pop%10==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=5
            delitel_1-=40
            delitel_2-=40
    if coord_fly_x_1 > x_vrag_1 and coord_fly_x_1 < x_vrag_1+70 and coord_fly_y_1 > y_vrag_1 and coord_fly_y_1 < y_vrag_1 + 70:
        wait_respawn = pygame.time.get_ticks()
        x_vrag_1=-100
        vrag_1=False
        vistrel_1=False    
        count_pop+=1
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        if count_pop%10==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=5
            delitel_1-=40
            delitel_2-=40
    if vrag_2==False and pygame.time.get_ticks() - wait_respawn_1 > 700:
        x_vrag_2=random.randint(0,600)
        y_vrag_2=random.randint(0,400)
        #pygame.draw.rect(win,(255,255,0),(x_vrag_2,y_vrag_2,30,30))
        win.blit(jpeg_vrag_2,(x_vrag_2,y_vrag_2))
        pygame.display.update()
        naprx_2=1
        napry_2=1
        vrag_2=True
    if vrag_2:
        x_vrag_2+=speed_vrag * naprx_2
        #y_vrag_2+=speed_vrag * napry
        #pygame.draw.rect(win,(255,255,0),(x_vrag_2,y_vrag_2,30,30))
        win.blit(jpeg_vrag_2,(x_vrag_2,y_vrag_2))
        pygame.display.update()
        if x_vrag_2>600-30:
            naprx_2=-1
        if x_vrag_2<1:
            naprx_2=1
        if y_vrag_2<1:
            napry_2=1
        if y_vrag_2>400:
            napry_2=-1
    if coord_fly_x_1 > x_vrag_2 and coord_fly_x_1 < x_vrag_2+70 and coord_fly_y_1 > y_vrag_2 and coord_fly_y_1 < y_vrag_2 + 70:
        wait_respawn_1 = pygame.time.get_ticks()
        x_vrag_2=-100
        vrag_2=False
        vistrel_1=False
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        count_pop+=1
        if count_pop%10==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=5
            delitel_1-=40
            delitel_2-=40
    if coord_fly_x > x_vrag_2 and coord_fly_x < x_vrag_2+70 and coord_fly_y > y_vrag_2 and coord_fly_y < y_vrag_2 + 70:
        wait_respawn_1 = pygame.time.get_ticks()
        x_vrag_2=-100
        vrag_2=False
        vistrel=False
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        count_pop+=1
        if count_pop%10==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=5
            delitel_1-=40
            delitel_2-=40
####################################################################################
    if vrag_3==False and pygame.time.get_ticks() - wait_respawn_2 > 700:
        x_vrag_3=random.randint(0,600)
        y_vrag_3=random.randint(0,400)
        #pygame.draw.rect(win,(255,255,0),(x_vrag_2,y_vrag_2,30,30))
        win.blit(jpeg_vrag_3,(x_vrag_3,y_vrag_3))
        pygame.display.update()
        naprx_3=-1
        napry_3=-1
        vrag_3=True
    if vrag_3:
        x_vrag_3+=speed_vrag * naprx_3
        y_vrag_3+=speed_vrag * napry_3
        #pygame.draw.rect(win,(255,255,0),(x_vrag_2,y_vrag_2,30,30))
        win.blit(jpeg_vrag_3,(x_vrag_3,y_vrag_3))
        pygame.display.update()
        if x_vrag_3>600-30:
            naprx_3=-1
        if x_vrag_3<1:
            naprx_3=1
        if y_vrag_3<1:
            napry_3=1
        if y_vrag_3>400-70:
            napry_3=-1
    if coord_fly_x_1 > x_vrag_3 and coord_fly_x_1 < x_vrag_3+70 and coord_fly_y_1 > y_vrag_3 and coord_fly_y_1 < y_vrag_3 + 70:
        wait_respawn_2 = pygame.time.get_ticks()
        x_vrag_3=-100
        vrag_3=False
        vistrel_1=False
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        count_pop+=1
        if count_pop%10==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=5
            delitel_1-=40
            delitel_2-=40
    if coord_fly_x > x_vrag_3 and coord_fly_x < x_vrag_3+70 and coord_fly_y > y_vrag_3 and coord_fly_y < y_vrag_3 + 70:
        wait_respawn_2 = pygame.time.get_ticks()
        x_vrag_3=-100
        vrag_3=False
        vistrel=False
        pygame.draw.circle(win,RED,(coord_fly_x,coord_fly_y),15,15)
        pygame.display.update()
        count_pop+=1
        if count_pop%10==0 and count_pop!=0:
            speed_vrag+=1
            speed_snaryad_1+=5
            delitel_1-=40
            delitel_2-=40
###################################################################################
    if snaryad_vraga == False and pygame.time.get_ticks()-wait_snaryad > delitel_1:
        snaryad_vraga_x=x_vrag_1
        snaryad_vraga_y=y_vrag_1
        snaryad_vraga=True
        wait_snaryad = pygame.time.get_ticks()
    if snaryad_vraga:
        snaryad_vraga_y+=speed_snaryad_1
        pygame.draw.circle(win,RED,(snaryad_vraga_x,snaryad_vraga_y),5)
        pygame.display.update()
        if snaryad_vraga_y>800:
            snaryad_vraga=False
    if snaryad_vraga_1 == False and pygame.time.get_ticks()-wait_snaryad_1 > delitel_2:
        snaryad_vraga_x_1=x_vrag_2
        snaryad_vraga_y_1=y_vrag_2
        snaryad_vraga_1=True
        wait_snaryad_1 = pygame.time.get_ticks()
    if snaryad_vraga_1:
        snaryad_vraga_y_1+=speed_snaryad_1
        pygame.draw.circle(win,RED,(snaryad_vraga_x_1,snaryad_vraga_y_1),5)
        pygame.display.update()
        if snaryad_vraga_y_1>800:
            snaryad_vraga_1=False
        ####
    if snaryad_vraga_2 == False and pygame.time.get_ticks()-wait_snaryad_2 > delitel_2:
        snaryad_vraga_x_2=x_vrag_3
        snaryad_vraga_y_2=y_vrag_3
        snaryad_vraga_2=True
        wait_snaryad_2 = pygame.time.get_ticks()
    if snaryad_vraga_2:
        snaryad_vraga_y_2+=speed_snaryad_1
        pygame.draw.circle(win,RED,(snaryad_vraga_x_2,snaryad_vraga_y_2),5)
        pygame.display.update()
        if snaryad_vraga_y_2>800:
            snaryad_vraga_2=False
    if snaryad_vraga_x > x and snaryad_vraga_x < x + wirina and snaryad_vraga_y > y and snaryad_vraga_y < y + dlina or snaryad_vraga_x_1 > x and snaryad_vraga_x_1 < x + wirina and snaryad_vraga_y_1 > y and snaryad_vraga_y_1 < y + dlina or snaryad_vraga_x_2 > x and snaryad_vraga_x_2 < x + wirina and snaryad_vraga_y_2 > y and snaryad_vraga_y_2 < y + dlina :
        pause=True
        while pause:
            pygame.time.delay(30)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pause=False
                    run=False
            win.blit((Fon_2),(0,0))
            pygame.display.update()
            fontObj = pygame.font.Font('18963.ttf', 20)
            text = str(count_pop)
            textSurfaceObj = fontObj.render((f"Вы убили: {text}, нажмите Enter что бы повторить") , True, BLUE, RED)
            win.blit(textSurfaceObj,(100,300))
            pygame.display.update()
            vopros=pygame.key.get_pressed()
            if vopros[pygame.K_RETURN]:
                pause=False
                speed_vrag=1
                speed_snaryad_1=5
                delitel_1=300
                delitel_2=400
                snaryad_vraga_1=False
                snaryad_vraga=False
                snaryad_vraga_2=False
                wait_snaryad=0
                wait_snaryad_1=0
                wait_snaryad_2=0
                count_pop=0
                vrag_1=False
                vrag_2=False
                vrag_3=False
                wait_respawn=0
                wait_respawn_1=0
                wait_respawn_2=0
               #if count_blur%2==0:
               #win.fill((0,0,0))