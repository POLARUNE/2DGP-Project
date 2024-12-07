from pico2d import load_image, draw_rectangle


class Block:
    def __init__(self, x, y):
        self.image = load_image('block1.png')
        # x와 y 좌표는 블록 정중앙
        self.x = x * 50 - 25 # 1부터 시작
        self.y = y * 50 - 25 # 1부터 시작
        self.size = 50  # 가로 세로 길이

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
        # 충돌 영역 그리기
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        # 4개의 값을 리턴하는데, 사실은 1개의 튜플
        return self.x - self.size / 2, self.y - self.size / 2, self.x + self.size / 2, self.y + self.size / 2

    def handle_collision(self, group, other):
        # print(f'block: {self.x}, {self.y}')
        pass