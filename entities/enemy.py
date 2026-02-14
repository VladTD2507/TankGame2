import pygame
import random
from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.health = 50
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.shoot_timer = 0

    @abstractmethod
    def move(self, obstacles, player_rect):
        pass

    def shoot(self, bullet_manager):
        self.shoot_timer += 1
        if self.shoot_timer >= 60:
            bx = self.x + self.width // 2 - 3
            by = self.y + self.height // 2 - 3
            bullet_manager.add_bullet(bx, by, self.direction, "enemy")
            self.shoot_timer = 0

    def take_damage(self, amount):
        self.health -= amount

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        indicator_rect = pygame.Rect(self.x + 15, self.y + 15, 10, 10)
        pygame.draw.rect(screen, (150, 0, 0), indicator_rect)

class StraightEnemy(Enemy):
    def move(self, obstacles, player_rect):
        old_x, old_y = self.x, self.y
        
        if self.direction == "UP": self.y -= self.speed
        elif self.direction == "DOWN": self.y += self.speed
        elif self.direction == "LEFT": self.x -= self.speed
        elif self.direction == "RIGHT": self.x += self.speed
        
        self.rect.topleft = (self.x, self.y)
        
        collision = False
        if self.x < 0 or self.x > 760 or self.y < 0 or self.y > 560:
            collision = True
        
        if not collision and self.rect.colliderect(player_rect):
            collision = True

        if not collision:
            for obs in obstacles:
                if self.rect.colliderect(obs.rect):
                    collision = True
                    break
        
        if collision:
            self.x, self.y = old_x, old_y
            self.rect.topleft = (self.x, self.y)
            reverse = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
            self.direction = reverse[self.direction]

class RandomEnemy(Enemy):
    def move(self, obstacles, player_rect):
        old_x, old_y = self.x, self.y
        
        if self.direction == "UP": self.y -= self.speed
        elif self.direction == "DOWN": self.y += self.speed
        elif self.direction == "LEFT": self.x -= self.speed
        elif self.direction == "RIGHT": self.x += self.speed
        
        self.rect.topleft = (self.x, self.y)
        
        collision = False
        if self.x < 0 or self.x > 760 or self.y < 0 or self.y > 560: collision = True
        
        if not collision and self.rect.colliderect(player_rect):
            collision = True

        if not collision:
            for obs in obstacles:
                if self.rect.colliderect(obs.rect):
                    collision = True
                    break
        
        if random.random() < 0.01 or collision:
            if collision:
                self.x, self.y = old_x, old_y
                self.rect.topleft = (self.x, self.y)
            self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
