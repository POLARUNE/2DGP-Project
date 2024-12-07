from pico2d import *

import complete_mode
import game_framework
import game_world


class Coin:
    eat_coin_sound = None

    def __init__(self, x, y):
        self.image = load_image('coin.png')
        self.x = x * 50 - 25  # 블록 정중앙
        self.y = y * 50 - 25  # 블록 정중앙
        self.size = 40  # 가로 세로 길이
        self.alpha = 1.0  # 투명도 (1.0: 불투명, 0.0: 완전 투명)
        self.state = 'normal'  # 상태 ('normal', 'disappearing', 'removed')
        self.start_y = self.y  # 초기 y 좌표 저장
        self.time = 0  # 상태 변화에 사용할 타이머
        self.animation_duration = 2.0  # 애니메이션 총 지속 시간
        self.transition_delay = 1.0  # 타이틀 화면 이동 딜레이
        if not Coin.eat_coin_sound:
            Coin.eat_coin_sound = load_wav('eat_coin.wav')
            Coin.eat_coin_sound.set_volume(32)

    def draw(self):
        if self.state == 'normal' or self.state == 'disappearing':
            self.image.opacify(self.alpha)
            self.image.draw(self.x, self.y, self.size, self.size)
            # 충돌 영역은 'normal' 상태에서만 표시
            # if self.state == 'normal':
                #draw_rectangle(*self.get_bb())

    def update(self):
        if self.state == 'disappearing':
            self.time += 0.016  # 약 60 FPS 기준 (1/60초)
            progress = self.time / self.animation_duration  # 진행률 (0.0 ~ 1.0)

            if progress <= 1.0:
                # 포물선 이동
                self.y = self.start_y + 50 * (-4 * (progress - 0.5) ** 2 + 1)
                self.alpha = 1.0 - progress  # 투명도 감소
            else:
                # 애니메이션이 끝나면 상태를 'removed'로 변경
                self.state = 'removed'
                game_world.remove_object(self)
                #화면 이동
                game_framework.push_mode(complete_mode)

    def get_bb(self):
        return self.x - self.size / 2, self.y - self.size / 2, self.x + self.size / 2, self.y + self.size / 2

    def handle_collision(self, group, other):
        if group == 'cube:coin' and self.state == 'normal':
            self.state = 'disappearing'
            self.time = 0  # 타이머 초기화
            Coin.eat_coin_sound.play()  # 코인 먹는 소리 재생

            # 큐브 충돌 그룹 제거
            game_world.remove_collision_object(other)
