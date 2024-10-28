from pico2d import load_image


class Block:
    def __init__(self, x, y):
        self.image = load_image('block1.png')
        self.x = x
        self.y = y
        self.size = 50

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        pass
