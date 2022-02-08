import pygame

class Ino(pygame.sprite.Sprite):
    # klass odnogo prishelca

    def __init__(self, screen):
        # initializiryem i zadaem nachalnyu poziciu
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # vivod prisheltca na ikran
        self.screen.blit(self.image, self.rect)

    def update(self):
        # peremeschaet prishelcev
        self.y += 0.1
        self.rect.y = self.y