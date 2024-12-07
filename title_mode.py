from pico2d import *
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import play_mode
import stage_sel_mode
from settings import canvas_w, canvas_h


def init():
    global image
    image = load_image('title_bg.png') # 게임 시작 초기 화면에 로고만 붙이기


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
            #start sound 필요
            delay(0.5)
            game_framework.change_mode(stage_sel_mode)


def draw():
    clear_canvas()
    image.draw(canvas_w / 2, canvas_h / 2)
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass