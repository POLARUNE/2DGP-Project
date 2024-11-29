from pico2d import *

import game_framework
import game_world
from bg import Bg
from block import Block
from Cube import Cube
from jump_pad import Jump_Pad
from jump_ring import Jump_Ring
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
    global cube, blocks, spikes, jump_pads
    global yellow_jump_rings, pink_jump_rings, red_jump_rings, blue_jump_rings

    bg = Bg()
    # game_world.add_object(bg, 0)

    # 맵 넓이 (24, 8), 큐브 점프 (3, 3)
    cube = Cube(2, 3)
    game_world.add_object(cube, 2)

    blocks = [ Block(2,2), Block(5, 2), Block(8, 3), Block(11, 5) ]
    game_world.add_objects(blocks, 1)

    spikes = [ Spike(3,2,"right"), Spike(4, 1, "up"), Spike(8, 2, "down"), Spike(4, 2, "left") ]
    game_world.add_objects(spikes, 1)

    jump_rings =[ Jump_Ring(9, 1, "yellow"), Jump_Ring(12,2,"pink"), Jump_Ring(15,3,"red"),Jump_Ring(18,4, "blue") ]
    game_world.add_objects(jump_rings, 1)

    jump_pads = [ Jump_Pad(14,1, "yellow"), Jump_Pad(16,1,"pink"), Jump_Pad(18,1,"red"), Jump_Pad(20,1,"blue") ]
    game_world.add_objects(jump_pads, 1)


    # 충돌 정보를 등록
    game_world.add_collision_pair('cube:block', cube, None)
    for block in blocks:
        game_world.add_collision_pair('cube:block', None, block)

    game_world.add_collision_pair('cube:spike', cube, None)
    for spike in spikes:
        game_world.add_collision_pair('cube:spike', None, spike)

    game_world.add_collision_pair('cube:ring', cube, None)
    for jump_ring in jump_rings:
        game_world.add_collision_pair('cube:ring', None, jump_ring)

    game_world.add_collision_pair('cube:pad', cube, None)
    for jump_pad in jump_pads:
        game_world.add_collision_pair('cube:pad', None, jump_pad)



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