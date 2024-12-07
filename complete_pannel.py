from pico2d import *

class Pannel:
    def __init__(self):
        self.image = load_image('complete_level.png')
        self.x = 600  # 패널의 초기 x 좌표
        self.y = 1050  # 패널의 초기 y 좌표 (화면 위)
        self.target_y = 400  # 패널의 목표 y 좌표
        self.state = 'waiting'  # 'waiting' -> 'moving' 상태 전환
        self.time = 0  # 딜레이 타이머
        self.speed = 300  # 이동 속도 (픽셀/초)


    def draw(self):
        self.image.draw(self.x, self.y, 700, 500)

    def update(self):
        if self.state == 'waiting':
            self.time += 0.016  # 약 60 FPS 기준
            if self.time >= 1.0:  # 1초 대기 후 이동 시작
                self.state = 'moving'
        elif self.state == 'moving':
            # 패널을 목표 y 좌표로 이동
            if self.y > self.target_y:
                self.y -= self.speed * 0.016  # 속도와 시간에 따라 이동
                if self.y <= self.target_y:  # 목표에 도달했으면 고정
                    self.y = self.target_y
                    self.state = 'stopped'  # 이동 종료 상태
