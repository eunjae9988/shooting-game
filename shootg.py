import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("shooting game")
clock = pygame.time.Clock()

person_x = screen.get_size()[0] // 2
person_y = screen.get_size()[1] // 2
planet_x = random.randint(50, 450)
planet_y = random.randint(50, 450)

def shape_dockalien(surface, x, y):
    pygame.draw.ellipse(surface, (0, 255, 0), (x - 20, y - 15, 40, 30))
    pygame.draw.circle(surface, (0, 255, 0), (x, y - 20), 10)
    pygame.draw.circle(surface, (255, 0, 15), (x - 7, y - 22), 5)
    pygame.draw.line(surface, (0, 255, 0), (x - 10, y - 35), (x + 10, y - 35), 3)

def draw_planet(surface, x, y):
    pygame.draw.circle(surface, (100, 100, 255), (x, y), 25)
    pygame.draw.ellipse(surface, (200, 200, 255), (x - 35, y - 10, 70, 20), 2)

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                person_y -= 10
            elif event.key == pygame.K_DOWN:
                person_y += 10
            elif event.key == pygame.K_RIGHT:
                person_x += 10
            elif event.key == pygame.K_LEFT:
                person_x -= 10

    screen.fill((0, 0, 0))
    
    draw_planet(screen, planet_x, planet_y)
    shape_dockalien(screen, person_x, person_y)
    
    pygame.display.flip()

pygame.quit()