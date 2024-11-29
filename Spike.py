from pico2d import *

class Spike:
    def __init__(self, x, y, direction):  # 방향 설정 ("up", "down", "left", "right")
        self.image = load_image('spike1.png')
        self.x = x
        self.y = y
        self.size = 50
        self.direction = direction  # 가시의 방향 설정

    def draw(self):
        if self.direction == "up":
            self.image.draw(self.x, self.y, self.size, self.size)
        elif self.direction == "down":
            self.image.composite_draw(3.141592, 'h', self.x, self.y, self.size, self.size)  # 아래쪽 방향 (수직 반전)
        elif self.direction == "left":
            self.image.composite_draw(3.141592/2, 'h', self.x, self.y, self.size, self.size)  # 왼쪽 방향 (90도 회전)
        elif self.direction == "right":
            self.image.composite_draw(-(3.141592/2), 'h', self.x, self.y, self.size, self.size)  # 오른쪽 방향 (-90도 회전)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        # 4개의 값을 리턴하는데, 사실은 1개의 튜플
        if self.direction == "up":
            return self.x - self.size / 3 + 5, self.y - self.size / 2, self.x + self.size / 3 - 5, self.y + self.size / 3 - 10
        elif self.direction == "down":
            return self.x - self.size / 3 + 5, self.y - self.size / 3 + 10, self.x + self.size / 3 - 5, self.y + self.size / 2
        elif self.direction == "right":
            return self.x - self.size / 2, self.y - self.size / 3 + 5, self.x + self.size / 3 - 10, self.y + self.size / 3 - 5
        elif self.direction == "left":
            return self.x - self.size / 3 + 10, self.y - self.size / 3 + 5, self.x + self.size / 2, self.y + self.size / 3 - 5

    def handle_collision(self, group, other):
        # print(f'spike: {self.x}, {self.y}')
        pass

