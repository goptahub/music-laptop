import pygame
import sys
from brawls import Brawls
import laptop

laptop.init_laptop()

br = Brawls()
br.run()


pygame.quit()
sys.exit()