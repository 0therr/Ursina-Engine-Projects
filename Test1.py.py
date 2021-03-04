from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController  
app = Ursina()
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)
block_pick = 1
window.fps_counter.enabled = False
window.exit_button.visible = False
def update():
    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    for entity in spheres:
        entity.rotation_y = entity.rotation_y + time.dt * 100
spheres = []
sphere = Entity(model='sphere', color=color.red, rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(5.25,2,5.25))
sphere1 = Entity(model='sphere', color=color.orange, rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(6.25,2,6.25))
sphere2 = Entity(model='sphere', color=rgb(255, 215, 0), rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(7.25,2,7.25))
sphere3 = Entity(model='sphere', color=color.yellow, rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(8.25,2,8.25))
sphere4 = Entity(model='sphere', color=color.green, rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(9.25,2,9.25))
sphere5 = Entity(model='sphere', color=color.blue, rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(9.25,2,9.25))
sphere6 = Entity(model='sphere', color=rgb(128, 0, 128), rotation=(45, 45, 0),
    texture="sphere.jpg",size='50',collider='sphere',position=(10.25,2,10.25))
Entity(model='cube',position=(2,.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(2,1.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(1,.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(1,1.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(0,.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(0,1.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(2,1.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(2,2.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(1,1.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(1,2.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(0,1.75,2),color=color.gray,texture='brick',collider='cube')
Entity(model='cube',position=(0,2.75,2),color=color.gray,texture='brick',collider='cube')
spheres.extend((sphere,sphere1,sphere2,sphere3,sphere4,sphere5,sphere6)) # list.extend()
class Voxel(Button):  
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture='brick',
            color=color.white,
            scale=0.5)
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=250,
            double_sided=True)
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self): 
        self.position = Vec2(0.4, -0.6)
for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x, 0, z))      
player = FirstPersonController()
sky = Sky()
hand = Hand()
window.title = 'Title'
window.borderless = False
window.fps_counter.enabled = True
app.run()  