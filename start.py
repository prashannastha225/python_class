import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame")

# 3. Define Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 000, 255)

# 4. The Game Loop
running = True

while running:

    # A. Check for Events (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If you click the 'X'
            running = False

    # B. Drawing
    screen.fill((30, 30, 30)) # Clear the screen first
    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100))#Draw a blue square

    # C. Refresh the Screen
    pygame.display.flip()

pygame.quit()