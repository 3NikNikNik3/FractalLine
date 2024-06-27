from PIL import ImageDraw, Image
from vec_math import Vector
from engine import Fractal


class Drawer:
    def __init__(self, draw: ImageDraw):
        self.draw = draw

    def draw_line(self, color, s: Vector, e: Vector, r: int):
        self.draw.line((s.x, s.y, e.x, e.y), color, r)


def get_int(argv) -> int:
    if len(argv) < 6 or not argv[5].isdigit():
        return 0
    return int(argv[5])


def get_str(argv: list[str]) -> str:
    if len(argv) < 7:
        return 'result.png'
    return argv[6]


def main(frac: Fractal, size, arg: list[str]):
    move = get_int(arg)
    for i in range(move):
        print(f'{i + 1}/{move}')
        frac.next(0)

    print('save')
    file = Image.new("RGB", size, (255, 255, 255))
    draw = ImageDraw.Draw(file)
    draw_ = Drawer(draw)
    frac.draw(draw_, 1)
    file.save(get_str(arg))
    print('all!')
