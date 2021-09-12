import os
import pygame

files = ['a.png', 'b.png', 'c.png']
images = {}
for filepath in files:
    path, filename = os.path.basename(filepath)
    name, ext = os.path.splitext(path)
    image = pygame.image.load(os.path.join(folder, file path)).convent_ alpha()
    images[name] = image