#for now this is incomplete

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Chess")

def Pawn():
    pass

def Knight():
    pass

def Bishop():
    pass

def Rook():
    pass

def Queen():
    pass

def King():
    pass

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    dt = clock.tick(60) / 1000.0
    current_time = pygame.time.get_ticks() / 1000.0 
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

