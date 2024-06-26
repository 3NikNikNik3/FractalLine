import pygame
from vec_math import Vector
from engine import Fractal


class Drawer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def draw_line(self, color, s: Vector, e: Vector, r: int):
        pygame.draw.line(self.screen, color, (s.x, s.y), (e.x, e.y), r)


def main(frac: Fractal, size, move: float):
    pygame.init()

    screen = pygame.display.set_mode(size)
    tick = pygame.time.Clock()

    dr = Drawer(screen)

    old_delta = 0

    time_stop = 0

    play = True
    while play:
        tick.tick(60)
        pygame.display.set_caption(f'{frac.iter} iter; {len(frac.arr)} point; {tick.get_fps()} fps')
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                play = False
            elif i.type == pygame.KEYDOWN:
                if (i.key == pygame.K_RIGHT or i.key == pygame.K_d) and time_stop == 0:
                    frac.next(move)
                    time_stop = move
                elif i.key == pygame.K_ESCAPE:
                    play = False

        screen.fill((255, 255, 255))
        t = pygame.time.get_ticks()
        frac.draw(dr, (t - old_delta) / 1000)
        if time_stop != 0:
            time_stop -= (t - old_delta) / 1000
            if time_stop < 0:
                time_stop = 0
        old_delta = t
        pygame.display.flip()

    pygame.quit()
