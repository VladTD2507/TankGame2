import pygame
from entities.bullet import Bullet

class BulletManager:
    def __init__(self):
        self.bullets = []

    def add_bullet(self, x, y, direction, owner_type):
        new_bullet = Bullet(x, y, direction, owner_type)
        self.bullets.append(new_bullet)

    def update(self):
        for bullet in self.bullets:
            bullet.update()
        
        self.bullets = [b for b in self.bullets if b.active and 0 <= b.x <= 800 and 0 <= b.y <= 600]

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)