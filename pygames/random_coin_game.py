import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 60, bold=True)
small_font = pygame.font.SysFont('consolas', 32, bold=True)

# Entities
player = pygame.Rect(200, 200, 40, 40)
coin = pygame.Rect(0, 0, 30, 30)
kill_brick = pygame.Rect(540, 260, 200, 200) 
start_button = pygame.Rect(440, 310, 400, 100)

score = 0
timer = 3.0
game_state = "MENU"

# Dash settings
base_speed = 7
dash_distance = 180
dash_cooldown = 0.4
last_dash_time = 0

def move_coin():
    while True:
        new_rect = pygame.Rect(random.randint(100, 1100), random.randint(100, 600), 30, 30)
        if not new_rect.colliderect(kill_brick):
            coin.topleft = new_rect.topleft
            break

def reset_game():
    global score, timer, game_state
    score = 0
    timer = 3.0
    player.topleft = (100, 100)
    move_coin()
    game_state = "PLAYING"

running = True
while running:
    dt = clock.tick(60) / 1000.0
    current_time = pygame.time.get_ticks() / 1000.0 
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # DASH LOGIC - Reliable Event Trigger
        if event.type == pygame.KEYDOWN and game_state == "PLAYING":
            if event.key == pygame.K_q and (current_time - last_dash_time) > dash_cooldown:
                keys = pygame.key.get_pressed()
                mx, my = 0, 0
                if keys[pygame.K_w]: my = -1
                if keys[pygame.K_s]: my = 1
                if keys[pygame.K_a]: mx = -1
                if keys[pygame.K_d]: mx = 1
                
                if mx != 0 or my != 0:
                    player.x += mx * dash_distance
                    player.y += my * dash_distance
                    last_dash_time = current_time

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MENU" and start_button.collidepoint(mouse_pos):
                reset_game()
            elif game_state in ["WIN", "LOSE"]:
                game_state = "MENU"

    if game_state == "PLAYING":
        timer -= dt
        if timer <= 0: game_state = "LOSE"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player.y -= base_speed
        if keys[pygame.K_s]: player.y += base_speed
        if keys[pygame.K_a]: player.x -= base_speed
        if keys[pygame.K_d]: player.x += base_speed
        
        player.clamp_ip(screen.get_rect())
        if player.colliderect(kill_brick): game_state = "LOSE"
        if player.colliderect(coin):
            score += 1
            timer = 3.0
            move_coin()
            if score >= 25: game_state = "WIN"

    # --- DRAWING ---
    screen.fill("black")
    
    if game_state == "MENU":
        pygame.draw.rect(screen, "white", start_button, 5)
        screen.blit(font.render("START GAME", True, "white"), (start_button.x + 35, start_button.y + 20))

    elif game_state == "PLAYING":
        pygame.draw.rect(screen, (255, 50, 50), kill_brick)
        pygame.draw.rect(screen, (0, 200, 255), player) 
        pygame.draw.rect(screen, (255, 215, 0), coin) 
        
        # SCORE & TIMER
        screen.blit(font.render(f"SCORE: {score}/25", True, "white"), (20, 20))
        t_color = "red" if timer < 1.0 else "white"
        screen.blit(font.render(f"{round(timer, 1)}", True, t_color), (1100, 20))
        
        # --- FIXED DASH GUI BOX ---
        dash_ready = (current_time - last_dash_time) > dash_cooldown
        gui_color = (0, 255, 255) if dash_ready else (80, 80, 80)
        
        gui_rect = pygame.Rect(20, 100, 300, 50)
        
        # Draw the outline
        pygame.draw.rect(screen, gui_color, gui_rect, 3)
        
        # Optional: Add a slight background fill when ready to make it "pop"
        if dash_ready:
            inner_rect = pygame.Rect(23, 103, 294, 44)
            # Semi-transparent feel (just a darker cyan)
            pygame.draw.rect(screen, (0, 100, 100), inner_rect)

        status_text = "DASH READY [Q]" if dash_ready else "RECHARGING..."
        # Shifted text slightly to the right for better centering
        screen.blit(small_font.render(status_text, True, gui_color), (35, 108))
    elif game_state == "LOSE":
        screen.blit(font.render("U DED", True, "red"), (500, 300))
    elif game_state == "WIN":
        screen.blit(font.render("GOAT STATUS!", True, "green"), (450, 300))

    pygame.display.flip()
pygame.quit()