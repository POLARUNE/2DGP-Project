from pico2d import *

class Spike:
    def __init__(self, x, y, direction="up"):  # 방향 설정 ("up", "down", "left", "right")
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

    def update(self):
        pass
