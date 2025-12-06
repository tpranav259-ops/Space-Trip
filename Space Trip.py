import pygame
import random
import time
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.mixer.music.load('back-to-the-volcano-castle-free-halloween-music-scloudtomp3downloader.com_.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#display variables
white = (255,255,255)
r=100
t=100
character = pygame.image.load('character.png')
sprite1 = pygame.image.load('sprite 1.png')
sprite1 = pygame.transform.scale(sprite1,(r,t))
sprite2 = pygame.image.load('sprite 2.jpg')
sprite3 = pygame.image.load('sprite 3.jpg')
background = pygame.image.load('background.jpg')
x=80
y=80
a=800
b=600
q=400
w=500
vel=5
x_random=random.randrange(0,600,)
y_random=0
pygame.display.set_caption('Space Trip')
background=pygame.transform.scale(background,(a,b))
pygame.display.set_icon(character)
screen.blit(background,(800,600))
count=0

pygame.display.update()

#game loop
game_over = False
while game_over == False:
    def enemy(x_random,y_random):
        screen.blit(sprite1,(x_random,y_random))
    def crash(q,x_random,w,y_random):
        if x_random<q<x_random+90 and y_random<w<y_random+60:
            time.sleep(1)
    def score(count):
        if w<y_random:
            count+=1
        font = pygame.font.SysFont(None,30)
        screen_text=font.render('score:'+str(count),True,white)
        screen.blit(screen_text,(0,0))
    userinput = pygame.key.get_pressed()

    if userinput[pygame.K_LEFT] and q > 0:
        q -= 1.5
    if userinput[pygame.K_RIGHT] and q < 740:
        q += 1.5

    screen.fill((0,9,0))
    character = pygame.transform.scale(character, (x, y))
    screen.blit(character, (q, w))
    score(count)
    enemy(x_random, y_random)
    y_random+=4
    if y_random==600:
        x_random=random.randrange(0,600)
        y_random=0

    crash(q, x_random, w, y_random)
    if x_random<q<x_random+90 and y_random<w<y_random+60:
        game_over=True
    if y_random == 600:
        count += 1


    pygame.display.update()


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True



pygame.quit()
