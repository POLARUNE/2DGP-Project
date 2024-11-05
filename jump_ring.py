from pico2d import load_image


class Yellow_Jump_Ring:
    def __init__(self, x, y):
        self.image = load_image('yellow_jump_ring.png')
        self.x = x
        self.y = y
        self.size = 50
        self.jump_power = 10

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        pass

class Pink_Jump_Ring:
    def __init__(self, x, y):
        self.image = load_image('pink_jump_ring.png')
        self.x = x
        self.y = y
        self.size = 50
        self.jump_power = 5

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        pass

class Red_Jump_Ring:
    def __init__(self, x, y):
        self.image = load_image('red_jump_ring.png')
        self.x = x
        self.y = y
        self.size = 50
        self.jump_power = 15

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        pass


class Blue_Jump_Ring:
    def __init__(self, x, y):
        self.image = load_image('blue_jump_ring.png')
        self.x = x
        self.y = y
        self.size = 50
        self.jump_power = 0

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        pass