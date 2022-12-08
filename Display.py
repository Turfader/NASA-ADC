from ursina import *

path = "C:/Users/ashwa/Desktop/testBlenderProgram.blend"
app = Ursina()

load_blender_scene(name='test', path=path, load=True, reload=False, skip_hidden=True, models_only=False)


app.run()
