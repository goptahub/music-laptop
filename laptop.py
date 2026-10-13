import pygame

def init_laptop():
    pygame.init()
    screen_scales = (400, 300)
    screen = pygame.display.set_mode(screen_scales)
    pygame.display.set_caption("music_laptop")
    image = pygame.image.load("piano.png")
    scaled_image = pygame.transform.scale(image, screen_scales)
    screen.blit(scaled_image, (0, 0))
    pygame.display.flip()


