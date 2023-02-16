import pygame
from random import randint

time_clocks = pygame.time.Clock()

# Initialize
pygame.init()
width_screen = 1366
height_screen = 768

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

pygame.mixer.music.load("sound/music.wav")
snake_sound = pygame.mixer.Sound("sound/snake.wav")
win = pygame.mixer.Sound("sound/win.wav")
lose = pygame.mixer.Sound("sound/lose.wav")
ladder = pygame.mixer.Sound("sound/ladder.wav")
