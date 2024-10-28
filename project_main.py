from pico2d import *
import random


class Bg:
    def __init__(self):
        self.image = load_image('bg1.png')

    def draw(self):
        self.image.draw_to_origin(0, 0, canvas_w, canvas_h)

    def update(self):
        pass

class Spike:
    def __init__(self, x, y):  # x, y 좌표를 매개변수로 받아 초기화
        self.image = load_image('spike1.png')
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(0,150,100,100,self.x, self.y,50,50)

    def update(self):
        pass

class Cube:
    def __init__(self):
        self.image = load_image('cube.png')
        self.x = 100
        self.y = 25
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

    def update(self):
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

    def jump(self):
        if not self.is_jumping:  # 점프 중이 아닐 때만 점프 가능
            self.is_jumping = True
            self.dy = self.jump_power  # 점프할 때의 초기 속도를 설정


def handle_events():
    global running
    global cube
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                cube.left_pressed = True  # 왼쪽 키가 눌림
            elif event.key == SDLK_RIGHT:
                cube.right_pressed = True  # 오른쪽 키가 눌림
            elif event.key == SDLK_SPACE:
                cube.space_pressed = True  # 스페이스바 눌림
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                cube.left_pressed = False  # 왼쪽 키가 떼어짐
            elif event.key == SDLK_RIGHT:
                cube.right_pressed = False  # 오른쪽 키가 떼어짐
            elif event.key == SDLK_SPACE:
                cube.space_pressed = False  # 스페이스바가 떼어짐


def reset_world():
    global running
    global bg
    global cube
    global spikes
    global world

    running = True
    world = []

    bg = Bg()
    world.append(bg)

    cube = Cube()
    world.append(cube)

    spikes = [Spike(300, 25), Spike(450, 25), Spike(600, 25)]
    world += spikes


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

canvas_w = 1200
canvas_h = 800
open_canvas(canvas_w, canvas_h)
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()