import pygame

pygame.init()

SCREEN_SIZE = (1280, 720) # (x, y)
PADDLE_SIZE = (20, 110) # (width, height)
BALL_RADIUS = 20 

class Racket:
    def __init__(self, pos_x):
        self.racket = pygame.Rect(pos_x, (SCREEN_SIZE[1] / 2) - 50, 20, 110)
        self.racket_speed = 7

    def move(self, direction):
        if direction == "up":
            self.racket.y -= self.racket_speed
        elif direction == "down":
            self.racket.y += self.racket_speed

        self.boundary()

    def boundary(self):
        y_bound = (0, 720 - 110)

        if self.racket.y > y_bound[1]:
            self.racket.y = y_bound[1]
        elif self.racket.y < y_bound[0]:
            self.racket.y = y_bound[0]

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.racket)

class Ball:
    def __init__(self):
        self.ball = pygame.Rect(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, BALL_RADIUS, BALL_RADIUS)
        self.speed_x = 10
        self.speed_y = 0

    def move(self):
        self.ball.x += self.speed_x
        self.ball.y += self.speed_y
        self.boundary()

    def collision(self, racket1, racket2):
        if self.ball.colliderect(racket1.racket) or self.ball.colliderect(racket2.racket):
            self.speed_x *= -1

    def boundary(self):
        if self.ball.x > SCREEN_SIZE[0] or self.ball.x < 0:
            self.ball.x = SCREEN_SIZE[0]/2
            self.ball.y = SCREEN_SIZE[1]/2

    def draw(self, screen):
        pygame.draw.ellipse(screen, "red", self.ball)

class Pong:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.first_racket = Racket(20)
        self.second_racket = Racket((1280 - 15) - 23)
        self.ball = Ball()
        self.second_scoreboard = 0
        self.first_scoreboard = 0

    def handle_player_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.first_racket.move("up")
        if keys[pygame.K_s]:
            self.first_racket.move("down")
        if keys[pygame.K_UP]:
            self.second_racket.move("up")
        if keys[pygame.K_DOWN]:
            self.second_racket.move("down")

    def handle_ball(self):
        self.ball.move()
        self.ball.collision(self.first_racket, self.second_racket)

    def draw_objects(self):
        self.first_racket.draw(self.screen)
        self.second_racket.draw(self.screen)
        self.ball.draw(self.screen)
            
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("black")


            self.handle_player_keys()
            self.handle_ball()
            self.draw_objects()

            pygame.display.flip()

            self.clock.tick(60)
    
        pygame.quit()

if __name__ == "__main__":
    pong = Pong()
    pong.run()