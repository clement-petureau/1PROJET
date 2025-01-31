import pygame
import sys

pygame.init()

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Katarenga")

# Couleur de fond
White = (255, 255, 255)

# Charger les images des cases
BlueCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Image\Blue.png")
RedCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Image\Red.png")
YellowCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Image\Yellow.png")
GreenCase = pygame.image.load(r"C:\Users\rayha\.vscode\Projet Final\Image\Green.png")

# Redimensionner les images 
BlueCase = pygame.transform.scale(BlueCase, (75, 75))
RedCase = pygame.transform.scale(RedCase, (75, 75))
YellowCase = pygame.transform.scale(YellowCase, (75, 75))
GreenCase = pygame.transform.scale(GreenCase, (75, 75))

# Patterns for each quadrant
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

# Function to get the correct image based on the character
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

# Boucle principale
running = True
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

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()
