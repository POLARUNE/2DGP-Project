from pico2d import *


class Jump_Ring:
    def __init__(self, x, y, color):
        if color == "yellow":
            self.image = load_image('yellow_jump_ring.png')
            self.jump_power = 800 # 공점 위로 3칸 상승
        elif color == "red":
            self.image = load_image('red_jump_ring.png')
            self.jump_power = 1000
        elif color == "pink":
            self.image = load_image('pink_jump_ring.png')
            self.jump_power = 600 # 공점 위로 2칸 상승
        elif color == "blue":
            self.image = load_image('blue_jump_ring.png')
            self.jump_power = 0
        self.x = x * 50 - 25  # 1부터 시작
        self.y = y * 50 - 25  # 1부터 시작
        self.size = 50

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
        # 충돌 영역 그리기
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        # 4개의 값을 리턴하는데, 사실은 1개의 튜플
        return self.x - self.size / 2, self.y - self.size / 2, self.x + self.size / 2, self.y + self.size / 2

    def handle_collision(self, group, other):
        pass