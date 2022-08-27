import random

from animator import Speed
from animator import Animator, Animation


class Game(Animation):
    """ Simple implementation of Conway's Game of Life
    """
    Alive = chr(9608)  # chr(9632)
    Dying = chr(9617)
    Dead = ' '

    def __init__(self, y_size, x_size, seed=True):
        """ class constructor
        """
        self.x_size = x_size
        self.y_size = y_size
        self._grid = self._reset()
        self._grid_ = self._reset()
        if seed:
            self.add_random_seed()

    @property
    def grid(self):
        return self._grid

    def _reset(self):
        """ return grid of dead cells
        """
        return [[Game.Dead for x in range(self.x_size)] for y in range(self.y_size)]

    def add_random_seed(self):
        """ add random seed to grid
        """
        choices = [Game.Alive, Game.Dead]
        self._grid = [[random.choice(choices) for x in range(self.x_size)] for y in range(self.y_size)]

    def add_glider_seed(self):
        """ add glider seed
        """
        self._grid[0][1] = Game.Alive
        self._grid[1][2] = Game.Alive
        self._grid[2][0] = Game.Alive
        self._grid[2][1] = Game.Alive
        self._grid[2][2] = Game.Alive

    def add_blinker_seed(self):
        """ add blinker oscillator seed
        """
        self._grid[4][3] = Game.Alive
        self._grid[4][4] = Game.Alive
        self._grid[4][5] = Game.Alive

    def add_beacon_seed(self):
        """ add beacon oscillator seed
        """
        self._grid[1][1] = Game.Alive
        self._grid[1][2] = Game.Alive
        self._grid[2][1] = Game.Alive
        self._grid[3][4] = Game.Alive
        self._grid[4][3] = Game.Alive
        self._grid[4][4] = Game.Alive

    def get_neighbor_count(self, y, x):
        """ return count of alive neighbors
        """
        neighbor_count = 0
        for dy in range(y - 1, y + 2):
            for dx in range(x - 1, x + 2):
                xx = dx % self.x_size
                yy = dy % self.y_size
                if not (xx == x and yy == y) and self._grid[yy][xx] == Game.Alive:
                    # print(f'[{dy}][{dx}] is alive')
                    neighbor_count += 1
        return neighbor_count

    def apply_rules(self, neighbor_count, state):
        """ return new_state after applying rules to state with neighbor_count
        """
        new_state = state
        if state == Game.Alive:
            if neighbor_count < 2:
                # new_state = Game.Dead
                new_state = Game.Dying
            elif neighbor_count == 2 or neighbor_count == 3:
                new_state = Game.Alive
            else:
                # new_state = Game.Dead
                new_state = Game.Dying
        else:
            if neighbor_count == 3:
                new_state = Game.Alive
            else:
                new_state = Game.Dead
        return new_state

    def get_new_state(self, y, x):
        """ return new_state for cell at position y, x
        """
        neighbor_count = self.get_neighbor_count(y, x)
        current_state = self._grid[y][x]
        new_state = self.apply_rules(neighbor_count, current_state)
        # print(f'{y}.{x} : {current_state} - {neighbor_count} -> {new_state}')
        return new_state

    def cycle(self):
        """ cycle through grid - create new grid from existing grid by applying game rules
        """
        for y in range(self.y_size):
            for x in range(self.x_size):
                self._grid_[y][x] = self.get_new_state(y, x)
        self._grid = self._grid_
        self._grid_ = self._reset()

    def __str__(self):
        """ return string representation of Game instance
        """
        string = '   '
        for index in range(len(self._grid)):
            string += f'{str(index).zfill(2)} '
        string += '\n'
        for index, list1 in enumerate(self._grid):
            string += f'{str(index).zfill(2)}: ' + '  '.join(str(item) for item in list1)
            string += '\n'
        return string


def main():
    """ main program subroutine
    """
    Animator(animation=Game(40, 120))


if __name__ == '__main__':  # pragma: no cover
    main()
