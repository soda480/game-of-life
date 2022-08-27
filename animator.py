from time import sleep
from enum import Enum
from l2term import Lines


class Speed(Enum):
    NORMAL = .07
    FAST = .03
    SLOW = .11


class Animator(object):

    def __init__(self, animation=None, speed=Speed.NORMAL):
        """ initialize Animator
        """
        if not isinstance(speed, Speed):
            raise ValueError("speed must be an instance of Speed Enum")
        self.speed = speed
        self.animation = animation
        self._start()

    def _start(self):
        """ start animating the animation
        """
        with Lines(self.animation.grid, show_index=False) as lines:
            try:
                while True:
                    self.animation.cycle()
                    for index in range(len(self.animation.grid)):
                        lines[index] = self.animation.grid[index]
                    sleep(self.speed.value)
            except KeyboardInterrupt:
                pass
