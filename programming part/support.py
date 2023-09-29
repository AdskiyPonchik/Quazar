import pygame
def player_importer(path):
    surface_list = []
    lst = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
    for data in lst:
        full_path = path+'/'+data
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)
    return surface_list

def platform_importer(path):
    surface_list = []
    lst = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png','11.png']
    for data in lst:
        full_path = path + '/' + data
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)
    return surface_list

def coin_importer(path):
    surface_list = []
    lst = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']
    for data in lst:
        full_path = path +'/'+data
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)
    return surface_list
