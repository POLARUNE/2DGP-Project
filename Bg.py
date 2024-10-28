from pico2d import *
from settings import canvas_w, canvas_h

class Bg:
    def __init__(self):
        self.image = load_image('bg1.png')

    def draw(self):
        self.image.draw_to_origin(0, 0, canvas_w, canvas_h)

    def update(self):
        pass
