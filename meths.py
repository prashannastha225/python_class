import pygame
import math
import random
import copy

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 50, bold=True)

# --- MAP DATA ---
ORIGINAL_MAP = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,0,0,0,1,2,0,0,0,1],
    [1,0,0,0,0,0,0,2,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]
TILE_SIZE = 100

def reset_game():
    global px, py, p_angle, score, game_state, current_map, last_dash, domain_active, shake_timer
    px, py, p_angle, score = 150, 150, 0, 0
    last_dash, shake_timer = 0, 0
    domain_active = False
    game_state = "PLAYING"
    current_map = copy.deepcopy(ORIGINAL_MAP)

reset_game()

def cast_rays():
    # If Domain is active, we use "Cursed Vision" (Infinite FOV feel)
    NUM_RAYS = 120
    FOV = math.pi / (2 if domain_active else 3) 
    SCALE = WIDTH // NUM_RAYS
    for r in range(NUM_RAYS):
        angle = (p_angle - FOV/2) + r * (FOV / NUM_RAYS)
        for depth in range(1, 1000):
            tx, ty = px + depth * math.cos(angle), py + depth * math.sin(angle)
            col, row = int(tx // TILE_SIZE), int(ty // TILE_SIZE)
            if 0 <= row < len(current_map) and 0 <= col < len(current_map[0]):
                if current_map[row][col] > 0:
                    depth *= math.cos(p_angle - angle)
                    wall_h = 21000 / (depth + 0.0001)
                    # Domain colors: Black and Deep Red
                    color = (150, 0, 0) if not domain_active else (50, 0, 0)
                    if current_map[row][col] == 2: color = (255, 215, 0)
                    pygame.draw.rect(screen, color, (r * SCALE, (HEIGHT//2)-wall_h//2, SCALE, wall_h))
                    break

running = True
while running:
    now = pygame.time.get_ticks() / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: reset_game()
            if event.key == pygame.K_q and game_state == "PLAYING" and (now - last_dash) > 0.4:
                px += math.cos(p_angle) * 180
                py += math.sin(p_angle) * 180
                last_dash, shake_timer = now, 0.2 # Dash shake

    if game_state == "PLAYING":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: p_angle -= 0.07
        if keys[pygame.K_d]: p_angle += 0.07
        move = 6 if keys[pygame.K_w] else -6 if keys[pygame.K_s] else 0
        nx, ny = px + math.cos(p_angle) * move, py + math.sin(p_angle) * move
        
        # Simple Collision
        if current_map[int(ny//TILE_SIZE)][int(nx//TILE_SIZE)] != 1:
            px, py = nx, ny
        elif not domain_active: game_state = "LOSE"

        # Coin / Domain Trigger
        cx, cy = int(px//TILE_SIZE), int(py//TILE_SIZE)
        if current_map[cy][cx] == 2:
            score += 1
            current_map[cy][cx] = 0
            shake_timer = 0.3 # Hit shake
            if score >= 3: domain_active = True

    # --- DRAWING ---
    # Screen Shake Logic
    offset = (0,0)
    if shake_timer > 0:
        offset = (random.randint(-10, 10), random.randint(-10, 10))
        shake_timer -= 0.02

    screen.fill((20, 0, 0) if domain_active else (10, 10, 10))
    temp_surf = pygame.Surface((WIDTH, HEIGHT))
    
    cast_rays()
    
    if domain_active:
        msg = font.render("DOMAIN EXPANSION", True, (255, 0, 0))
        screen.blit(msg, (WIDTH//2 - 200, 50))

    if game_state == "LOSE":
        msg = font.render("U DED 💀 - Press R", True, "white")
        screen.blit(msg, (WIDTH//2 - 200, HEIGHT//2))

    # Apply Shake
    screen.blit(screen, offset)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()