import pygame

class UIElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pass

class Label(UIElement):
    def __init__(self, x, y, text, font_size=24, color=(255, 255, 255)):
        super().__init__(x, y)
        self.text = text
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = color
        self.update_surface()

    def update_surface(self):
        self.surface = self.font.render(self.text, True, self.color)

    def set_text(self, text):
        self.text = f"{text}"
        self.update_surface()

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

class Button(UIElement):
    def __init__(self, x, y, width, height, text, callback, font_size=24, 
                 bg_color=(100, 100, 100), hover_color=(150, 150, 150), text_color=(255, 255, 255)):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", font_size)
        self.update_text_surface()

    def update_text_surface(self):
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.bg_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        screen.blit(self.text_surface, self.text_rect)

class Observer:
    def __init__(self, update_func):
        self.update_func = update_func

    def notify(self, value):
        self.update_func(value)
