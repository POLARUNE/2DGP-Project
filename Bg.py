from pico2d import *
from settings import canvas_w, canvas_h

class Bg:
    def __init__(self):
        self.image = load_image('Stage1BG.png')
        self.bgm = load_music('TMM43 - Ultimate Destruction.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw_to_origin(0, 0, canvas_w, canvas_h)

    def update(self):
        pass
