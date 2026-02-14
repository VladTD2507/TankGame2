class SceneManager:
    def __init__(self):
        self.current_scene = None

    def switch_scene(self, scene):
        self.current_scene = scene

    def handle_events(self, event):
        if self.current_scene:
            self.current_scene.handle_events(event, self)

    def update(self):
        if self.current_scene:
            self.current_scene.update(self)

    def render(self, screen):
        if self.current_scene:
            self.current_scene.render(screen)
