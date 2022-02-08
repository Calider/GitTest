import pygame
import sys
from bullet import Bullet
from ino import Ino

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #     vpravo
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False
        # vlevo
def update(bg_color, screen, gun, inos, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_inos(inos):
    inos.update()

def create_army(screen, inos):
    # sozdanie armii
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800-100-2 * ino_height) / ino_height)
    for row_nomber in range(number_ino_y - 5):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_nomber)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_nomber)
            inos.add(ino)