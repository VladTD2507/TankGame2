import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.health = 100
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (0, 255, 0)
        self.direction = "UP"

    def move(self, direction):
        self.direction = direction
        if direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed
        elif direction == "LEFT":
            self.x -= self.speed
        elif direction == "RIGHT":
            self.x += self.speed
        
        self.rect.topleft = (self.x, self.y)

    def shoot(self, bullet_manager):
        bx = self.x + self.width // 2 - 3
        by = self.y + self.height // 2 - 3
        bullet_manager.add_bullet(bx, by, self.direction, "player")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        ix, iy = self.x + 15, self.y + 15
        if self.direction == "UP": iy -= 10
        elif self.direction == "DOWN": iy += 10
        elif self.direction == "LEFT": ix -= 10
        elif self.direction == "RIGHT": ix += 10
        
        indicator_rect = pygame.Rect(ix, iy, 10, 10)
        pygame.draw.rect(screen, (0, 100, 0), indicator_rect)

    def update(self):
        pass
