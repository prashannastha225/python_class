import pygame
import random

# 1. Setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rainbow Painter - 'C' to Clear, Right Click to Erase")
clock = pygame.time.Clock()

# Start with a black screen
screen.fill((0, 0, 0))

# Variables for the "messing around" features
hue = 0
running = True

while running:
    # A. Check for specific button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # CLEAR SCREEN: If user presses the 'C' key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill((0, 0, 0))

    # B. Mouse Logic
    mouse_buttons = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if mouse_buttons[0]: # LEFT CLICK: Draw Rainbow
        # This part makes the "smooth" color transition
        color = pygame.Color(0)
        color.hsva = (hue, 100, 100, 100) 
        pygame.draw.circle(screen, color, pos, 5)
        
        hue = (hue + 2) % 360 # Change color speed (higher = faster rainbow)

    elif mouse_buttons[2]: # RIGHT CLICK: Erase
        # Draw big black circles to "wipe" the screen
        pygame.draw.circle(screen, (0, 0, 0), pos, 30)

    # C. Update Display
    pygame.display.flip()
    
    # Keeping it at 120 FPS for that smooth DDR5 feel
    clock.tick(10000)

pygame.quit()