import pygame

pygame.init()

SCREEN_SIZE = (1280, 720)

class Racket:
    def __init__(self, pos_x):
        self.racket = pygame.Rect(pos_x, 30, 15, 110)
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
        self.radius = 15
        self.pos_x = SCREEN_SIZE[0]/2
        self.pos_y = SCREEN_SIZE[1]/2
        self.ball_speed = 10

    def move(self):
        self.pos_x += self.ball_speed
        self.boundary()

    def collision(self):
        pass

    def boundary(self):
        if self.pos_x > SCREEN_SIZE[0] or self.pos_x < 0:
            self.pos_x = SCREEN_SIZE[0]/2
            self.pos_y = SCREEN_SIZE[1]/2

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.pos_x, self.pos_y), self.radius)


class Pong:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.first_racket = Racket(20)
        self.second_racket = Racket((1280 - 15) - 23)
        self.ball = Ball()

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

    def update_positions(self):
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
            self.update_positions()
            self.ball.move()

            pygame.display.flip()

            self.clock.tick(60)
    
        pygame.quit()

if __name__ == "__main__":
    game = Pong()
    game.run()