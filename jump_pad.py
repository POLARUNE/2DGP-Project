from pico2d import load_image


class Yellow_Jump_Pad:
    def __init__(self, x, y):
        self.image = load_image('yellow_jump_pad.png')
        self.x = x
        self.y = y
        self.jump_power = 15

    def draw(self):
        self.image.draw(self.x, self.y, 50, 10)

    def update(self):
        pass

class Pink_Jump_Pad:
    def __init__(self, x, y):
        self.image = load_image('pink_jump_pad.png')
        self.x = x
        self.y = y
        self.jump_power = 10

    def draw(self):
        self.image.draw(self.x, self.y, 50, 10)

    def update(self):
        pass

class Red_Jump_Pad:
    def __init__(self, x, y):
        self.image = load_image('red_jump_pad.png')
        self.x = x
        self.y = y
        self.jump_power = 20

    def draw(self):
        self.image.draw(self.x, self.y, 50, 10)

    def update(self):
        pass

class Blue_Jump_Pad:
    def __init__(self, x, y):
        self.image = load_image('blue_jump_pad.png')
        self.x = x
        self.y = y
        self.jump_power = 0

    def draw(self):
        self.image.draw(self.x, self.y, 50, 10)

    def update(self):
        pass