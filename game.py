import pygame
import sys
from managers.scene_manager import SceneManager
from scenes.scenes import MenuScene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Battle City Remake")
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = SceneManager()
        self.scene_manager.switch_scene(MenuScene())

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scene_manager.handle_events(event)

    def update(self):
        self.scene_manager.update()

    def render(self):
        self.scene_manager.render(self.screen)
        pygame.display.flip()