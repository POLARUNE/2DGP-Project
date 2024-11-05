from pico2d import load_image

import game_world
from settings import canvas_w
from state_machine import *


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
        if space_down(e) and cube.is_jumping == False:
            cube.jump()
        else:
            pass

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
        cube.x += cube.dir * 8
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
        self.jump_power = 14  # 점프 속도
        self.gravity = 1  # 중력
        # self.jump_height = 50  # 최대 점프 높이
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
            self.y += self.jump_power
            self.jump_power -= self.gravity  # 중력 적용
            if self.y <= self.start_y:  # 지면에 도달했을 때
                self.y = self.start_y
                self.is_jumping = False
                self.jump_power = 14  # 점프 속도 초기화

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def jump(self):
        if not self.is_jumping:  # 점프 중이 아닐 때만 실행
            self.is_jumping = True
            print('JUMP')