import pygame
import sys

# 1. Start Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Safe Test - Click to Draw")
clock = pygame.time.Clock()

# Set background once
screen.fill((20, 20, 20))

running = True
while running:
    # 2. THE BRAIN: This part prevents the "on and on" freezing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Emergency Exit
                running = False

    # 3. DRAWING: Only if you click
    if pygame.mouse.get_pressed()[0]: # Left Click
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255, 255, 255), pos, 10)

    # 4. REFRESH
    pygame.display.flip()
    
    # 5. BRAKES: This stops the CPU from going crazy
    clock.tick(30) 

pygame.quit()
sys.exit()