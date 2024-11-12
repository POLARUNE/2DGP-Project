from pico2d import *

import game_framework
import game_world
from bg import Bg
from block import Block
from Cube import Cube
from jump_pad import Yellow_Jump_Pad, Pink_Jump_Pad, Red_Jump_Pad, Blue_Jump_Pad
from jump_ring import Yellow_Jump_Ring, Pink_Jump_Ring, Red_Jump_Ring, Blue_Jump_Ring
from spike import Spike


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            cube.handle_event(event)


def init():
    global cube

    running = True

    bg = Bg()
    game_world.add_object(bg, 0)

    cube = Cube()
    game_world.add_object(cube, 2)

    block = Block(275,75)
    game_world.add_object(block, 1)

    spike = Spike(675,25,"up")
    game_world.add_object(spike, 1)

    yellow_jump_ring = Yellow_Jump_Ring(475, 75)
    game_world.add_object(yellow_jump_ring, 1)

    pink_jump_ring = Pink_Jump_Ring(675,75)
    game_world.add_object(pink_jump_ring, 1)

    red_jump_ring = Red_Jump_Ring(675, 175)
    game_world.add_object(red_jump_ring, 1)

    blue_jump_ring = Blue_Jump_Ring(475, 175)
    game_world.add_object(blue_jump_ring, 1)

    yellow_jump_pad = Yellow_Jump_Pad(875,5)
    game_world.add_object(yellow_jump_pad, 1)

    pink_jump_pad = Pink_Jump_Pad(925,5)
    game_world.add_object(pink_jump_pad, 1)

    red_jump_pad = Red_Jump_Pad(975,5)
    game_world.add_object(red_jump_pad, 1)

    blue_jump_pad = Blue_Jump_Pad(1025,5)
    game_world.add_object(blue_jump_pad, 1)


def update():
    game_world.update()
    # delay(0.1)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()


def pause(): pass
def resume(): pass