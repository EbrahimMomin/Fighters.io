import pygame
import math
import random

pygame.init()

w_offset = 60
h_offset = 120

width = pygame.display.Info().current_w - w_offset
height = pygame.display.Info().current_h - h_offset

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("FIGHTERS.IO")

clientNumber = 0

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.width = 30
        self.height = 30
        self.health = 25
        self.color_array = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        for i in range(3):
            if self.color_array[i] < 35: self.color_array[i] < 35
        self.color = (self.color_array[0], self.color_array[1], self.color_array[2])
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        angle = math.atan2(dy, dx)
        x_movement = self.speed * math.cos(angle)
        y_movement = self.speed * math.sin(angle)
        self.x += x_movement
        self.y += y_movement
        if self.x < 0: self.x = -self.width
        if self.y < 0: self.y = -self.width
        if self.x > width - self.width: self.x = width - self.width
        if self.y > height - self.height: self.y = height - self.height
        

def redraw_window(win, player):
    win.fill((10, 10, 10))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    p = Player(random.randint(0, width), random.randint(0, height))
    clock = pygame.time.Clock()
    FPS = 60

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move()
        redraw_window(win, p)

main()