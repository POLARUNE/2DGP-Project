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
    global cube, blocks, spikes
    global yellow_jump_rings, pink_jump_rings, red_jump_rings, blue_jump_rings
    global yellow_jump_pads, pink_jump_pads, red_jump_pads, blue_jump_pads

    bg = Bg()
    game_world.add_object(bg, 0)

    cube = Cube()
    game_world.add_object(cube, 2)

    blocks = [ Block(275,75), Block(475, 125), Block(725, 175), Block(925, 150) ]
    game_world.add_objects(blocks, 1)

    spikes = [ Spike(675,25,"right"), Spike(675, 75, "up"), Spike(675, 125, "down"), Spike(675, 175, "left") ]
    game_world.add_objects(spikes, 1)

    yellow_jump_rings =[ Yellow_Jump_Ring(825, 75) ]
    game_world.add_objects(yellow_jump_rings, 1)

    pink_jump_rings = [ Pink_Jump_Ring(825,75) ]
    game_world.add_objects(pink_jump_rings, 1)

    red_jump_rings = [ Red_Jump_Ring(825, 175) ]
    game_world.add_objects(red_jump_rings, 1)

    blue_jump_rings = [ Blue_Jump_Ring(475, 175) ]
    game_world.add_objects(blue_jump_rings, 1)

    yellow_jump_pads = [ Yellow_Jump_Pad(875,5) ]
    game_world.add_objects(yellow_jump_pads, 1)

    pink_jump_pads = [ Pink_Jump_Pad(925,5) ]
    game_world.add_objects(pink_jump_pads, 1)

    red_jump_pads = [ Red_Jump_Pad(975,5) ]
    game_world.add_objects(red_jump_pads, 1)

    blue_jump_pads = [ Blue_Jump_Pad(1025,5) ]
    game_world.add_objects(blue_jump_pads, 1)


    # 충돌 정보를 등록
    game_world.add_collision_pair('cube:block', cube, None)
    for block in blocks:
        game_world.add_collision_pair('cube:block', None, block)

    game_world.add_collision_pair('cube:spike', cube, None)
    for spike in spikes:
        game_world.add_collision_pair('cube:spike', None, spike)



def update():
    game_world.update()
    game_world.handle_collisions()
    # delay(0.1)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()


def pause(): pass
def resume(): pass