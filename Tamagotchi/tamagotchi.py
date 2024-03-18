import pygame
from pet import Tamagotchi

pygame.display.init()
pygame.font.init()
Width, Height = 400, 450
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tamagotchi")
clock = pygame.time.Clock()

background_color = (200, 200, 200)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255,255,0)
red = (255, 0, 0)

def def_color(level):

    if level > 70:
        return green
    
    if 30 <= level <=70:
        return yellow
    
    return red

wesoly = pygame.image.load('happy.jpg')
wesoly = pygame.transform.scale(wesoly, (150, 150))
neutralny = pygame.image.load('neutral.jpg')
neutralny = pygame.transform.scale(neutralny, (150, 150))
smutny = pygame.image.load('sad.jpg')
smutny = pygame.transform.scale(smutny, (150, 150))

font = pygame.font.SysFont("Comic Sans", 20)

tamagotchi = Tamagotchi()

game_end = False

while game_end != True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_end = True
        elif event.type == pygame.QUIT:
            game_end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if feed_button.collidepoint(event.pos):
                tamagotchi.feed()
            elif play_button.collidepoint(event.pos):
                tamagotchi.play()

    tamagotchi.update()
    display.fill(background_color)

    color_happiness = def_color(tamagotchi.happiness_lvl)
    pygame.draw.rect(display, color_happiness,
        pygame.Rect(50, 50, tamagotchi.happiness_lvl * 2, 20))
    text_happiness = font.render("Happiness", True, black)
    display.blit(text_happiness, (50, 20))

    color_hunger = def_color(tamagotchi.hunger_lvl)
    pygame.draw.rect(display, color_hunger,
        pygame.Rect(50, 100, tamagotchi.hunger_lvl * 2, 20))
    text_hunger = font.render("Hunger", True, black)
    display.blit(text_hunger, (50, 70))

    text_hunger_lvl = font.render(f"{int(tamagotchi.hunger_lvl)}", True, black)
    display.blit(text_hunger_lvl, (50, 95))
    text_happiness_lvl = font.render(f"{int(tamagotchi.happiness_lvl)}", True, black)
    display.blit(text_happiness_lvl, (50, 45))

    feed_button = pygame.Rect(225, 300, 150, 50)
    play_button = pygame.Rect(25, 300, 150, 50)
    pygame.draw.rect(display, white, feed_button, 3)
    pygame.draw.rect(display, white, play_button, 3)

    text_feed = font.render("Feed", True, black)
    text_play = font.render("Play", True, black)

    text_width_feed, text_height_feed = text_feed.get_size()
    text_width_play, text_height_play = text_play.get_size()

    display.blit(text_feed, (feed_button.x + (feed_button.width - text_width_feed) // 2, feed_button.y + (feed_button.height - text_height_feed) // 2))
    display.blit(text_play, (play_button.x + (play_button.width - text_width_play) // 2, play_button.y + (play_button.height - text_height_play) // 2))

    nastroj = tamagotchi.hunger_lvl + tamagotchi.happiness_lvl
    if nastroj > 120:
        display.blit(wesoly, (125, 135))
    elif nastroj > 60:
        display.blit(neutralny, (125, 135))
    else:
        display.blit(smutny, (125, 135))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()