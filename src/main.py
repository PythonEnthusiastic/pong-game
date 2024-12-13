import pygame

pygame.init()

SCREEN_SIZE = (1280, 720)

class Racket:
    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.pos_y = (SCREEN_SIZE[1] / 2) - 50
        self.racket_speed = 7

    def move(self, direction):
        if direction == "up":
            self.pos_y -= self.racket_speed
        elif direction == "down":
            self.pos_y += self.racket_speed

        self.boundary()

    def boundary(self):
        y_bound = (0, 720 - 110)

        if self.pos_y > y_bound[1]:
            self.pos_y = y_bound[1]
        elif self.pos_y < y_bound[0]:
            self.pos_y = y_bound[0]

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.pos_x, self.pos_y, 20, 110))

class Ball:
    def __init__(self):
        self.radius = 20
        self.pos_x = SCREEN_SIZE[0]/2
        self.pos_y = SCREEN_SIZE[1]/2
        self.speed_x = 10
        self.speed_y = 0

    def move(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.boundary()

    def collision(self, racket1, racket2):
        racket1_pos = [racket1.pos_x, racket1.pos_y]
        racket2_pos = [racket2.pos_x, racket2.pos_y]

        if ((racket1_pos[0] - 40) <= self.pos_x <= (racket1_pos[0] + 40)) and ((racket1_pos[1] - 110 - 20) <= self.pos_y <= racket1_pos[1] + 110 + 20):
            self.speed_x *= -1
        elif ((racket2_pos[0] - 40) <= self.pos_x <= (racket2_pos[0] + 40)) and ((racket2_pos[1] - 110 - 20) <= self.pos_y <= racket2_pos[1] + 110 + 20):
            self.speed_x *= -1

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