from entities.enemy import StraightEnemy, RandomEnemy

class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type, x, y):
        if enemy_type == "straight":
            return StraightEnemy(x, y)
        elif enemy_type == "random":
            return RandomEnemy(x, y)
        return None