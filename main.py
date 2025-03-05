import pygame
import sys


class Racket:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, racket_w, racket_h)

    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= speed_racket
        if keys[down] and self.rect.bottom < height:
            self.rect.y += speed_racket

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ball_size, ball_size)
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)

    def reset(self):
        self.rect.center = (width // 2, height // 2)
        self.speed_x *= -1


if __name__ == '__main__':
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Понг")

    racket_w, racket_h = 10, 100
    ball_size = 20
    fps = 60

    speed_racket = 5
    ball_speed_x, ball_speed_y = 4, 4

    paddle1 = Racket(30, height // 2 - racket_h // 2)
    paddle2 = Racket(width - 30 - racket_w, height // 2 - racket_h // 2)
    ball = Ball(width // 2 - ball_size // 2, height // 2 - ball_size // 2)

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        paddle1.move(pygame.K_w, pygame.K_s)
        paddle2.move(pygame.K_UP, pygame.K_DOWN)

        ball.move()

        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        if ball.rect.left <= 0 or ball.rect.right >= width:
            ball.reset()

        screen.fill((0, 0, 0))
        paddle1.draw()
        paddle2.draw()
        ball.draw()
        pygame.display.flip()
        clock.tick(fps)