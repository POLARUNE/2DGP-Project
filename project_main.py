from pico2d import *

import game_world
from bg import Bg
from block import Block
from cube import Cube
from settings import canvas_w, canvas_h
from spike import Spike


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            cube.handle_event(event)


def reset_world():
    global running
    global cube
    global bg
    global block

    running = True

    bg = Bg()
    # game_world.add_object(bg, 0)

    cube = Cube()
    game_world.add_object(cube, 1)

    block = Block(200,200)
    game_world.add_object(block, 1)

    spike = Spike(200,249,"up")
    game_world.add_object(spike, 1)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas(canvas_w, canvas_h)
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()