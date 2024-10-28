from pico2d import load_image

from settings import canvas_w


class Cube:
    def __init__(self):
        self.image = load_image('cube.png')
        self.initial_x = 100  # 초기 위치 x
        self.initial_y = 25  # 초기 위치 y
        self.x = self.initial_x
        self.y = self.initial_y
        self.dx = 0  # 좌우 이동 속도
        self.dy = 0  # 점프 속도 (y축)
        self.scale = 50 # 큐브 가로 및 세로 크기
        self.is_jumping = False  # 점프 상태
        self.gravity = -0.5  # 중력
        self.jump_power = 10  # 점프할 때의 초기 속도
        self.ground_level = 25  # 바닥 y 좌표
        self.left_pressed = False  # 왼쪽 키가 눌렸는지
        self.right_pressed = False  # 오른쪽 키가 눌렸는지
        self.space_pressed = False  # 스페이스 키가 눌렸는지

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, spikes):
        # 좌우 이동 처리
        if self.left_pressed:
            self.dx = -5  # 왼쪽으로 이동
        elif self.right_pressed:
            self.dx = 5  # 오른쪽으로 이동
        else:
            self.dx = 0  # 양쪽 키를 모두 떼면 멈춤

        # 좌우 경계 체크 (큐브가 화면 밖으로 나가지 않도록)
        self.x += self.dx
        if self.x < self.scale // 2:
            self.x = self.scale // 2  # 왼쪽 경계
        elif self.x > canvas_w - self.scale // 2:
            self.x = canvas_w - self.scale // 2  # 오른쪽 경계

        # 점프 중일 때 중력 처리
        if self.is_jumping:
            self.dy += self.gravity  # 중력 작용
            self.y += self.dy  # y 좌표 업데이트

            # 바닥에 도착하면 점프 종료
            if self.y <= self.ground_level:
                self.y = self.ground_level
                self.is_jumping = False
                self.dy = 0  # 점프 속도를 초기화

        # 스페이스 키가 계속 눌려있으면 점프 상태를 계속 유지
        if self.space_pressed and not self.is_jumping:
            self.jump()

        # 가시 충돌 체크
        for spike in spikes:
            if spike.is_colliding_with_cube(self):
                self.reset_position()  # 충돌 시 큐브를 초기 위치로 리셋

    def jump(self):
        if not self.is_jumping:  # 점프 중이 아닐 때만 점프 가능
            self.is_jumping = True
            self.dy = self.jump_power  # 점프할 때의 초기 속도를 설정

    def reset_position(self):
        # 초기 위치로 돌아가기
        self.x = self.initial_x
        self.y = self.initial_y
        self.dx = 0
        self.dy = 0
        self.is_jumping = False
