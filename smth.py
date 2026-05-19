import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# --- VARIABLES (OUTSIDE THE LOOP) ---
x, y = 400, 300
ex, ey = 0, 0
evx, evy = 0, 0    # These MUST stay out here to "remember" speed
friction = 0.95
respawn_timer = 0

running = True
while running: # Anything inside here repeats 60 times a second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # (Player movement and collision code goes here...)

    if respawn_timer > 0:
        respawn_timer -= 1
        current_bg = (20, 20, 20)
        # We also reset velocity here so he doesn't 
        # zoom away while he's supposed to be "dead"
        evx, evy = 0, 0 
    else:
        current_bg = "blue"
        # 1. Acceleration (Change velocity)
        if ex < x: evx += 0.2
        if ex > x: evx -= 0.2
        if ey < y: evy += 0.2
        if ey > y: evy -= 0.2

        # 2. Friction (Slow down slightly)
        evx *= friction
        evy *= friction

        # 3. Position (Apply the velocity)
        ex += evx
        ey += evy

    # (Drawing code goes here...)
    screen.fill(current_bg)
    pygame.draw.rect(screen, "white", (x, y, 50, 50))
    pygame.draw.rect(screen, "red", (ex, ey, 50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()