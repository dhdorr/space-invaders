import sys
import pygame
from pygame.sprite import Sprite

#maybe spritesheet implementation
from spritesheet import SpriteSheet

"""gameClock = pygame.time.Clock()
# used for frames
def clock():
    current_time = pygame.time.get_ticks()
    return current_time

def tick(fps):
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    gameClock.tick(fps)
    return gameClock.get_fps()"""

class Ship(pygame.sprite.Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #FROM Sprite sheet example arrays that store location of images
        self.flying_frames = []

        sprite_sheet = SpriteSheet("images/SpriteSheet.png")
        #Load all the right facing images into a list
        for num_pics1 in range(6):
            image = sprite_sheet.get_image(0, 128, 32, 32)
            self.flying_frames.append(image)
        for num_pics2 in range(6):
            image = sprite_sheet.get_image(32, 128, 32, 32)
            self.flying_frames.append(image)
        for num_pics3 in range(6):
            image = sprite_sheet.get_image(0, 160, 32, 32)
            self.flying_frames.append(image)
        for num_pics4 in range(6):
            image = sprite_sheet.get_image(32, 160, 32, 32)
            self.flying_frames.append(image)

        self.image = self.flying_frames[0]

        # Load the ship image, and get its rect. *EDITED SELF.IMAGE*

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False

        self.index = 0
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

        self.index += 1

        if self.index >= len(self.flying_frames):
            self.index = 0

        self.image = self.flying_frames[self.index]

        """nextFrame = clock()
        frame=0
        if clock() > nextFrame:
            frame = (frame+1)%4
            nextFrame += 40

        self.image = self.flying_frames[frame]

        tick(60)"""

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
