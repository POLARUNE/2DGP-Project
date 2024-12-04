from pico2d import load_image, draw_rectangle
import time
import game_framework
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
    def __init__(self, x, y):
        # 큐브 x,y 좌표는 큐브 정중앙
        self.x = x * 50 - 25  # 1부터 시작
        self.y = y * 50 - 25  # 1부터 시작
        self.checkpoint_x, self.checkpoint_y = self.x, self.y # 죽으면 다시 부활할 위치
        self.dir = 1 # 큐브 방향
        self.image = load_image('cube.png') # 이미지 크기 50*50 고정
        self.is_jumping = False
        self.jump_power = INIT_JUMP_POWER  # 점프 가속도
        self.start_jump_y = self.y  #초기 점프 시작 위치
        self.on_block = False
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {space_down: Idle, right_down: Run, left_down: Run, right_up: Run, left_up: Run},
                Run: {space_down: Run, right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
            }
        )
        self.visible = True  # 큐브가 화면에 표시되는 상태
        self.respawn_timer = 0  # 부활 대기 시간 초기화
        self.is_space_pressed = False  # 스페이스바 눌림 상태

    def update(self):
        if not self.visible and time.time() >= self.respawn_timer:  # 부활 타이머가 끝난 경우
            self.visible = True
            self.x, self.y = self.checkpoint_x, self.checkpoint_y  # 부활 위치로 이동
            self.start_jump_y = self.checkpoint_y
            self.jump_power = INIT_JUMP_POWER
            self.is_jumping = False

        if self.visible:  # 큐브가 보일 때만 업데이트 진행
            self.state_machine.update()
            self.on_block = False
            if self.is_jumping:
                self.jump_power -= GRAVITY * game_framework.frame_time  # 중력 적용
                self.y += self.jump_power * game_framework.frame_time
                if self.y <= GROUND + 25: # 지면에 도달했을 때
                    self.y = GROUND + 25
                    self.start_jump_y = self.y
                    self.jump_power = INIT_JUMP_POWER
                    self.is_jumping = False
            elif not self.is_jumping and self.y > GROUND + 25 and not self.on_block: # 지면에 도달하지 않았을 때
                self.is_jumping = True
                self.jump_power = 0

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            self.is_space_pressed = True  # 스페이스바 눌림 상태
        elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
            self.is_space_pressed = False  # 스페이스바 해제 상태

        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        if self.visible:  # 큐브가 보일 때만 그리기
            self.state_machine.draw()
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
            # 큐브가 블록 아래를 때림
            if (    other.y - other.size / 2 + 25 > self.y + 25 > other.y - other.size / 2
                    and self.x + 25 > other.x - other.size / 2
                    and self.x - 25 < other.x + other.size / 2
            ):
                print('down')
                self.y = other.y - other.size / 2 - 25
                self.jump_power = 0

            # 큐브가 블록 위에 있음
            if (  other.y + other.size / 2 - 15 <= self.y - 25 < other.y + other.size / 2 + 15 # y 오차값 +-15
                    and self.x + 25 > other.x - other.size / 2
                    and self.x - 25 < other.x + other.size / 2
            ):
                # print('standing on block')
                self.y = other.y + other.size / 2 + 25
                self.on_block = True
                self.is_jumping = False
                self.start_jump_y = self.y
                self.jump_power = INIT_JUMP_POWER

            # 큐브가 블록 왼쪽에 부딪힘
            if (self.x + 25 > other.x - other.size / 2 > self.x + 10
                    and other.y - other.size / 2 - 24 < self.y < other.y + other.size / 2 + 24):
                # print('left collision')
                self.x = other.x - other.size / 2 - 25

                # 큐브가 블록 오른쪽에 부딪힘
            if (self.x - 25 < other.x + other.size / 2 < self.x - 10
                    and other.y - other.size / 2 - 24 < self.y < other.y + other.size / 2 + 24):
                # print('right collision')
                self.x = other.x + other.size / 2 + 25

        if group == 'cube:spike':
            if self.visible:  # 큐브가 보일 때만 충돌 처리
                self.visible = False  # 큐브를 화면에서 숨김
                self.respawn_timer = time.time() + 0.5  # 0.5초 후 부활

        if group == 'cube:pad':
            self.is_jumping = True
            self.jump_power = other.jump_power  # 점프 시작 가속도를 초기화

        if group == 'cube:ring':
            if self.is_space_pressed:  # 스페이스바가 눌렸는지 확인
                self.is_jumping = True
                self.jump_power = other.jump_power  # 점프 가속도를 초기화


