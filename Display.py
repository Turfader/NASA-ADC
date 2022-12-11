from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

path = "C:/Users/ashwa/Desktop/testBlenderProgram.blend"
app = Ursina()


ground = Entity(
    # model = 'testBlenderProgram'
    model = 'TheMoon',
    texture = 'lunar_regolith',
    collider = 'mesh',
    scale = (200, 1, 200)
)

class Sky(Entity):

    def __init__(self, **kwargs):
        from ursina.shaders import unlit_shader
        super().__init__(parent=render, name='sky', model='sky_dome', texture='space', scale=9900, shader=unlit_shader)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.world_position = camera.world_position


# Sky()

# player = FirstPersonController()

EditorCamera()

app.run()
