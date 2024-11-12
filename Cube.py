from pico2d import load_image

import game_framework
import game_world
from settings import canvas_w
from state_machine import *

#  큐브 속도 조절
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 45.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 점프 속도와 높이 조절
INIT_JUMP_POWER = 810
GRAVITY = 3200

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

    @staticmethod
    def draw(cube):
        cube.image.draw(cube.x, cube.y)


class Cube:
    def __init__(self):
        self.x, self.y = 100, 25
        self.dir = 1 # 큐브 방향
        self.image = load_image('cube.png')
        self.is_jumping = False
        self.jump_power = INIT_JUMP_POWER  # 점프 속도
        self.start_y = self.y  # 점프 시작 위치
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
            self.y += self.jump_power * game_framework.frame_time
            self.jump_power -= GRAVITY * game_framework.frame_time  # 중력 적용
            if self.y <= self.start_y:  # 지면에 도달했을 때
                self.y = self.start_y
                self.is_jumping = False
                self.jump_power = INIT_JUMP_POWER  # 점프 속도 초기화

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def jump(self):
        if not self.is_jumping:  # 점프 중이 아닐 때만 실행
            self.is_jumping = True
            print('JUMP')