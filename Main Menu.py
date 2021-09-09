import pygame
import os

os.chdir('C:/Users/natha/Desktop/Monkey Motion Menu')

pygame.init()

display_width = 1500
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (200,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Monkey Motion')
clock = pygame.time.Clock()

pygame.mixer.music.load('Menu Music.mp3')
pygame.mixer.music.play(-1)

titImg = pygame.image.load('images/Title.png')

crashed = False

def tit(x,y):
    gameDisplay.blit(titImg,(-100,-400))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(titImg,(0,-400))


        mouse = pygame.mouse.get_pos()

        button("Start",750,400,100,50,bright_red,red,level_select)
        button("Help",750,500,100,50,bright_red,red,game_controls)
        button("Quit",750,600,100,50,bright_red,red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_controls():

    gcont = True

    while gcont:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(titImg,(0,-400))

        mouse = pygame.mouse.get_pos()

        mainText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects("To control the monkey, you must use the motion sensors to move left to right.", mainText)
        TextRect.center = ((display_width/2),(520))
        gameDisplay.blit(TextSurf, TextRect)
        mainText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects("You must dodge obstacles and gather bananas and progress through the level.", mainText)
        TextRect.center = ((display_width/2),(550))
        gameDisplay.blit(TextSurf, TextRect)

        button("Back",1200,600,100,50,bright_red,red,game_intro)

        pygame.display.update()
        clock.tick(15)

def level_select():

    select = True

    while select:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(titImg,(0,-400))


        mouse = pygame.mouse.get_pos()

        button("Level 1",750,400,100,50,bright_red,red,level_1)
        button("Level 2",750,500,100,50,bright_red,red,level_2)
        button("Level 3",750,600,100,50,bright_red,red,level_3)
        button("Back",1200,600,100,50,bright_red,red,game_intro)

        pygame.display.update()
        clock.tick(15)

def level_1():
    global pause

def level_2():
    global pause

def level_3():
    global pause

game_intro()
game_controls()
level_select()
level_1()
level_2()
level_3()
pygame.quit()
quit()
