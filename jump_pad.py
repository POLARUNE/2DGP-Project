from pico2d import *


class Jump_Pad:
    def __init__(self, x, y, color):
        if color == "yellow":
            self.image = load_image('yellow_jump_pad.png')
            self.jump_power = 800 # 3칸 상승
        elif color == "red":
            self.image = load_image('red_jump_pad.png')
            self.jump_power = 1000 # 4칸 상승
        elif color == "pink":
            self.image = load_image('pink_jump_pad.png')
            self.jump_power = 600 # 2칸 상승
        elif color == "blue":
            self.image = load_image('blue_jump_pad.png')
            self.jump_power = 0

        self.x = x * 50 - 25  # 1부터 시작
        self.y = y * 50 - 45 # 1부터 시작


    def draw(self):
        self.image.draw(self.x, self.y, 50, 10)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        # 4개의 값을 리턴하는데, 사실은 1개의 튜플
        return self.x - 25, self.y - 5, self.x + 25, self.y + 5

    def handle_collision(self, group, other):
        pass