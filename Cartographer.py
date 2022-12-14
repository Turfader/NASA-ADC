# This program is used to create the heightmap and slope map from the data

import csv
import pygame
from pygame import gfxdraw
import os

from PIL import Image, ImageDraw

rect_coord_path = "C:/Users/ashwa/Desktop/ADCLander/ProcessedData/ProcessedCoordinateData.csv"
rect_coord_path = rect_coord_path.replace("\\", "/")
with open(rect_coord_path, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    full_list = list(csv_reader)


def calculate_color(height):
    color = ((height+2872)*255/4830)
    return int(color), int(color), int(color)

def draw_points(isPygame):
    for i in range(1, len(full_list)):
        color = calculate_color(float(full_list[i][2]))
        x_pos = (i-1) % 1277
        y_pos = (i-1)//1277
        print(x_pos, y_pos)
        if isPygame:
            gfxdraw.pixel(screen, int(x_pos), int(y_pos), color)
        else:
            canvas.putpixel((int(x_pos), int(y_pos)), color)
        # note that there is a bit of data loss here.
        # Ideally, we'd make the final image have a size equal to the maximum span of the x and y data


def draw_slopes(isPygame):
    for i in range(1, len(full_list)):
        color = (255, 0, 0)
        if float(full_list[i][3]) < 20:
            color = (255, 255, 0)
        if float(full_list[i][3]) < 8:
            color = (0, 255, 0)
        x_pos = (i-1) % 1277
        y_pos = (i-1)//1277
        print(x_pos, y_pos)
        if isPygame:
            gfxdraw.pixel(screen, int(x_pos), int(y_pos), color)
        else:
            canvas.putpixel((int(x_pos), int(y_pos)), color)

###

canvas = Image.new('RGB', (1277, 1277), 'blue')
draw_points(False)
canvas.save('C:/Users/ashwa/Desktop/heightmap_test.jpg')
draw_slopes(False)
canvas.save('C:/Users/ashwa/Desktop/slopemap_test.jpg')

###

print("initiating pygame")
pygame.init()
screen = pygame.display.set_mode((1277, 1277))

done = False
clock = pygame.time.Clock()
while not done:

    done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                draw_points(True)
            elif event.key == pygame.K_s:
                draw_slopes(True)

    #screen.fill((0, 0, 255))

    #draw_points()
    #draw_slopes()

    pygame.display.flip()
    clock.tick(60)

