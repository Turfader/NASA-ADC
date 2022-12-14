from csv import reader as r
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

path = "C:/Users/ashwa/Desktop/testBlenderProgram.blend"
app = Ursina()


ground = Entity(
    # model = 'testBlenderProgram'
    model=Terrain(heightmap='htmap6'),
    texture='moon9',
    #collider='box',
    collider='mesh',
    scale=(1240, 150, 1240)
)

t_lat = Text(text='Latitude:', x=-.8, y=.45, scale=2)
t_lon = Text(text='Longitude:', x=-.8, y=.40, scale=2)
t_ht = Text(text='Height:', x=-.8, y=.35, scale=2)
t_slope = Text(text='Slope:', x=-.8, y=.30, scale=2)



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

player = FirstPersonController(position= (0, 1000, 0), speed=50, mouse_sensitivity=Vec2(25, 25))

def input(key):
    if key == 'r':
        player.set_position((0, 200, 0))
    if key == 's':
        ground.texture = 'slopemap_test'
    if key == 'h':
        ground.texture = 'color_heights_test'
    if key == 'm':
        ground.texture = 'moon9'
def update():
    x, y, z = player.position.x, player.position.y, player.position.z

    #for scale testing
    #print(f'x = {x}, y = {y}, z = {z}')

    t_lat.text = 'Latitude: ' + latitudes[int(x) + 620][int(abs(z-620))]
    t_lon.text = 'Longitude: ' + longitudes[int(x) + 620][int(abs(z-620))]
    t_ht.text = 'Height: ' + heights[int(x) + 620][int(abs(z-620))]
    t_slope.text = 'Slope: ' + slopes[int(x) + 620][int(abs(z-620))]

    if player.position.y < -50:
        player.set_position((0, 200, 0))


#EditorCamera()

app.run()

