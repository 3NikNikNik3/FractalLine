from PIL import ImageDraw, Image
from vec_math import Vector
from engine import Fractal

class Drawer:
    def __init__(self, draw: ImageDraw):
        self.draw = draw

    def draw_line(self, color, s: Vector, e: Vector, r: int):
        self.draw.line((s.x, s.y, e.x, e.y), color, r)


def main(frac: Fractal, size, move: float):
    move = int(move)
    for i in range(move):
        print(f'{i + 1}/{move}')
        frac.next(0)

    print('save')
    file = Image.new("RGB", size, (255, 255, 255))
    draw = ImageDraw.Draw(file)
    draw_ = Drawer(draw)
    frac.draw(draw_, 1)
    file.save('result.png')
    print('all!')
