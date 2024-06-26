from vec_math import Vector, get_s
import json


class Point(Vector):
    def __init__(self, x: float, y: float, end: Vector = None, time: float = 0):
        super().__init__(x, y)
        self.start = Vector(x, y)
        self.end = end
        self.time = self.max_time = time
        if time == 0 and not end is None:
            self.x, self.y = end.x, end.y

    def update(self, delta: float):
        if self.time != 0:
            if self.time - delta <= 0:
                self.x, self.y = self.end.x, self.end.y
                self.time = 0
            else:
                new = (self.end - self.start) * (delta / self.max_time)
                self.x += new.x
                self.y += new.y
                self.time -= delta


class Fractal:
    def __init__(self):
        self.iter = 0
        self.arr: list[Point] = []
        # 0 - ang, 1 - len (0-1)
        self.algorithm: list[tuple[float, float]] = []
        self.max_len = 0
        self.color = (0, 0, 0)
        self.r = 10
        self.auto_end = True

    def load(self, path: str, size_window) -> str:
        with open(path, 'r') as file:
            data = json.load(file)

        if 'start' in data and 'end' in data:
            if 'x' in data['start'] and 'y' in data['start']:
                self.arr.append(Point(data['start']['x'] * size_window[0], data['start']['y'] * size_window[1]))
            else:
                return 'Error: not correct start pos'
            if 'x' in data['end'] and 'y' in data['end']:
                self.arr.append(Point(data['end']['x'] * size_window[0], data['end']['y'] * size_window[1]))
            else:
                return 'Error: not correct end pos'
        else:
            return 'Error: not start or end pos'

        if 'alg' in data:
            for i in data['alg']:
                if 'ang' in i and 'len' in i:
                    self.algorithm.append((i['ang'], i['len']))
                    self.max_len += i['len']
                elif 'len' in i:
                    self.algorithm.append((0, i['len']))
                    self.max_len += i['len']
                else:
                    return 'Error: not correct alg (len / len+ang)'
        else:
            return 'Error: not alg'

        if 'color' in data and type(data['color']) == list and len(data['color']) == 3:
            self.color = tuple(data['color'])

        if 'r' in data and type(data['r']) == int:
            self.r = data['r']

        if 'auto_end' in data:
            self.auto_end = data['auto_end']

        if 'end_len' in data and type(data['end_len']) == float and self.auto_end:
            self.max_len += data['end_len']

        return 'ok'

    def next(self, time: float):
        self.iter += 1
        ans = []
        for i in range(len(self.arr) - 1):
            norm = self.arr[i + 1] - self.arr[i]
            size = norm.len()
            norm = norm.norm()
            pos = norm.copy()
            go = 0
            old = self.arr[i].copy()
            ans.append(Point(old.x, old.y))
            for j in self.algorithm:
                norm.rotate(j[0])
                old += norm * (size * j[1])
                #new = (self.arr[i + 1] - self.arr[i]) * get_s(self.arr[i], self.arr[i + 1], old) + self.arr[i]
                go += j[1]
                new = self.arr[i] + pos * (size * go / self.max_len)
                ans.append(Point(new.x, new.y, old.copy(), time))
        if self.auto_end:
            ans.append(Point(self.arr[-1].x, self.arr[-1].y))

        self.arr = ans

    def draw(self, screen, delta: float):
        self.arr[0].update(delta)
        for i in range(len(self.arr) - 1):
            self.arr[i + 1].update(delta)
            screen.draw_line(self.color, self.arr[i], self.arr[i + 1], self.r)
