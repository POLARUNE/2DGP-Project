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

    def is_colliding_with_cube(self, cube):
        # 가시 방향에 따라 삼각형 꼭짓점 좌표 설정
        if self.direction == "up":
            p1 = (self.x - self.size / 2, self.y)             # 왼쪽 아래
            p2 = (self.x + self.size / 2, self.y)             # 오른쪽 아래
            p3 = (self.x, self.y + self.size)                 # 위쪽 정점
        elif self.direction == "down":
            p1 = (self.x - self.size / 2, self.y + self.size / 2) # 왼쪽 위
            p2 = (self.x + self.size / 2, self.y + self.size / 2) # 오른쪽 위
            p3 = (self.x, self.y - self.size / 2)             # 아래쪽 정점
        elif self.direction == "left":
            p1 = (self.x - self.size / 2, self.y - self.size / 2)   # 아래쪽
            p2 = (self.x - self.size / 2, self.y + self.size / 2)   # 위쪽
            p3 = (self.x + self.size, self.y)                 # 왼쪽 정점
        elif self.direction == "right":
            p1 = (self.x + self.size / 2, self.y - self.size / 2)             # 아래쪽
            p2 = (self.x + self.size / 2, self.y + self.size / 2)             # 위쪽
            p3 = (self.x - self.size, self.y)                 # 오른쪽 정점

        # 큐브의 중앙 좌표
        cx, cy = cube.x, cube.y

        # 삼각형 내부 충돌 체크 함수
        def point_in_triangle(px, py, p1, p2, p3):
            # 벡터를 이용한 면적 비교
            def sign(p1, p2, p3):
                return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

            d1 = sign((px, py), p1, p2)
            d2 = sign((px, py), p2, p3)
            d3 = sign((px, py), p3, p1)

            # 삼각형 내부에 점이 있는지 체크
            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
            return not (has_neg and has_pos)

        # 충돌 체크 결과 반환
        return point_in_triangle(cx, cy, p1, p2, p3)
