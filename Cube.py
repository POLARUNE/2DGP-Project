from pico2d import load_image, draw_rectangle

import game_framework
import game_world
from settings import canvas_w
from state_machine import *

#  큐브 속도 조절
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 47.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 점프 가속도와 높이 조절 // 가속 운동일 때는 오일러 공식 // v = at
INIT_JUMP_POWER = 800
GRAVITY = 3000
GROUND = 0 # 땅 Y 좌표

class Idle:
    @staticmethod
    def enter(cube, e):
        if start_event(e):
            cube.dir = 1
        elif right_down(e) or left_up(e):
            cube.dir = -1
        elif left_down(e) or right_up(e):
            cube.dir = 1


    @staticmethod
    def exit(cube, e):
        if space_down(e):
            cube.jump()

    @staticmethod
    def do(cube):
        pass

    @staticmethod
    def draw(cube):
        cube.image.draw(cube.x, cube.y)


class Run:
    @staticmethod
    def enter(cube, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            cube.dir = 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            cube.dir = -1

    @staticmethod
    def exit(cube, e):
        if space_down(e):
            cube.jump()

    @staticmethod
    def do(cube):
        cube.x += cube.dir * RUN_SPEED_PPS * game_framework.frame_time
        if cube.x > canvas_w + 50:
            cube.x = 0
        elif cube.x < -50:
            cube.x = canvas_w
        if cube.start_jump_y > GROUND + 25:
            cube.start_jump_y = GROUND
            cube.jump_power -= GRAVITY * game_framework.frame_time  # 중력 적용

    @staticmethod
    def draw(cube):
        cube.image.draw(cube.x, cube.y)


class Cube:
    def __init__(self):
        self.x, self.y = 100, 25 # 큐브 x,y 좌표는 큐브 정중앙
        self.dir = 1 # 큐브 방향
        self.image = load_image('cube.png') # 이미지 크기 50*50 고정
        self.is_jumping = False
        self.jump_power = INIT_JUMP_POWER  # 점프 가속도
        self.start_jump_y = self.y  #초기 점프 시작 위치
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {space_down: Idle, right_down: Run, left_down: Run, right_up: Run, left_up: Run},
                Run: {space_down: Run, right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
            }
        )

    def update(self):
        self.state_machine.update()
        # 점프 중일 때의 동작 처리
        if self.is_jumping:
            self.jump_power -= GRAVITY * game_framework.frame_time # 중력 적용
            self.y += self.jump_power * game_framework.frame_time
            if self.y <= GROUND + 25:  # 지면에 도달했을 때
                self.y = GROUND + 25
                self.jump_power = INIT_JUMP_POWER  # 점프 가속도 초기화
                self.is_jumping = False

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # 충돌 영역 그리기
        draw_rectangle(*self.get_bb())

    def jump(self):
        if not self.is_jumping:  # 점프 중이 아닐 때만 실행
            self.is_jumping = True
            print('JUMP')

    def get_bb(self):
        # 4개의 값을 리턴하는데, 사실은 1개의 튜플
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, group, other):
        if group == 'cube:block':
            # 큐브가 블럭 아래를 때림
           if other.y - other.size/2 + 25 > self.y + 25 > other.y - other.size/2 and (self.x + 25 > other.x - other.size/2 or self.x - 25 < other.x + other.size/2):
               print('down')
               self.y = other.y - other.size/2 - 25
               self.jump_power = 0

            # 큐브가 블럭 위에 있음
           elif other.y + other.size/2 - 5 < self.y - 25 < other.y + other.size/2 and (self.x + 25 > other.x - other.size/2 or self.x - 25 < other.x + other.size/2):
               print('up')
               self.y = other.y + other.size/2 + 25
               self.start_jump_y = other.y + other.size/2 + 25
               self.is_jumping = False
               self.jump_power = INIT_JUMP_POWER

            # 큐브가 블럭 왼쪽에 부딪힘

            # 큐브가 블럭 오른쪽에 부딪힘

        pass
