from pico2d import *

import game_framework
import title_mode
from settings import canvas_w, canvas_h


def init():
    global image
    image = load_image('title.png') # 게임 시작 초기 화면에 로고만 붙이기

def finish():
    global image
    del image

def handle_events():
    global stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        # 스테이지를 누르면 play_mode로


def draw():
    clear_canvas()
    image.draw(canvas_w / 2, canvas_h / 2)
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass