from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import play_mode
from settings import canvas_w, canvas_h


def init():
    global image
    image = load_image('title.png') # 게임 시작 초기 화면에 로고만 붙이기


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
            # 이 사이에 로고만 올라가게?
            game_framework.change_mode(play_mode)


def draw():
    clear_canvas()
    image.draw(canvas_w / 2, canvas_h / 2)
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass