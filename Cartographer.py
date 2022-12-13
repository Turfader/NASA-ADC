# This program is used to create the heightmap and slope map from the data

import csv
import pygame
from pygame import gfxdraw
import os


rect_coord_path = os.getcwd() + "/Raw Data/Rectangular Coordinate Data.csv"
rect_coord_path = rect_coord_path.replace("\\", "/")
with open(rect_coord_path, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    full_list = list(csv_reader)


def calculate_color(height):
    color = ((height+2872)*255/4830)
    return color, color, color
# data is being lost by saving as an int ^^

# min x = -31 062
# max x = 20 047
# min y = -12 036
# max y = 39 073
### Testing below, please ignore ###


def draw_points():
    for i in range(1, len(full_list)):
        color = calculate_color(float(full_list[i][2]))
        x_pos = (i-1) % 1277
        y_pos = (i-1)//1277
        print(x_pos, y_pos)
        #screen.set_at((x_pos, y_pos), color)
        gfxdraw.pixel(screen, int(x_pos), int(y_pos), color)
        # note that there is a bit of data loss here.
        # Ideally, we'd make the final image have a size equal to the maximum span of the x and y data


def draw_slopes():
    for i in range(1, len(full_list)):
        color = (255, 0, 0)
        if float(full_list[i][3]) < 20:
            color = (255, 255, 0)
        if float(full_list[i][3]) < 8:
            color = (0, 255, 0)
        x_pos = (i-1) % 1277
        y_pos = (i-1)//1277
        print(x_pos, y_pos)
        #screen.set_at((x_pos, y_pos), color)
        gfxdraw.pixel(screen, int(x_pos), int(y_pos), color)


print("initiating pygame")
pygame.init()
screen = pygame.display.set_mode((1277, 1277))

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                draw_points()
            elif event.key == pygame.K_s:
                draw_slopes()

    #screen.fill((0, 0, 255))

    #draw_points()
    #draw_slopes()

    pygame.display.flip()
    clock.tick(60)
