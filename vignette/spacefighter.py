import pygame
import os

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
BG = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds', 'space.png')), (WIDTH, HEIGHT))

# Text
HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WIN_FONT = pygame.font.SysFont('comicsans', 80)
WHITE = (255,255,255)

# Sound
RED_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets/sfx', 'red_hit.wav'))
RED_BULLET_SOUND = pygame.mixer.Sound(os.path.join('assets/sfx', 'red_laser.mp3'))
GREEN_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets/sfx', 'green_hit.wav'))
GREEN_BULLET_SOUND = pygame.mixer.Sound(os.path.join('assets/sfx', 'green_laser.mp3'))

# Define movement constants
FPS = 60
VEL = 6
BULLET_VEL = 10
MAX_BULLETS = 3

# User events for collisions
RED_HIT = pygame.USEREVENT + 1
GREEN_HIT = pygame.USEREVENT + 2

# Define player ship constants
SHIP_WIDTH, SHIP_HEIGHT = 179//1.5, 200//1.5
RED_SHIP = pygame.image.load(os.path.join('./assets/cats', 'red.png'))
GREEN_SHIP = pygame.image.load(os.path.join('./assets/cats', 'green.png'))
YS = pygame.transform.scale(RED_SHIP, (SHIP_WIDTH,SHIP_HEIGHT))
BS = pygame.transform.scale(GREEN_SHIP, (SHIP_WIDTH,SHIP_HEIGHT))

RED = (224,16,115)
GREEN = (85,192,152)

pygame.display.set_caption("Cats in Space!")

def draw_window(red, green, red_bullets, green_bullets, red_health, green_health):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, (0,0,0), BORDER)

    red_health_text = HEALTH_FONT.render("Floofer Health: " + str(red_health), 1, RED)
    green_health_text = HEALTH_FONT.render("Goober Health: " + str(green_health), 1, GREEN)
    WIN.blit(green_health_text, (WIDTH - green_health_text.get_width() -10, 10))
    WIN.blit(red_health_text, (10, 10))

    WIN.blit(YS, (red.x, red.y))
    WIN.blit(BS, (green.x, green.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in green_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

    pygame.display.update()

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - VEL > 0: # left
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + red.width < BORDER.x: # right
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0: # up
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + red.height < HEIGHT: # down
        red.y += VEL

def green_movement(keys_pressed, green):
    if keys_pressed[pygame.K_LEFT] and green.x - VEL > BORDER.x + BORDER.width: # left
        green.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and green.x + green.width < WIDTH: # right
        green.x += VEL
    if keys_pressed[pygame.K_UP] and green.y - VEL > 0: # up
        green.y -= VEL
    if keys_pressed[pygame.K_DOWN] and green.y + VEL + green.height < HEIGHT: # down
        green.y += VEL

def handle_bullets(red_bullets, green_bullets, red, green):
    for bull in red_bullets:
        bull.x += BULLET_VEL
        # check collisions
        if green.colliderect(bull):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            red_bullets.remove(bull)
        elif bull.x >= WIDTH:
            red_bullets.remove(bull)

    for bull in green_bullets:
        bull.x -= BULLET_VEL
        # check collisions
        if red.colliderect(bull):
            pygame.event.post(pygame.event.Event(RED_HIT))
            green_bullets.remove(bull)
        elif bull.x <= 0:
            green_bullets.remove(bull)

def draw_winner(text):
    draw_text = WIN_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2  - draw_text.get_height()//2))
    
    pygame.display.update()
    pygame.time.delay(10000)

def main():
    red = pygame.Rect(100, 300, SHIP_WIDTH, SHIP_HEIGHT)
    green = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)

    red_bullets = []
    green_bullets = []

    red_health = 5
    green_health = 5
    winner_text = ""

    clock = pygame.time.Clock()
    run = True

    # game loop
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width, red.y + 16, 10, 5)
                    red_bullets.append(bullet)
                    RED_BULLET_SOUND.play()

                if event.key == pygame.K_RSHIFT and len(green_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(green.x, green.y + 16, 10, 5)
                    green_bullets.append(bullet)
                    GREEN_BULLET_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                RED_HIT_SOUND.play()

            if event.type == GREEN_HIT:
                green_health -= 1
                GREEN_HIT_SOUND.play()

        if red_health <= 0:
            winner_text = "Goober wins!"
        if green_health <= 0:
            winner_text = "Floofer wins!"
            
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed, red)
        green_movement(keys_pressed, green)
        handle_bullets(red_bullets, green_bullets, red, green)

        draw_window(red, green, red_bullets, green_bullets, red_health, green_health)

    pygame.quit()


if __name__ == "__main__":
    main()