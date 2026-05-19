import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("shooting game")

person_x = screen.get_size()[0] // 2
person_y = screen.get_size()[1] // 2

def shape_dockalien(surface, x, y):
    pygame.draw.ellipse(surface, (0, 255, 0), (x - 20, y - 15, 40, 30))
    pygame.draw.circle(surface, (0, 255, 0), (x, y - 20), 10)
    pygame.draw.circle(surface, (255, 0, 15), (x - 7, y - 22), 5)
    pygame.draw.line(surface, (0, 255, 0), (x - 10, y - 35), (x + 10, y - 35), 3)
def draw_planet(surface, x, y):
    pygame.draw.circle(surface, (100, 100, 255), (x, y), 25)
    pygame.draw.ellipse(surface, (200, 200, 255), (x - 35, y - 10, 70, 20), 2)
planet_x=random.randint(50,450)
planet_y=random.randint(50,450)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    shape_dockalien(screen, person_x, person_y)
    draw_planet(screen, planet_x, planet_y)
    pygame.display.flip()

pygame.quit()