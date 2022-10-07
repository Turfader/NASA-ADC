# This program is used to create the heightmap and slope map from the data

from PIL import Image
# import ImageDraw
import csv
import pygame
from pygame import gfxdraw

x_coords = []
y_coords = []
heights = []
slopes = []

with open("C:/Users/Owner/Documents/NASA project/Raw Data/Rectangular Coordinate Data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    full_list = list(csv_reader)

for i in range(1, len(full_list)):
    for j in range(4):
        if j == 0:
            x_coords.append(float(full_list[i][j]))
        elif j == 1:
            y_coords.append(float(full_list[i][j]))
        elif j == 2:
            heights.append(float(full_list[i][j]))
        else:
            slopes.append(float(full_list[i][j]))


def calculate_color(height):
    color = ((height+2872)*255/4830)
    return color, color, color


print(calculate_color(heights[0]))

# min x = -31 062
# max x = 20 047
# min y = -12 036
# max y = 39 073
### Testing below, please ignore ###


def draw_points():
    for i in range(len(slopes)):
        x_pos = (x_coords[i]/100) + 350
        y_pos = (y_coords[i]/100) + 250
        color = calculate_color(heights[i])
        gfxdraw.pixel(screen, int(x_pos), int(y_pos), color) # note that there is a bit of data loss here.
        # Ideally, we'd make the final image have a size equal to the maximum span of the x and y data


def draw_slopes():
    for i in range(len(slopes)):
        x_pos = (x_coords[i]/100) + 350
        y_pos = (y_coords[i]/100) + 250
        if slopes[i] >= 20:
            color = (255, 0, 0)
        elif slopes[i] >= 8:
            color = (255, 165, 0)
        else:
            color = (50, 150, 50)
        gfxdraw.pixel(screen, int(x_pos), int(y_pos), color)

print("initiating pygame")
pygame.init()
screen = pygame.display.set_mode((700, 700))
# "zero" = 350,350

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 255))

    # draw_points()
    # draw_slopes()
    
    pygame.display.flip()
    clock.tick(60)
