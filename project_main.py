from pico2d import open_canvas, close_canvas

import game_framework
from settings import canvas_w, canvas_h

import play_mode as start_mode


open_canvas(canvas_w, canvas_h)
game_framework.run(start_mode)
close_canvas()