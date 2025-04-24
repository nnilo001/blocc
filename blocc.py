import pygame
import keyboard

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("blocc")
clock = pygame.time.Clock()
pygame.image.load()
loopmega = 1
while loopmega == 1:
    pygame.mouse.set_visible(False)
    title = True
    loop = 1
    while loop == 1:
        screen.fill((0, 0, 0))
        fontbig = pygame.font.SysFont(None, 150)
        fontsmall = pygame.font.SysFont(None, 50)
        titl = fontbig.render("blocc", True, (255, 255, 255))
        starttext = fontsmall.render("press [SPACE] to start", True, (255, 255, 255))
        if title == True:
            screen.blit(titl, (260, 45))
            screen.blit(starttext, (220, 500))
        elif title == False:
            pass
    
        if keyboard.is_pressed("space"):
            title = False
            loop = 2
    
        clock.tick(30)
        pygame.display.flip()
        
        
        plrx = 400
        plry = 300
    while loop == 2:
        if plrx < -25:
            plrx = 800
        if plrx > 800:
            plrx = -25
        if plry < -25:
            plry = 600
        if plry > 600:
            plry = -25
            
        if keyboard.is_pressed("shift"):
            shiftpress = 3
        else:
            shiftpress = 0
        if keyboard.is_pressed("up"):
            plry = plry - 5 - shiftpress
        if keyboard.is_pressed("down"):
            plry = plry + 5 + shiftpress
        if keyboard.is_pressed("left"):
            plrx = plrx - 5 - shiftpress
        if keyboard.is_pressed("right"):
            plrx = plrx + 5 + shiftpress
        plr = pygame.Rect(plrx, plry, 25, 25)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), plr)
        clock.tick(30)
        pygame.display.flip()
        
        
        
        
    while loop == 3:
        pass
    
    

    if keyboard.is_pressed("esc"):
        pygame.quit()
        exit()