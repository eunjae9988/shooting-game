import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("shooting game")

font = pygame.font.SysFont("arial", 24)

person_x = screen.get_size()[0] // 2
person_y = screen.get_size()[1] // 2

star = []
score = 0
planet_x = 250
planet_y = 100
planet_speed = 3
planet_radius = 25  

for _ in range(100):
    star.append((random.randint(0, 500), random.randint(0, 500)))

bullets = []

def shape_dockalien(surface, x, y):
    pygame.draw.ellipse(surface, (0, 255, 0), (x - 20, y - 15, 40, 30))
    pygame.draw.circle(surface, (0, 255, 0), (x, y - 20), 10)
    pygame.draw.circle(surface, (255, 0, 15), (x - 7, y - 22), 5)
    pygame.draw.line(surface, (0, 255, 0), (x - 10, y - 35), (x + 10, y - 35), 3)

def draw_planet(surface, x, y):
    pygame.draw.circle(surface, (100, 100, 255), (x, y), planet_radius)
    pygame.draw.ellipse(surface, (200, 200, 255), (x - 35, y - 10, 70, 20), 2)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0)) 
    
    for star_pos in star:
        pygame.draw.circle(screen, (225, 222, 225), star_pos, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([person_x, person_y]) 
            elif event.key == pygame.K_UP:
                person_y -= 10
            elif event.key == pygame.K_DOWN:
                person_y += 10
            elif event.key == pygame.K_RIGHT:
                person_x += 10
            elif event.key == pygame.K_LEFT:
                person_x -= 10

    planet_x += planet_speed
    if planet_x > 450 or planet_x < 50:
        planet_speed *= -1

    for b in bullets[:]:
        b[1] -= 10 
        pygame.draw.rect(screen, (255, 255, 0), (b[0] - 2, b[1], 4, 10))

        distance = math.sqrt((b[0] - planet_x)**2 + (b[1] - planet_y)**2)
        if distance < planet_radius:
            score += 1
            bullets.remove(b)
            continue
            
        if b[1] < 0:
            bullets.remove(b)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


    draw_planet(screen, planet_x, planet_y)
    shape_dockalien(screen, person_x, person_y)
    pygame.display.flip()

    clock.tick(60) 

pygame.quit()