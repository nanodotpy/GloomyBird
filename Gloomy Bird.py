import pygame
import random
import winsound


pygame.init()

largeur = 1280
hauteur = 720

white = (255,255,255)

violetclair = (255,188,103)

gamedisplay = pygame.display.set_mode((largeur,hauteur))

pygame.mixer.music.load('Lil Uzi Vert Type Beat - Pixels.mp3')

pygame.mixer.music.play()

pygame.mixer.music.set_volume(0.3)

#flap = pygame.mixer.Sound( "wings.wav" )

fnt = pygame.image.load('Gloomy.png')

logo = pygame.image.load('flappy-blue.png').convert_alpha()

pygame.display.set_caption('Gloomy Bird')

pygame.display.set_icon(fnt)

clock = pygame.time.Clock()

logo = pygame.transform.rotozoom(logo, 0, 0.038)
   
sky = pygame.image.load('bg.png')

title = pygame.image.load('mneu-title.png')

title = pygame.transform.scale(title, (largeur,hauteur))

ground = pygame.image.load('ground.png').convert_alpha()

sky = pygame.transform.scale(sky, (largeur,hauteur))

ground = pygame.transform.scale(ground,(largeur,hauteur))

t = pygame.image.load('tuyau.png')

t = pygame.transform.scale(t,(int(largeur/10),int(hauteur/1.5)))

tr = pygame.transform.rotozoom(t,180,1)

tr = pygame.transform.flip(tr,True,False)

def flappy(y,a):
    gamedisplay.blit(pygame.transform.rotate(logo,a),(largeur*0.2,y))
    
        
def bg():
    gamedisplay.blit(sky,(0,0))


def floor(xg):
    gamedisplay.blit(ground,(xg,0))


def menutitle() :
    gamedisplay.blit(title,(0,0))


def menu():
    
    menu = True
    y = hauteur//3 -25 
    xg = 0
    gamespeed = 8
    
    y_change = 2
    

    
    while menu :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_SPACE :
                    menu = False
                
        y += y_change
        
        if y > hauteur//3 + 55 :
            y_change = -2
        elif y < hauteur//3 :
            y_change = 2
        
            
         
        
        if xg <= -largeur :
            xg = 0
        else :
            xg -= gamespeed
            
        
        bg()
        
        floor(xg)
        
        floor(largeur+xg)
        
        flappy(y,0)
         
        menutitle()
        
        pygame.display.update()
        


class tuyau :
    
    def __init__(self,x,yt):
        self.x = x
        self.yt = yt
    
    def afficher(self):
        gamedisplay.blit(t,(self.x,self.yt))
        gamedisplay.blit(tr,(self.x,self.yt+660))
        
        
def pointsound():
    #winsound.PlaySound("sfx_point.wav",winsound.SND_ASYNC)
    pass
        
wlogo = logo.get_width()
hlogo = logo.get_height()



#print(wlogo) 74
#print(hlogo) 53


wtuyau = t.get_width()
htuyau = t.get_height()
  
chiasse = True



def game_loop():
    
    winsound.PlaySound("wings.wav" , winsound.SND_ASYNC )
        
    with open('HS.txt', 'r+') as hs :
        try : 
            ths  = int(hs.read())
        except :
            ths = 0
    
    
    tuyau1 = tuyau(int(largeur*1.2),random.randint(int(-hauteur/1.6),-100))
    
    tuyau2 = tuyau(tuyau1.x+400,random.randint(int(-hauteur/1.6),-100))
            
    tuyau3 = tuyau(tuyau2.x+400,random.randint(int(-hauteur/1.6),-100))
    
    tuyau4 = tuyau(tuyau3.x+400,random.randint(int(-hauteur/1.6),-100)) 
    
    a = 0 
    
    gamespeed = 6
    xg = 0 
    crash = False
    pt = False
    counter = 0
    global chiasse 
    y = hauteur//3
    y_change = - hauteur//40
    accel = hauteur//225
    
    
    while chiasse :
        
        
        
        # y_change compris entre -18 et 20 
        
        
        if y_change < 0 :
            a += 10
        
        elif y_change > 5 :
            a -= 4 
        
        if a < -75 :
            a = -75
        elif a > 30 :
            a = 30
            
        
        
        
        if tuyau1.x < -largeur/10 :
            tuyau1 = tuyau(tuyau4.x + 400,random.randint(int(-hauteur/1.6),-100))
        if tuyau2.x < -largeur/10 :
            tuyau2 = tuyau(tuyau1.x + 400,random.randint(int(-hauteur/1.6),-100))
        if tuyau3.x < -largeur/10 :
            tuyau3 = tuyau(tuyau2.x + 400,random.randint(int(-hauteur/1.6),-100))
        if tuyau4.x < -largeur/10 :
            tuyau4 = tuyau(tuyau3.x + 400,random.randint(int(-hauteur/1.6),-100))
       
        if tuyau1.x <= largeur*0.2 + wlogo <= tuyau1.x + wtuyau or tuyau1.x <= largeur*0.2 <= tuyau1.x + wtuyau :
            if not tuyau1.yt + htuyau < y < tuyau1.yt + 610 and not y >= hauteur*0.835:
                crash = True
                again()
            elif largeur*0.2 >= tuyau1.x + wtuyau - gamespeed and not crash :
                counter += 1 
                pointsound()
        
        if tuyau2.x <largeur*0.2 + wlogo < tuyau2.x + wtuyau or tuyau2.x <largeur*0.2<tuyau2.x + wtuyau :
            if not tuyau2.yt + htuyau < y < tuyau2.yt + 610 and not y >= hauteur*0.835:
                crash = True
                again()
            elif largeur*0.2 >= tuyau2.x + wtuyau - gamespeed and not crash :
                counter += 1 
                pointsound()
            
        if tuyau3.x <largeur*0.2 + wlogo < tuyau3.x + wtuyau or tuyau3.x <largeur*0.2<tuyau3.x + wtuyau :
            if not tuyau3.yt + htuyau < y < tuyau3.yt + 610 and not y >= hauteur*0.835 :
                crash = True
                again
            elif largeur*0.2 >= tuyau3.x + wtuyau - gamespeed and not crash :
                counter += 1
                pointsound()
                
        if tuyau4.x <largeur*0.2 + wlogo < tuyau4.x + wtuyau or tuyau4.x <largeur*0.2<tuyau4.x + wtuyau :
            if not tuyau4.yt + htuyau < y < tuyau4.yt + 610 and not y >= hauteur*0.835 :
                crash = True
                again()
            elif largeur*0.2 >= tuyau4.x + wtuyau - gamespeed and not crash :
                counter += 1
                pointsound()
                

        if xg <= -largeur :
            xg = 0
        else :
            xg -= gamespeed

        if crash and y < hauteur*0.835:
            
            tuyau1.x += gamespeed
            tuyau2.x += gamespeed
            tuyau3.x += gamespeed
            tuyau4.x += gamespeed
            xg += gamespeed
            
                    
        if y >= hauteur*0.835 :
            pt = True
            accel = 0
            y_change = 0
            tuyau1.x += gamespeed
            tuyau2.x += gamespeed
            tuyau3.x += gamespeed
            tuyau4.x += gamespeed
            xg += gamespeed
            again()
        else :
            accel = hauteur//225
            score(str(counter))
         
        y_change += accel
        
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                chiasse = False
                    
            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_SPACE and not crash and not pt:
                    winsound.PlaySound("wings.wav" , winsound.SND_ASYNC )
                    y_change = - hauteur//40 
                
        y += y_change           
           
        bg()      
        
        tuyau1.afficher()
        tuyau2.afficher()
        tuyau3.afficher()
        tuyau4.afficher()
        
        tuyau1.x -= gamespeed
        tuyau2.x -= gamespeed
        tuyau3.x -= gamespeed
        tuyau4.x -= gamespeed
        
        floor(xg)
        
        floor(largeur+xg)
         
        flappy(y,a)
        
        
        if ths >= counter :
                
            highscore('{}'.format(ths))
        else :
            highscore('{}'.format(counter))
        
        y_change -= hauteur//500
                  
        if y_change > 20/720*hauteur:
            y_change = 20/720*hauteur
        
        
        if counter > ths :
            with open('HS.txt','w') as f: 
                f.write(str(counter))
                
    
                
            
        pygame.display.update()
        
        clock.tick(120)

def again(): 
    game_loop()   
    
def score(text): 
    font = pygame.font.Font('visitor1.ttf', 60) 
    txt = font.render(text, True, white)
    gamedisplay.blit(txt, (largeur//2-(txt.get_width()//2),hauteur//4))
    pygame.display.update()  
    
def highscore(texta):
    fonta = pygame.font.Font('visitor1.ttf', 45) 
    dtxt = fonta.render(texta, True, violetclair)
    gamedisplay.blit(dtxt,(10,0))
    pygame.display.update
    
    
menu()    
    
game_loop() 
   

pygame.display.quit()
pygame.quit()

quit()


            
        