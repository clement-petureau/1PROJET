import pygame
import sys
pygame.init()

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Katarenga")

# Les couleurs
White = (255, 255, 255)
Gray = (128, 128, 128)
DarkGray = (169,169,169)

# Boucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(White) # Pour mettre l'écran en blanc
    
    for row in range(8): # Pour déssiner le plateau de jeu
        for col in range(8):
            rect = pygame.Rect(col * 75, row * 75, 75, 75)
            if (row + col) % 4 == 0:
                pygame.draw.rect(screen, Gray, rect)
            elif (row + col) % 3 == 0:
                pygame.draw.rect(screen, Gray, rect)
            elif (row+col) % 5 == 0:
                pygame.draw.rect(screen, Gray, rect)
            else:
                pygame.draw.rect(screen, Gray, rect)

    pygame.display.flip() # Met a jour les changements

pygame.quit() # Fermeture de la page
sys.exit()








