from pico2d import *

class Checkpoint:
    def __init__(self, x, y):
        self.image = load_image('checkpointOFF.png')
        self.x = x * 50 - 25 # 1부터 시작
        self.y = y * 50 - 25 # 1부터 시작
        self.x_size = 25  # 가로 길이
        self.y_size = 40  # 세로 길이

    def draw(self):
        self.image.draw(self.x,self.y,self.x_size,self.y_size)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        # 4개의 값을 리턴하는데, 사실은 1개의 튜플
        return self.x - self.x_size / 2, self.y - self.y_size / 2, self.x + self.x_size / 2, self.y + self.y_size / 2

    def handle_collision(self, group, other):
        if group == 'cube:checkpoint':
            self.image = load_image('checkpointON.png')