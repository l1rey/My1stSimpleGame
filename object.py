from sprite import Sprite


class Ground(Sprite):
    def __init__(self, startx, starty):
        super().__init__("ground.png", startx, starty)