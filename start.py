import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Setup the Display (Using your 16GB RAM, this will be instant)
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame")

# 3. Define Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 000, 255)

# 4. The Game Loop
running = True
clock = pygame.time.Clock() # Controls the speed (FPS)

while running:
    # A. Check for Events (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If you click the 'X'
            running = False

    # B. Game Logic (Update positions here)

    # C. Drawing
    screen.fill((30, 30, 30)) # Clear the screen first
    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100)) # Draw a blue square
    
    # D. Refresh the Screen
    pygame.display.flip()

    # E. Cap the Frame Rate (60 FPS is standard)
    clock.tick(60)

# 5. Quit
pygame.quit()