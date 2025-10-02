import pygame, json, sys

pygame.init()

# --- Paramètres ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 32

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mon Jeu Ogmo + Pygame")
clock = pygame.time.Clock()

# --- Charger le background ---
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # adapte à la taille écran

# --- Charger le fichier Ogmo ---
with open("niveau.json") as f:   # <= ton fichier Ogmo exporté
    data = json.load(f)

collision_rects = []

for layer in data["layers"]:
    if layer["name"] == "Collisions":   # ton layer invisible
        grid = layer["grid"]
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":  # 1 = bloc solide
                    rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    collision_rects.append(rect)

# --- Joueur (un carré rouge pour test) ---
player = pygame.Rect(100, 100, 32, 32)
velocity = pygame.Vector2(0, 0)
GRAVITY = 0.5
JUMP_FORCE = -10

debug = False  # touche D pour voir les collisions

# --- Boucle principale ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                debug = not debug  # activer/désactiver debug

    # --- Contrôles ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity.x = -3
    elif keys[pygame.K_RIGHT]:
        velocity.x = 3
    else:
        velocity.x = 0

    if keys[pygame.K_SPACE] and velocity.y == 0:  # saut si sur le sol
        velocity.y = JUMP_FORCE

    # --- Physique ---
    velocity.y += GRAVITY
    player.x += velocity.x
    player.y += velocity.y

    # --- Collisions ---
    for rect in collision_rects:
        if player.colliderect(rect):
            if velocity.y > 0:  # tombe
                player.bottom = rect.top
                velocity.y = 0

    # --- Dessin ---
    screen.blit(background, (0, 0))  # afficher le fond
    pygame.draw.rect(screen, (255, 0, 0), player)  # joueur

    # mode debug : afficher les blocs en vert
    if debug:
        for rect in collision_rects:
            pygame.draw.rect(screen, (0, 255, 0), rect, 1)

    pygame.display.flip()
    clock.tick(60)
