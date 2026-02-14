import random
import pygame
from factory.enemy_factory import EnemyFactory

class EnemyManager:
    def __init__(self, obstacles):
        self.enemies = []
        self.obstacles = obstacles
        self.spawn_timer = 0
        self.kills = 0

    def spawn_enemy(self):
        types = ["straight", "random"]
        etype = random.choice(types)
        
        max_attempts = 10
        for _ in range(max_attempts):
            ex = random.randint(0, 760)
            ey = random.randint(0, 200)
            new_rect = pygame.Rect(ex, ey, 40, 40)
            
            in_wall = False
            for obs in self.obstacles:
                if new_rect.colliderect(obs.rect):
                    in_wall = True
                    break
            
            if not in_wall:
                new_enemy = EnemyFactory.create_enemy(etype, ex, ey)
                self.enemies.append(new_enemy)
                return

    def update(self, bullet_manager, player_rect):
        self.spawn_timer += 1
        if self.spawn_timer >= 180 and len(self.enemies) < 5:
            self.spawn_enemy()
            self.spawn_timer = 0
            
        for enemy in self.enemies:
            enemy.move(self.obstacles, player_rect)
            enemy.shoot(bullet_manager)
            
        for enemy in self.enemies:
            if enemy.health <= 0:
                self.kills += 1
                
        self.enemies = [e for e in self.enemies if e.health > 0]

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
