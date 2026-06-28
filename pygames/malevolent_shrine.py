import pygame
import math
import random
import copy

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create a dedicated display surface to handle clean screen shaking
display_surface = pygame.Surface((WIDTH, HEIGHT))
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
    global px, py, p_angle, score, game_state, current_map, last_dash, domain_active, shake_timer, slash_effects
    px, py, p_angle, score = 150, 150, 0, 0
    last_dash, shake_timer = 0, 0
    domain_active = False
    game_state = "PLAYING"
    current_map = copy.deepcopy(ORIGINAL_MAP)
    slash_effects = [] # Holds active slash lines for Cleave/Dismantle

reset_game()

def trigger_cleave():
    """Generates a flurry of sharp, fast slashes across the screen."""
    global slash_effects
    for _ in range(5):
        x1 = random.randint(100, WIDTH - 100)
        y1 = random.randint(100, HEIGHT - 100)
        length = random.randint(150, 400)
        
        # CHANGED THIS LINE: Gives a completely randomized 360-degree angle
        angle = random.uniform(0, 2 * math.pi) 
        
        x2 = x1 + length * math.cos(angle)
        y2 = y1 + length * math.sin(angle)
        slash_effects.append({"start": (x1, y1), "end": (x2, y2), "timer": 6})
                             
def cast_rays():
    NUM_RAYS = 120
    FOV = math.pi / (1.5 if domain_active else 3) # Wider, more chaotic FOV during domain
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
                    
                    # Cursed Energy Colors
                    if domain_active:
                        # Dark crimson walls that flicker slightly
                        color = (random.randint(40, 70), 0, 0)
                    else:
                        color = (150, 0, 0)
                        
                    if current_map[row][col] == 2: 
                        color = (255, 215, 0) # Gold Coin walls
                        
                    pygame.draw.rect(display_surface, color, (r * SCALE, (HEIGHT//2)-wall_h//2, SCALE, wall_h))
                    break

running = True
while running:
    now = pygame.time.get_ticks() / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: 
                reset_game()
            if event.key == pygame.K_q and game_state == "PLAYING" and (now - last_dash) > 0.4:
                px += math.cos(p_angle) * 180
                py += math.sin(p_angle) * 180
                last_dash = now
                shake_timer = 0.25
                trigger_cleave() # Cleave on dash!

    if game_state == "PLAYING":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: p_angle -= 0.07
        if keys[pygame.K_d]: p_angle += 0.07
        move = 6 if keys[pygame.K_w] else -6 if keys[pygame.K_s] else 0
        nx, ny = px + math.cos(p_angle) * move, py + math.sin(p_angle) * move
        
        # Simple Collision Logic
        if current_map[int(ny//TILE_SIZE)][int(nx//TILE_SIZE)] != 1:
            px, py = nx, ny
        elif not domain_active: 
            game_state = "LOSE"

        # Coin Tracking / Domain Activation
        cx, cy = int(px//TILE_SIZE), int(py//TILE_SIZE)
        if current_map[cy][cx] == 2:
            score += 1
            current_map[cy][cx] = 0
            shake_timer = 0.2
            trigger_cleave() # Slashing animation when ripping apart a cursed object
            if score >= 3: 
                domain_active = True

    # --- DRAWING (RENDER TO VIRTUAL SURFACE FIRST) ---
    display_surface.fill((25, 5, 5) if domain_active else (15, 15, 15))
    
    cast_rays()
    
    # Continuous Dismantle Slashes inside the Malevolent Shrine
    if domain_active and game_state == "PLAYING" and random.random() < 0.4:
        # Glitchy text effect
        text_color = (255, 0, 0) if random.random() > 0.1 else (255, 255, 255)
        msg = font.render("DOMAIN EXPANSION: MALEVOLENT SHRINE", True, text_color)
        display_surface.blit(msg, (WIDTH//2 - msg.get_width()//2, 50))
        trigger_cleave()
        shake_timer = 0.15

    # Render Active Slash Animations (Cleave/Dismantle Effects)
    for slash in slash_effects[:]:
        # Bright red/white cursed energy cuts
        color = random.choice([(255, 255, 255), (255, 0, 0), (180, 0, 0)])
        thickness = random.randint(2, 6)
        pygame.draw.line(display_surface, color, slash["start"], slash["end"], thickness)
        slash["timer"] -= 1
        if slash["timer"] <= 0:
            slash_effects.remove(slash)

    if game_state == "LOSE":
        msg = font.render("CLEAVED & DISMANTLED - Press R", True, "white")
        display_surface.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))

    # --- SCREEN SHAKE & FINAL BLIT ---
    offset_x, offset_y = 0, 0
    if shake_timer > 0:
        intensity = 15 if domain_active else 8 # Domain makes screen shake violent
        offset_x = random.randint(-intensity, intensity)
        offset_y = random.randint(-intensity, intensity)
        shake_timer -= 0.016 # Roughly tied to 60 FPS delta

    # Clear main screen, then safely blit the display surface with the offset
    screen.fill((0, 0, 0))
    screen.blit(display_surface, (offset_x, offset_y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()