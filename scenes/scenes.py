import pygame
from abc import ABC, abstractmethod

class Scene(ABC):
    @abstractmethod
    def handle_events(self, event, scene_manager):
        pass

    @abstractmethod
    def update(self, scene_manager):
        pass

    @abstractmethod
    def render(self, screen):
        pass

class MenuScene(Scene):
    def handle_events(self, event, scene_manager):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                from utils.logger import Logger
                Logger.log("Starting game...")
                scene_manager.switch_scene(GameScene())

    def update(self, scene_manager):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 48)
        text = font.render("Battle City Remake", True, (255, 255, 255))
        screen.blit(text, (200, 200))
        
        font_small = pygame.font.SysFont("Arial", 24)
        hint = font_small.render("Press SPACE to Start", True, (200, 200, 200))
        screen.blit(hint, (300, 350))

class GameScene(Scene):
    def __init__(self):
        from entities.player import Player
        from entities.obstacles import Obstacle
        from managers.collision_manager import CollisionManager
        from utils.logger import Logger
        from managers.enemy_manager import EnemyManager
        from managers.bullet_manager import BulletManager
        
        self.player = Player(400, 500)
        self.obstacles = [
            Obstacle(100, 100), Obstacle(140, 100), Obstacle(180, 100),
            Obstacle(300, 300), Obstacle(340, 300), Obstacle(300, 340),
            Obstacle(600, 150), Obstacle(600, 190)
        ]
        self.collision_manager = CollisionManager()
        self.bullet_manager = BulletManager()
        self.enemy_manager = EnemyManager(self.obstacles)
        self.score = 0
        Logger.log("GameScene initialized")

    def handle_events(self, event, scene_manager):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene_manager.switch_scene(MenuScene())
            if event.key == pygame.K_SPACE:
                self.player.shoot(self.bullet_manager)

    def update(self, scene_manager):
        keys = pygame.key.get_pressed()
        direction = None
        if keys[pygame.K_UP] or keys[pygame.K_w]: direction = "UP"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]: direction = "DOWN"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]: direction = "LEFT"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]: direction = "RIGHT"
        
        if direction:
            old_x, old_y = self.player.x, self.player.y
            self.player.move(direction)
            
            collision = False
            if self.player.x < 0 or self.player.x > 760 or self.player.y < 0 or self.player.y > 560:
                 collision = True

            if not collision:
                for obstacle in self.obstacles:
                    if self.player.rect.colliderect(obstacle.rect):
                        collision = True
                        break
            
            if not collision:
                if self.collision_manager.check_player_enemy(self.player, self.enemy_manager.enemies):
                    collision = True

            if collision:
                self.player.x, self.player.y = old_x, old_y
                self.player.rect.topleft = (self.player.x, self.player.y)

        self.bullet_manager.update()
        self.enemy_manager.update(self.bullet_manager, self.player.rect)

        self.collision_manager.check_bullet_enemy(self.bullet_manager.bullets, self.enemy_manager.enemies)
        self.collision_manager.check_bullet_player(self.bullet_manager.bullets, self.player)
        self.collision_manager.check_bullet_obstacle(self.bullet_manager.bullets, self.obstacles)

        if self.enemy_manager.kills >= 10:
            from utils.logger import Logger
            Logger.log("Mission accomplished! Switching to WinScene.")
            scene_manager.switch_scene(WinScene())

        if self.player.health <= 0:
            from utils.logger import Logger
            Logger.log("Player destroyed! Switching to LoseScene.")
            scene_manager.switch_scene(LoseScene())

    def render(self, screen):
        screen.fill((30, 30, 30))
        self.player.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.bullet_manager.draw(screen)
        self.enemy_manager.draw(screen)
        
        font = pygame.font.SysFont("Arial", 20)
        hp_text = font.render(f"Health: {self.player.health}", True, (255, 255, 255))
        screen.blit(hp_text, (10, 10))
        
        kills_text = font.render(f"Kills: {self.enemy_manager.kills}/10", True, (255, 255, 255))
        screen.blit(kills_text, (10, 35))

class WinScene(Scene):
    def handle_events(self, event, scene_manager):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scene_manager.switch_scene(MenuScene())

    def update(self, scene_manager): pass
    def render(self, screen):
        screen.fill((0, 100, 0))
        font = pygame.font.SysFont("Arial", 48)
        text = font.render("YOU WIN!", True, (255, 255, 255))
        screen.blit(text, (300, 250))
        
        font_small = pygame.font.SysFont("Arial", 24)
        hint = font_small.render("Press SPACE to return to Menu", True, (200, 200, 200))
        screen.blit(hint, (270, 350))

class LoseScene(Scene):
    def handle_events(self, event, scene_manager):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scene_manager.switch_scene(MenuScene())

    def update(self, scene_manager): pass
    def render(self, screen):
        screen.fill((100, 0, 0))
        font = pygame.font.SysFont("Arial", 48)
        text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(text, (280, 250))
