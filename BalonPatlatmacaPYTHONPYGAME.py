import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balon Patlatma Oyunu")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - 40
paddle_speed = 10
BALL_RADIUS = 15
ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
ball_y = HEIGHT // 2
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = -5
NUM_BALLOONS = 300
balloons = []
for _ in range(NUM_BALLOONS):
    bx = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
    by = random.randint(BALL_RADIUS, HEIGHT // 2)
    balloons.append([bx, by])
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        ball_speed_x *= -1
    if ball_y - BALL_RADIUS <= 0:
        ball_speed_y *= -1
    if paddle_y <= ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
        ball_speed_y *= -1
    if ball_y + BALL_RADIUS >= HEIGHT:
        print("Oyun Bitti!")
        running = False
    for balloon in balloons[:]:
        bx, by = balloon
        if (bx - BALL_RADIUS <= ball_x <= bx + BALL_RADIUS) and (by - BALL_RADIUS <= ball_y <= by + BALL_RADIUS):
            balloons.remove(balloon)
            ball_speed_y *= -1
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    for bx, by in balloons:
        pygame.draw.circle(screen, GREEN, (bx, by), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
