import pygame

class Bullet:
    def __init__(self, x, y, direction, owner_type):
        self.x = x
        self.y = y
        self.speed = 7
        self.direction = direction
        self.owner_type = owner_type
        self.width = 6
        self.height = 6
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = True

    def update(self):
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed
        
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
