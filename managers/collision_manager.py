import pygame

class CollisionManager:
    def check_player_enemy(self, player, enemies):
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                return enemy
        return None

    def check_bullet_enemy(self, bullets, enemies):
        for bullet in bullets:
            if bullet.owner_type == "player":
                for enemy in enemies:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.take_damage(25)
                        bullet.active = False
                        return True
        return False

    def check_bullet_player(self, bullets, player):
        for bullet in bullets:
            if bullet.owner_type == "enemy":
                if bullet.rect.colliderect(player.rect):
                    player.take_damage(10)
                    bullet.active = False
                    return True
        return False

    def check_bullet_obstacle(self, bullets, obstacles):
        for bullet in bullets:
            for obstacle in obstacles:
                if bullet.rect.colliderect(obstacle.rect):
                    bullet.active = False
                    return True
        return False
        
    def check_rect_collision(self, rect1, rect2):
        return rect1.colliderect(rect2)