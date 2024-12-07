from pico2d import *
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import game_world
import title_mode
from complete_pannel import Pannel


def init():
    global pannel, complete_sound, cube
    pannel = Pannel()
    #1초 후에 패널이 위에서 내려옴
    game_world.add_object(pannel, 3)
    complete_sound = load_wav('complete_sound.wav')
    complete_sound.set_volume(32)
    complete_sound.play()


def finish():
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(title_mode)

def update():
    game_world.update()

def draw():
    game_world.render()
    update_canvas()

def pause(): pass
def resume(): pass