from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    try:
        with open(path) as level_map:
            layout = reader(level_map, delimiter=',')
            for row in layout:
                terrain_map.append(list(row))
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"Error reading {path}: {e}")
    return terrain_map
    
def import_folder(path):
    surface_list = []
    try:
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                try:
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(image_surf)
                except pygame.error as e:
                    print(f"Error loading image {full_path}: {e}")
    except Exception as e:
        print(f"Error accessing folder {path}: {e}")
    return surface_list
