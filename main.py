import pygame,sys,threading,random,time,os
from pygame.locals import *
#from sprite_sheet import SpriteSheet
black = (100,90,200)
white=(255,255,255)
c1 = (10,210,100)
l = (0,0,0)


pygame.init()
FPS=40




class enemy(pygame.sprite.Sprite):
    def __init__(self,name):
        super().__init__()
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()

#OBSTACLES RANDOMISTATION
def cactus_update(blk):
    counter = 0
    
    try:
        b = [-1000,-1500,-1900,-2400,-2900,-3400]
        
        c=0
        while True:
            for i in blk:
                i.rect.x+=10
                if i.rect.x == scrw:
                    i.rect.x=b[c]
                    c+=1
                    if c==6:
                        c=0

            
            fpsclock.tick(FPS)
            
    except:
        #cleanup_stop_thread()
        sys.exit()
        pygame.quit()
        
#BACKGOUND UPDATION
def land_update(dhabbe):
    
    try:
        while True:
            

            dhabbe.rect.x+=10
            if dhabbe.rect.x==0:
                dhabbe.rect.x=-1600
            clouds.rect.x+=0.01
            if clouds.rect.x==0:
                clouds.rect.x=-800
            
            
                         
            fpsclock.tick(FPS)
            
    except:
        #cleanup_stop_thread()
        sys.exit()
        pygame.quit()




block_list=pygame.sprite.Group()
all_sprite_list=pygame.sprite.Group()
scrw=800
scrh=600
screen=pygame.display.set_mode((scrw,scrh))
pygame.display.set_caption("Ska-T-Rex")





#BACKGROUND THINGS
player = enemy("player_copy.png")
player.rect.x=700
player.rect.y=410
all_sprite_list.add(player)

land =enemy("zamen_line.png")
land.rect.x=0
land.rect.y=470
all_sprite_list.add(land)

dhabbe = enemy("land1.png")
dhabbe.rect.x=-1600
dhabbe.rect.y=480
all_sprite_list.add(dhabbe)

clouds = enemy("s_clouds.png")
clouds.rect.x = 0
clouds.rect.y = 0
all_sprite_list.add(clouds)



#OBSTACLES
cac1 = enemy("cac1.png")
cac1.rect.y=410
cac1.rect.x=-100
block_list.add(cac1)
all_sprite_list.add(cac1)
cac2 = enemy("cac2.png")
cac2.rect.y=410
cac2.rect.x=-500
block_list.add(cac2)
all_sprite_list.add(cac2)
cac3 = enemy("cac3.png")
cac3.rect.y=410
cac3.rect.x=-1200
block_list.add(cac3)
all_sprite_list.add(cac3)
cac4 = enemy("cac4.png")
cac4.rect.y=410
cac4.rect.x=-1700
block_list.add(cac4)
all_sprite_list.add(cac4)
cac5 = enemy("cac5.png")
cac5.rect.y=410
cac5.rect.x=-2200
block_list.add(cac5)
all_sprite_list.add(cac5)
cac6 = enemy("cac6.png")
cac6.rect.y=410
cac6.rect.x=-2800
block_list.add(cac6)
all_sprite_list.add(cac6)
             
fpsclock=pygame.time.Clock()

def cal_score(score):
    fontobj = pygame.font.Font("freesansbold.ttf",15)
    textsurface = fontobj.render(str(score),True,black)
    textrect = textsurface.get_rect()
    textrect.topleft=(750,0)
    screen.blit(textsurface,textrect)
    pygame.display.update(textrect)
    
    return

def text(text,fobject):
    tsurf=fobject.render(text,True,black)
    trect = tsurf.get_rect()
    return tsurf,trect

#BACKGROUND THREAD
   
def back_thread():
    t1=threading.Thread(target=land_update, args=(dhabbe,),daemon=True)
    t1.start()
    return


def restart_prog():
    python = sys.executable
    os.execl(python,python, *sys.argv)


def quit_func():
    pygame.quit()
    sys.exit()
    

def game_intro():
    back_thread()
    intro =True
    startimg = pygame.image.load("start_button.png")
    startselect = pygame.image.load("start_2.png")
    quitimg = pygame.image.load("quit.png")
    quitselect=pygame.image.load("quit_2.png")
    
    posx=scrw/2-100
    s_y=scrh/2-100
    q_y=scrh/2
    while intro:
        for event in pygame.event.get():
            mx,my=pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(white)
        screen.blit(startimg,(posx, s_y))
        screen.blit(quitimg,(posx, q_y)) 
        all_sprite_list.draw(screen)
        if ((posx+181) > mx > (posx+10))&((q_y+83) > my >(q_y)):
            screen.blit(quitselect,(posx, q_y))
            event in pygame.event.get()
            if(event.type == MOUSEBUTTONUP):
                intro=False
                quit_func()

        if ((posx+181) > mx > (posx+10))&((s_y+83) > my >(s_y)):
             screen.blit(startselect, (posx,s_y))
             event in pygame.event.get()
             if(event.type== MOUSEBUTTONUP):
                 intro=False
                 return

        pygame.display.update()
        fpsclock.tick(FPS)


def gameloop():
    t2=threading.Thread(target=cactus_update,args=(block_list,),daemon=True)
    t2.start()
       
    #OBSTACLE THREAD
    score=0
    over = pygame.image.load("game_over.png")
    fontobj  = pygame.font.Font("freesansbold.ttf",20)
    while True:
        score+=1
        
                    
        if(pygame.sprite.spritecollide(player,block_list,True)):
            fontobj = pygame.font.Font("freesansbold.ttf",20)
            tsurface = fontobj.render("Your score is:"+str(score),True,black)
            trect = tsurface.get_rect()
            trect.topleft=(0,500)
            while True:
                screen.blit(over,(0,0))
                screen.blit(tsurface,trect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        restart_prog()
                    elif event.type==QUIT:
                        sys.exit()
                        pygame.quit()

        textsurf,textrect = text(str(score),fontobj)
        textrect.topleft=(750,0)
        
        
        screen.fill(white)
        
        for event in pygame.event.get():
            j=event.dict
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if (j.get('scancode')==57)&(event.type==KEYUP):
                screen.fill(white)
                caty=410
                while(caty!=250):
                    score+=1
                    
                    screen.fill(white)
                    if(caty<=280):
                        caty=caty-10
                    else:
                        caty-=20
                    player.rect.y=caty
                    all_sprite_list.draw(screen)
                    cal_score(score)
                    pygame.display.update()
                    fpsclock.tick(FPS)
                                    
                while(caty!=410):
                    score+=1
                    
                    screen.fill(white)
                    caty+=10
                    player.rect.y=caty
                    all_sprite_list.draw(screen)
                    cal_score(score)
                    pygame.display.update()
                    fpsclock.tick(FPS)

        block_list.draw(screen)
        all_sprite_list.draw(screen)
        cal_score(score)
        pygame.display.update()
        fpsclock.tick(FPS)
       

def main():
    game_intro()
    gameloop()

if __name__=="__main__":
    main()


              



