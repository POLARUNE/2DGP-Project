from pico2d import *
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import play_mode
import stage_sel_mode
import title_mode
from settings import canvas_w, canvas_h


def init():
    global image, bgm, clickbgm
    image = load_image('title.png')
    click_bgm = None
    bgm = load_music('titlebgm.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()


def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image.draw(canvas_w / 2, canvas_h / 2)
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass