import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        # sozdaem pulu v pizicii pushki
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 252, 252, 252
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # peremeschenie puli vverh
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # risyem pyly na ekrane
        pygame.draw.rect(self.screen, self.color, self.rect)
