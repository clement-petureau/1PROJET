import pygame
import sys

pygame.init()

# Dimensions de la fenêtre
screen_width = 1000  
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Katarenga")

# Couleur de fond
White = (255, 255, 255)
Gray = (200, 200, 200)
DarkGray = (169, 169, 169)
Black = (0, 0, 0)

# Couleur boutons

Blue = (0, 0, 255)
Red = (255, 0, 0)

# Charger les images des cases
BlueCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Plateau\Image\Blue.png")
RedCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Plateau\Image\Red.png")
YellowCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Plateau\Image\Yellow.png")
GreenCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Plateau\Image\Green.png")

# Dimensions des images
BlueCase = pygame.transform.scale(BlueCase, (75, 75))
RedCase = pygame.transform.scale(RedCase, (75, 75))
YellowCase = pygame.transform.scale(YellowCase, (75, 75))
GreenCase = pygame.transform.scale(GreenCase, (75, 75))

# Les paternes de chaque quadrant pris du sujet
quadrant1 = [
    "BYGR",
    "GYRY",
    "RBGB",
    "YRBG"
]

quadrant2 = [
    "YBGR",
    "RGYY",
    "GRBB",
    "BYRG"
]

quadrant3 = [
    "GRYB",
    "BGRG",
    "YYBR",
    "RGBY"
]

quadrant4 = [
    "GBRY",
    "RGBB",
    "YRYG",
    "BGYR"
]

# Pour avoir la bonne image dans chaque case
def get_case_image(char):
    if char == 'B':
        return BlueCase
    elif char == 'R':
        return RedCase
    elif char == 'Y':
        return YellowCase
    elif char == 'G':
        return GreenCase
    else:
        return None

# Pour afficher les boutons
def draw_button(screen, text, x, y, width, height, inactive_color, active_color, font):
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_surface = font.render(text, True, Black)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

# Boucle principale
running = True
font = pygame.font.Font(None, 36)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir l'écran avec une couleur de fond
    screen.fill(White)

    # Dessiner le plateau de jeu
    for row in range(8):  # 8 lignes
        for col in range(8):  # 8 colonnes
            x = col * 75
            y = row * 75

            # Ajouter un espace de 10 pixels entre les quadrants
            if row >= 4:
                y += 10
            if col >= 4:
                x += 10

            if row < 4 and col < 4:
                char = quadrant1[row][col]
            elif row < 4 and col >= 4:
                char = quadrant2[row][col - 4]
            elif row >= 4 and col < 4:
                char = quadrant3[row - 4][col]
            else:
                char = quadrant4[row - 4][col - 4]

            case_image = get_case_image(char)
            if case_image:
                screen.blit(case_image, (x, y))

    # Dessiner les boutons
    draw_button(screen, "Forfeit", 820, 100, 150, 50, Blue, Red, font)
    draw_button(screen, "Break", 820, 200, 150, 50, Blue, Red, font)
    draw_button(screen, "Save", 820, 300, 150, 50, Blue, Red, font)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()

