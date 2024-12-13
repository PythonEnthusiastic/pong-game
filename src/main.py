import pygame

pygame.init()

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

class Pong:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.first_racket = Racket(20)
        self.second_racket = Racket((1280 - 15) - 23)

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

    def update_racket_position(self):
        self.first_racket.draw(self.screen)
        self.second_racket.draw(self.screen)
            
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            self.handle_player_keys()
            self.update_racket_position()

            pygame.display.flip()

            self.clock.tick(60)
    
        pygame.quit()

if __name__ == "__main__":
    game = Pong()
    game.run()