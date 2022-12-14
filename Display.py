from csv import reader as r
import numpy as np
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

path = "C:/Users/ashwa/Desktop/testBlenderProgram.blend"
app = Ursina()

ground = Entity(
    # model = 'testBlenderProgram'
    model=Terrain(heightmap='htmap6'),
    texture='moon9',
    #collider='box',
    collider='box',
    scale=(1240, 150, 1240)
)

t_lat = Text(text='Latitude:', x=-.8, y=.45, scale=1.1)
t_lon = Text(text='Longitude:', x=-.8, y=.40, scale=1.1)
t_ht = Text(text='Height:', x=-.8, y=.35, scale=1.1)
t_slope = Text(text='Slope:', x=-.8, y=.30, scale=1.1)
t_azi = Text(text='Azimuth:', x=-.8, y=.25, scale=1.1)
t_elev = Text(text='Elevation:', x=-.8, y=.20, scale=1.1)

t_info = Text(text='R for Real or Reset, M for Moon, H for Heightmap, S for Slope Map', x=-.8, y=-.20, scale=1.1)



latitudes, longitudes, heights, slopes = [], [], [], []
with open('C:/Users/ashwa/Downloads/RegLat.csv') as csv_file:
    reads = r(csv_file)
    for row in reads:
        latitudes.append(row)
with open('C:/Users/ashwa/Downloads/RegLong.csv') as csv_file:
    reads = r(csv_file)
    for row in reads:
        longitudes.append(row)
with open('C:/Users/ashwa/Downloads/RegHeight.csv') as csv_file:
    reads = r(csv_file)
    for row in reads:
        heights.append(row)
with open('C:/Users/ashwa/Downloads/RegSlope.csv') as csv_file:
    reads = r(csv_file)
    for row in reads:
        slopes.append(row)

# Changes Sky Background to Black (0x000000)
class Sky(Entity):
    def __init__(self, **kwargs):
        from ursina.shaders import unlit_shader
        super().__init__(parent=render, name='sky', model='sky_dome', color='000000', scale=9900, shader=unlit_shader)
        for key, value in kwargs.items():
            setattr(self, key, value)
    def update(self):
        self.world_position = camera.world_position

Sky()
player = FirstPersonController(position= (200, 1000, 200), speed=50, mouse_sensitivity=Vec2(25, 25))

def input(key):
    if key == 'r':
        player.set_position((200, 200, 200))
    if key == 's':
        ground.texture = 'slopemap_test'
    if key == 'h':
        ground.texture = 'color_heights_test'
    if key == 'm':
        ground.texture = 'moon9'
    if key == 'r':
        ground.texture = 'moon7'


def update():
    x, y, z = player.position.x, player.position.y, player.position.z

    # Azimuth Angle and Elevation Calculation
    latE, longE = 29.5593, 95.0900
    latM, longM = float(latitudes[int(x) + 620][int(abs(z-620))]), float(longitudes[int(x) + 620][int(abs(z-620))])

    rad_earth = 6378000
    xE = rad_earth * cos(latE) * cos(longE)
    yE = rad_earth * cos(latE) * sin(longE)
    zE = rad_earth * sin(latE)

    xM = latM * math.cos(float(longM) * math.pi / 180)
    yM = latM * math.sin(float(longM) * math.pi / 180)
    zM = float(heights[int(x) + 620][int(abs(z-620))])

    vecRes = [xE-xM, yE-yM, zE-zM]

    range = sqrt(vecRes[0] ** 2 + vecRes[1] ** 2 + vecRes[2] ** 2)

    rz = vecRes[0] * cos(latM) * cos(longM) + vecRes[1] * cos(latM) * cos(longM) + vecRes[2] * sin(latM)

    a = sin(longE - longM) * cos(latE)
    b = (cos(latM) * sin(latE)) - (sin(latM) * cos(latE) * cos(longE - longM))

    # Elevation Value
    elev = np.arcsin(rz/range)

    # Azimuth Angle Value
    azimuth = np.arctan2(a, b)

    #for scale testing
    #print(f'x = {x}, y = {y}, z = {z}')

    # Updating Variables
    t_lat.text = 'Latitude: ' + latitudes[int(x) + 620][int(abs(z-620))]
    t_lon.text = 'Longitude: ' + longitudes[int(x) + 620][int(abs(z-620))]
    t_ht.text = 'Height: ' + heights[int(x) + 620][int(abs(z-620))]
    t_slope.text = 'Slope: ' + slopes[int(x) + 620][int(abs(z-620))]
    t_azi.text = 'Azimuth: ' + str(azimuth)
    t_elev.text = 'Elevation: ' + str(elev)

    if player.position.y < -50:
         player.set_position((200, 200, 200))


#EditorCamera()

app.run()

