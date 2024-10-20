from pico2d import *
import random


# Game object class here
class Bg:
    def __init__(self):
        self.image = load_image('bg1.png')

    def draw(self):
        self.image.draw(400,300)

    def update(self):
        pass

class Cube:
    def __init__(self):
        self.image = load_image('cube.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global bg
    global cube
    global world

    running = True
    world = []

    bg = Bg()
    world.append(bg)

    cube = Cube()
    world.append(cube)


def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code
close_canvas()
