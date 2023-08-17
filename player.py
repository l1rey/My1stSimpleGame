import pygame.key

from sprite import Sprite


class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("VergilStand.png", startx, starty)

        self.stand_image = self.image
        self.walk_cycle = [pygame.image.load(f"VergilWalking{i:0>2}.png") for i in range(1, 9)]
        self.animation_index = 0
        self.facing_left = False

        self.speed = 5
        self.jump = 10
        self.gravity = 1
        self.vertical_speed = 0

    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def update(self, ground) -> None:
        horizontal_speed = 0
        onground = pygame.sprite.spritecollideany(self, ground)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.facing_left = True
            self.walk_animation()
            horizontal_speed = -self.speed
        elif key[pygame.K_RIGHT]:
            self.facing_left = False
            self.walk_animation()
            horizontal_speed = self.speed
        else:
            self.image = self.stand_image
        if key[pygame.K_UP] and onground:
            self.vertical_speed = -self.jump
        if self.vertical_speed < 10 and not onground:
            self.vertical_speed += self.gravity
        if self.vertical_speed > 0 and onground:
            self.vertical_speed = 0

        self.move(horizontal_speed, self.vertical_speed)

    def move(self, x, y):
        self.rect.move_ip([x, y])