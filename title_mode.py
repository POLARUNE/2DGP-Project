from pico2d import *
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import play_mode
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
            bgm.stop()
            #start sound 필요
            click_bgm = load_wav('title_to_play.wav')
            click_bgm.set_volume(32)
            click_bgm.play()
            delay(1.5)
            #game_framework.change_mode(stage_sel_mode)
            game_framework.change_mode(play_mode)


def draw():
    clear_canvas()
    image.draw(canvas_w / 2, canvas_h / 2)
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass