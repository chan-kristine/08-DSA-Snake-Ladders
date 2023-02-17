import pygame
from random import randint

time_clocks = pygame.time.Clock()

# Initialize Game Screen Size
pygame.init()
width_screen = 1366
height_screen = 768

# Game Icon and Title display
ic = pygame.image.load("images/icon.png")
game_layout_display = pygame.display.set_mode((height_screen, width_screen), pygame.FULLSCREEN)
pygame.display.set_caption("Snakes and Ladders Game ")
pygame.display.set_icon(ic)
pygame.display.update()

# Graphic Colors
black_color = (10, 10, 10)
white_color = (250, 250, 250)
grey_color = (50, 50, 50)
yellow_color = (150, 150, 0)
blue_purple_color = (60, 0, 190)
red_color = (200, 0, 0)
purple_color = (43, 3, 132)
green_color = (0, 200, 0)
blue_green_color = (0, 230, 0)
blue_color = (0, 0, 200)
blue_red_color = (240, 0, 0)

# Background Images
background1 = pygame.image.load("images/introduction1.png")
background2 = pygame.image.load("images/introduction2.png")
background3 = pygame.image.load("images/introduction3.png")
background4 = pygame.image.load("images/introduction4.png")
background5 = pygame.image.load("images/introduction5.png")
credits = pygame.image.load("images/developer.png")

# Main Backgrounds
menubg = pygame.image.load("images/menu.png")
gamebg = pygame.image.load("images/gamebg.png")

# Dice 1-6
mother_board = pygame.image.load("images/Snakes_ladders_big_image.png")
dice1 = pygame.image.load("images/dice1.png")
dice2 = pygame.image.load("images/dice2.png")
dice3 = pygame.image.load("images/dice3.png")
dice4 = pygame.image.load("images/dice4.png")
dice5 = pygame.image.load("images/dice5.png")
dice6 = pygame.image.load("images/dice6.png")

# Player Pawn 
pred = pygame.image.load("images/redplayer.png")
pyellow = pygame.image.load("images/yellowplayer.png")
pgreen = pygame.image.load("images/greenplayer.png")
pblue = pygame.image.load("images/blueplayer.png")
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
                    
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        best1 = best2 = best3 = best4 = best5 = -1
        game_layout_display.blit(menubg, (0, 0))
        # Single player button
        best1 = button("Single Player", mouse[0], mouse[1], (width_screen / 2 - 150), 250, 300, 50, green_color,
                       blue_green_color, 30, "s")
        # 2 player button
        best2 = button("2 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 350, 300, 50, green_color,
                       blue_green_color, 30, 2)
        # 3 player
        best3 = button("3 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 450, 300, 50, green_color,
                       blue_green_color, 30, 3)
        # 4 player
        best4 = button("4 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 550, 300, 50, green_color,
                       blue_green_color, 30, 4)
        
         # Back button
        best5 = button("Back", mouse[0], mouse[1], 0, 650, 200, 50, green_color, blue_red_color, 30, 5)
        if best5 == 5:
            main_menu()
        if best1 == "s":
            playing(21)
        if best2 == 2:
            playing(2)
        if best3 == 3:
            playing(3)
        if best4 == 4:
            playing(4)

        pygame.display.update()


def playing(best):
    best6 = -1
    time = 3000
    if best6 == 7:
        choice()
    game_layout_display.blit(gamebg, (0, 0))
    game_layout_display.blit(mother_board, (width_screen / 2 - 250, height_screen / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    game_layout_display.blit(pred, (xcy, ycy))
    if 5 > best > 1 or best == 21:
        game_layout_display.blit(pyellow, (xcy, ycy))

    if 5 > best > 2 or best == 21:
        game_layout_display.blit(pgreen, (xcg, ycg))

    if 5 > best > 2:
        game_layout_display.blit(pblue, (xcb, ycb))
    gamer1 = "Player 1"
    gamer1score = 0
    if best == 21:
        gamer2 = "Computer"
        gamer2score = 0
    if 5 > best > 1:
        gamer2 = "Player 2"
        gamer2score = 0
    if 5 > best > 2:
        gamer3 = "Player 3"
        gamer3score = 0
    if 5 > best > 3:
        gamer4 = "Player 4"
        gamer4score = 0
    tips = 1
    play = True
    while True:
        less = False
        set = False
        time = 3000
        game_layout_display.blit(gamebg, (0, 0))
        game_layout_display.blit(mother_board, (width_screen / 2 - 250, height_screen / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

main_menu()