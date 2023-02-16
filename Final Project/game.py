import pygame
from random import randint

time_clocks = pygame.time.Clock()

# Initialize Game Screen Size
pygame.init()
width_screen = 1366
height_screen = 768

# Game Icon and Title display
ic = pygame.image.load("images/icon.png")
game_layout_display = pygame.display.set_mode((width_screen, height_screen), pygame.FULLSCREEN)
pygame.display.set_caption("Snakes and Ladders Game ")
pygame.display.set_icon(ic)
pygame.display.update()

# Graphics:
black_color = (10, 10, 10)
white_color = (250, 250, 250)
grey_color = (50, 50, 50)
yellow_color = (150, 150, 0)
purple_color = (43, 3, 132)
blue_purple_color = (60, 0, 190)
red_color = (200, 0, 0)
blue_red_color = (240, 0, 0)
green_color = (0, 200, 0)
blue_green_color = (0, 230, 0)
blue_color = (0, 0, 200)

background1 = pygame.image.load("images/introduction1.png")
background2 = pygame.image.load("images/introduction2.png")
background3 = pygame.image.load("images/introduction3.png")
background4 = pygame.image.load("images/introduction4.png")
background5 = pygame.image.load("images/introduction5.png")
credits = pygame.image.load("images/developer.png")

menubg = pygame.image.load("images/menu.png")
gamebg = pygame.image.load("images/gamebg.png")

pygame.mixer.music.load("sound/music.wav")
snake_sound = pygame.mixer.Sound("sound/snake.wav")
win = pygame.mixer.Sound("sound/win.wav")
lose = pygame.mixer.Sound("sound/lose.wav")
ladder = pygame.mixer.Sound("sound/ladder.wav")

# Message displaying for field
def message_display1_screen(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)

def text_objects1_screen(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, blue_color)
    return textSurface, textSurface.get_rect()

# Message displaying for buttons
def message_display_screen(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects_screen(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)


def text_objects_screen(text, font):
    textSurface = font.render(text, True, black_color)
    return textSurface, textSurface.get_rect()


# Buttons for playing:
def button1(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)
    
def button2(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)
    

# Quitting:
def Quit():
    pygame.quit()
    quit()


# Buttons:
def button(t, xm, ym, x, y, wid, hei, int, after, fast, best):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if best == 1:
                choice()
            elif best == 5:
                return 5
            elif best == 0:
                Quit()
            elif best == "s" or best == 2 or best == 3 or best == 4:
                return best
            elif best == 7:
                choice()
            else:
                return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)
    
    
# Main Menu
def main_menu():
    pygame.mixer.music.play(-1)

    m = True
    while m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        game_layout_display.blit(menubg, (0, 0))
        button("Play", mouse[0], mouse[1], (width_screen / 2 - 100), (height_screen / 4), 200, 100, green_color,
               blue_green_color, 60, 1)

        button("Quit", mouse[0], mouse[1], (width_screen / 2 - 100), (height_screen / 5) + 200, 200, 100, red_color,
               blue_red_color, 60, 0)
        
def creditation():
    while True:
        game_layout_display.blit(credits, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], width_screen / 2 - 100, 700, 200, 50, green_color, blue_red_color, 25, 20):
            main_menu()

        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        if button2("Mute", mouse[0], mouse[1], 1166, 610, 200, 50, purple_color, blue_purple_color, 25):
            pygame.mixer.music.pause()
        if button2("Credits", mouse[0], mouse[1], 1166, 660, 200, 50, purple_color, blue_purple_color, 25):
            creditation()

        pygame.display.update()

# Main Menu Options
def choice():
    f = True
    while f == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
