
import pygame,sys,random
from time import *
from pygame.constants import MOUSEBUTTONDOWN

game_score = 0
gamehigh_score = 9
delay_counter = 0
clicked = False

pygame.init() 
screen= pygame.display.set_mode((900,600))
clock = pygame.time.Clock()


game_font = pygame.font.SysFont('Constantia',40)

#Game surfaces 
main_background = pygame.image.load('pyproj/gamefile/mainbg.png').convert_alpha()
background = pygame.transform.scale2x(main_background)

menu_background = pygame.image.load('pyproj/gamefile/secondbg.png').convert_alpha()
mainmenubg = pygame.transform.scale2x(menu_background)

game_floor = pygame.image.load('pyproj/gamefile/soil.png').convert_alpha()
game_soil = pygame.transform.scale(game_floor,(600,20))
game_soil = pygame.transform.scale2x(game_soil)
soil_xpos = 0

game_bird= pygame.image.load('pyproj/gamefile/flyingbird.png').convert_alpha()
game_bird = pygame.transform.scale(game_bird, (120,70))
bird_rect = game_bird.get_rect(center = (100,300))


ccf_pillar = pygame.image.load('pyproj/gamefile/grassyfence.png').convert_alpha()
ccf_pillar = pygame.transform.scale(ccf_pillar, (70,350))
pillar_list = []
PILLARSPAWNER = pygame.USEREVENT
pygame.time.set_timer(PILLARSPAWNER,1000)
pillarheights = [250,350,450] 

def build_floor():
    screen.blit(game_soil,(soil_xpos,560))   
    screen.blit(game_soil,(soil_xpos+900,560))   


def create_pipe():
    pillar_height = random.choice(pillarheights)
    base_pipe = ccf_pillar.get_rect(midtop=(1000,pillar_height))
    apex_pipe = ccf_pillar.get_rect(midbottom=(1000,pillar_height-200))
    return base_pipe, apex_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 8
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(ccf_pillar,pipe)
        else:
            rotatepipe = pygame.transform.flip(ccf_pillar,False,True)
            screen.blit(rotatepipe,pipe)


def check_collisions(pipes):
    for pipe in pipes: 
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top<= -100 or bird_rect.bottom>= 560:
        return False
    return True 

def write_text(screen,x,y,Word):
    import pygame
    pygame.init()
    font = pygame.font.SysFont('Constantia',40)
    text = font.render(Word, True,(255,255,255))
    screen.blit(text,(x,y))


def tutorial_screen():
    global clicked
    tutorial_background = pygame.image.load('pyproj/gamefile/tutorialbg.png').convert_alpha()
    while True:
        screen.blit(tutorial_background,(0,0))
        mx, my = pygame.mouse.get_pos()
        menubutton = pygame.Rect(720,50,150,75)
        if menubutton.collidepoint((mx, my)):
            if clicked:
                main_menu()
        clicked = False       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
            if event.type == MOUSEBUTTONDOWN and menubutton.collidepoint((mx, my)):    
                main_menu()
            if event.type == MOUSEBUTTONDOWN: 
                if event.button == 1:
                    clicked = True
        pygame.draw.rect(screen, (255,217,102), menubutton)
        pygame.display.update() #keeps the window on the screen infinately
        clock.tick(60)
def main_menu():
    global clicked
    while True: 
        screen.blit(menu_background,(0,0))   
        write_text(screen,400,200,'Main Menu')
        mx, my = pygame.mouse.get_pos()
        startbutton = pygame.Rect(400,300,200,75)
        #start button
        tutorialbutton = pygame.Rect(400,400,200,75)#Tutorial

        if startbutton.collidepoint((mx, my)):
            if clicked:
                game_loop()#(should be the game function being called here)
        if tutorialbutton.collidepoint((mx, my)):
            if clicked:
                tutorial_screen() #(should be the tutorial function being called here)  
 
        pygame.draw.rect(screen, (255,217,102), startbutton)
        pygame.draw.rect(screen, (255,217,102), tutorialbutton)


        clicked= False  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and startbutton.collidepoint((mx, my)):
                game_loop()
            if event.type == MOUSEBUTTONDOWN and tutorialbutton.collidepoint((mx, my)):    
                tutorial_screen()
            if event.type == MOUSEBUTTONDOWN: 
                if event.button == 1:
                    clicked = True
        pygame.display.update() #keeps the window on the screen infinately
        clock.tick(60)


def high_score(game_score,gamehigh_score):
    if game_score> gamehigh_score:
        gamehigh_score = game_score 
        scoretable = open("highscore_file.txt", 'w')
        scoretable.write(""+str(gamehigh_score)) 
        scoretable.close()
    return gamehigh_score
def display_score(game_active,game_score):
    if game_active == "main_game":
        score_surface = game_font.render(str(int(game_score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (700,100))
        screen.blit(score_surface,score_rect)
    if game_active == "game_over": 
        score_surface = game_font.render(f'Score: {int(game_score)}' ,True,(255,255,255))
        score_rect = score_surface.get_rect(center = (700,100))
        screen.blit(score_surface,score_rect)
          
        highscore_surface = game_font.render(f'High Score: {int(gamehigh_score)}',True,(255,255,255))
        highscore_rect = highscore_surface.get_rect(center = (700,200))
        screen.blit(highscore_surface,highscore_rect)
        write_text(screen,320,320,"You died")


#Main game loop
def game_loop():
    global soil_xpos,pillar_list,game_score,gamehigh_score,clicked
    delay_counter = 0
    gravity = 0.5
    bird_movement = 0
    game_running = True
    score_timer = 0
    active = True
    while active: 
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    bird_movement = 0 
                    bird_movement -= 8
                elif event.key == pygame.K_SPACE:
                    bird_movement =0
                    bird_movement -= 8
            if event.type == PILLARSPAWNER:
                pillar_list.extend(create_pipe())
            if event.type == MOUSEBUTTONDOWN and menubutton.collidepoint((mx, my)):
                main_menu()
            if event.type == MOUSEBUTTONDOWN: 
                if event.button == 1:
                    clicked = True
    #end of for loop
        screen.blit(main_background,(0,0)) 
        if game_running:
            bird_movement += gravity
            bird_rect.centery += bird_movement
            screen.blit(game_bird,bird_rect) 
 
            pillar_list = move_pipe(pillar_list)
            draw_pipes(pillar_list)
             
            if delay_counter>=70:
                if score_timer == (60) and check_collisions(pillar_list)==True:
                    game_score +=1
                    score_timer = 0
                else:
                    score_timer += 1
                    display_score('main_game',game_score) 
            else:
                delay_counter+=1
            soil_xpos-=1
        else:    
            gamehigh_score = high_score(gamehigh_score,game_score)
            display_score('game_over',game_score)   
            
            mx, my = pygame.mouse.get_pos()
            menubutton = pygame.Rect(300,400,200,75)

            if menubutton.collidepoint((mx, my)):
                if clicked:
                    main_menu()
            pygame.draw.rect(screen, (255,217,102), menubutton)
            active = False

        #soil_xpos-=1
        build_floor() 
        if soil_xpos <= -900:
            soil_xpos =0
        game_running= check_collisions(pillar_list)
        pygame.display.update() #keeps the window on the screen infinately
        clock.tick(60)

main_menu()