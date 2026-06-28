import pygame
import math
import random
import copy

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 45, bold=True)

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
    global px, py, p_angle, score, game_state, current_map, last_dash, domain_active, shake_timer, stars, ink_splatters
    px, py, p_angle, score = 150, 150, 0, 0
    last_dash, shake_timer = 0, 0
    domain_active = False
    game_state = "PLAYING"
    current_map = copy.deepcopy(ORIGINAL_MAP)
    ink_splatters = [] # Holds active white ink splashes
    
    # Generate random stars for Gojo's space void background
    stars = []
    for _ in range(150):
        stars.append({
            "x": random.randint(0, WIDTH),
            "y": random.randint(0, HEIGHT),
            "speed": random.uniform(0.5, 3.0),
            "size": random.randint(1, 3)
        })

reset_game()

def trigger_ink_splatter(amount=15):
    """Generates chaotic, high-contrast white paint splatters across the viewport."""
    global ink_splatters
    for _ in range(amount):
        cx = random.randint(100, WIDTH - 100)
        cy = random.randint(100, HEIGHT - 100)
        base_radius = random.randint(8, 25)
        
        # Main ink droplet core
        ink_splatters.append({
            "type": "circle",
            "x": cx,
            "y": cy,
            "r": base_radius,
            "timer": random.randint(15, 35)
        })
        
        # Micro-splatters shooting off the main droplet
        for _ in range(random.randint(3, 6)):
            angle = random.uniform(0, 2 * math.pi)
            dist = random.randint(base_radius, base_radius + 30)
            ink_splatters.append({
                "type": "circle",
                "x": cx + int(dist * math.cos(angle)),
                "y": cy + int(dist * math.sin(angle)),
                "r": random.randint(2, 5),
                "timer": random.randint(10, 25)
            })

def draw_infinite_void_black_hole():
    """Draws a cinematic black hole with a golden warped light ring and accretion disk."""
    bh_x, bh_y = WIDTH // 2, HEIGHT // 2
    
    # Outer Einstein Ring Glow
    for radius in range(140, 90, -4):
        glow_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        g_color = (random.randint(230, 255), random.randint(170, 200), random.randint(0, 50), 12)
        pygame.draw.circle(glow_surf, g_color, (radius, radius), radius)
        display_surface.blit(glow_surf, (bh_x - radius, bh_y - radius))

    # Horizontal Accretion Disk
    for h_thick in range(40, 10, -5):
        disk_surf = pygame.Surface((340, h_thick * 2), pygame.SRCALPHA)
        d_color = (random.randint(240, 255), random.randint(180, 215), 0, 25)
        pygame.draw.ellipse(disk_surf, d_color, (0, 0, 340, h_thick * 2))
        display_surface.blit(disk_surf, (bh_x - 170, bh_y - h_thick))

    # Inner Core Accretion Edge
    pygame.draw.circle(display_surface, (255, 200, 20), (bh_x, bh_y), 83, 4)
    pygame.draw.circle(display_surface, (255, 165, 0), (bh_x, bh_y), 81, 2)

    # Event Horizon
    pygame.draw.circle(display_surface, (2, 1, 5), (bh_x, bh_y), 79)

def cast_rays():
    NUM_RAYS = 120
    FOV = math.pi / (1.4 if domain_active else 3) 
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
                    
                    if current_map[row][col] == 2: 
                        color = (0, 255, 255)
                        pygame.draw.rect(display_surface, color, (r * SCALE, (HEIGHT//2)-wall_h//2, SCALE, wall_h))
                    else:
                        if domain_active:
                            wall_surf = pygame.Surface((SCALE, int(wall_h)))
                            wall_surf.fill((10, 2, random.randint(30, 50)))
                            wall_surf.set_alpha(155) 
                            display_surface.blit(wall_surf, (r * SCALE, (HEIGHT//2)-int(wall_h)//2))
                        else:
                            color = (0, 0, 130)
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
                shake_timer = 0.15
                trigger_ink_splatter(4)

    if game_state == "PLAYING":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: p_angle -= 0.07
        if keys[pygame.K_d]: p_angle += 0.07
        move = 6 if keys[pygame.K_w] else -6 if keys[pygame.K_s] else 0
        nx, ny = px + math.cos(p_angle) * move, py + math.sin(p_angle) * move
        
        if current_map[int(ny//TILE_SIZE)][int(nx//TILE_SIZE)] != 1:
            px, py = nx, ny
        elif not domain_active: 
            game_state = "LOSE"

        cx, cy = int(px//TILE_SIZE), int(py//TILE_SIZE)
        if current_map[cy][cx] == 2:
            score += 1
            current_map[cy][cx] = 0
            shake_timer = 0.2
            trigger_ink_splatter(6)
            if score >= 3: 
                domain_active = True
                trigger_ink_splatter(35) # Epic ink explosion!

    # --- DRAWING ---
    display_surface.fill((2, 1, 6))
    
    # 1. Background Starfield
    for star in stars:
        star_color = random.choice([(255, 255, 255), (160, 230, 255), (210, 190, 255)]) if domain_active else (90, 90, 90)
        pygame.draw.circle(display_surface, star_color, (int(star["x"]), int(star["y"])), star["size"])
        
        star["x"] -= star["speed"] if domain_active else (star["speed"] * 0.15)
        if star["x"] < 0:
            star["x"] = WIDTH
            star["y"] = random.randint(0, HEIGHT)

    # 2. Gojo's Singularity (Behind Walls)
    if domain_active:
        draw_infinite_void_black_hole()

    # 3. Project Raycasted Walls Over Space Background
    cast_rays()
    
    # 4. Continuous Ambient Ink Drops inside active Infinite Void
    if domain_active and game_state == "PLAYING" and random.random() < 0.15:
        trigger_ink_splatter(1)

    # 5. FIXED: Render and Process Anime White Splatters
    for splash in ink_splatters[:]:
        alpha = min(255, splash["timer"] * 12)
        splash_surf = pygame.Surface((splash["r"]*2, splash["r"]*2), pygame.SRCALPHA)
        
        # Correctly using splash_surf here now
        pygame.draw.circle(splash_surf, (255, 255, 255, alpha), (splash["r"], splash["r"]), splash["r"])
        display_surface.blit(splash_surf, (splash["x"] - splash["r"], splash["y"] - splash["r"]))
        
        splash["timer"] -= 1
        if splash["timer"] <= 0:
            ink_splatters.remove(splash)
    
    if domain_active and game_state == "PLAYING":
        msg = font.render("DOMAIN EXPANSION: INFINITE VOID", True, (0, 225, 255))
        display_surface.blit(msg, (WIDTH//2 - msg.get_width()//2, 50))
        shake_timer = 0.04 

    if game_state == "LOSE":
        msg = font.render("BRAIN PARALYZED BY INFINITE DATA - Press R", True, "white")
        display_surface.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))

    # --- SCREEN SHAKE & FINAL BLIT ---
    offset_x, offset_y = 0, 0
    if shake_timer > 0:
        intensity = 3 if domain_active else 1
        offset_x = random.randint(-intensity, intensity)
        offset_y = random.randint(-intensity, intensity)
        shake_timer -= 0.016

    screen.fill((0, 0, 0))
    screen.blit(display_surface, (offset_x, offset_y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()