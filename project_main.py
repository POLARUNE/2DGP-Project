from pico2d import *

from Bg import Bg
from Block import Block
from Cube import Cube
from Spike import Spike
from settings import canvas_w, canvas_h


def handle_events():
    global running
    global cube
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                cube.left_pressed = True  # 왼쪽 키가 눌림
            elif event.key == SDLK_RIGHT:
                cube.right_pressed = True  # 오른쪽 키가 눌림
            elif event.key == SDLK_SPACE:
                cube.space_pressed = True  # 스페이스바 눌림
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                cube.left_pressed = False  # 왼쪽 키가 떼어짐
            elif event.key == SDLK_RIGHT:
                cube.right_pressed = False  # 오른쪽 키가 떼어짐
            elif event.key == SDLK_SPACE:
                cube.space_pressed = False  # 스페이스바가 떼어짐


def reset_world():
    global running
    global bg
    global cube
    global spikes
    global world

    running = True
    world = []

    bg = Bg()
    world.append(bg)

    cube = Cube()
    world.append(cube)

    spikes = [ Spike(300, 25, direction="up"),
        Spike(450, 25, direction="down"),
        Spike(600, 25, direction="right")]
    world += spikes

    blocks = [Block(500, 400)]
    world += blocks


def update_world():
    for o in world:
        if isinstance(o, Cube):
            o.update(spikes)  # Cube update에 spikes 전달
        else:
            o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas(canvas_w, canvas_h)
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()