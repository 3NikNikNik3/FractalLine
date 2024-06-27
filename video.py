from vec_math import Vector
from engine import Fractal
import moviepy.editor as mpy
import numpy as np
import cv2


class Drawer:
    def __init__(self, w: int, h: int):
        self.arr = np.ones((h, w, 3), dtype=np.uint8) * 255

    def draw_line(self, color, s: Vector, e: Vector, r: int):
        cv2.line(self.arr, s.get_int_turtle(), e.get_int_turtle(), tuple(color), r)

    def get(self):
        return self.arr


class Setting:
    count_iter, sec, fps = 5, 0.5, 60
    frac: Fractal = None
    size = (0, 0)
    stop = True


def f(t):
    d = Drawer(Setting.size[0], Setting.size[1])
    if t % Setting.sec == 0:
        if Setting.stop:
            Setting.stop = False
        else:
            Setting.frac.next(Setting.sec)
    Setting.frac.draw(d, 1 / Setting.fps)
    return d.get()


def main(frac: Fractal, size: tuple[int, int], arg: list[str]):
    path = 'result.mp4'
    Setting.frac, Setting.size = frac, size
    if len(arg) > 5:
        path = arg[5]
    if len(arg) > 6 and arg[6].isdigit():
        Setting.count_iter = int(arg[6])
    if len(arg) > 7 and arg[7].replace('.', '', 1).isdigit():
        Setting.sec = float(arg[7])
    if len(arg) > 8 and arg[8].isdigit():
        Setting.fps = int(arg[8])

    clip = mpy.VideoClip(f, duration=Setting.sec * Setting.count_iter)
    clip.write_videofile(path, fps=Setting.fps)
