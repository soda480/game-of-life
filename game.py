import time
import random
from colorama import init as colorama_init
from colorama import Style
from colorama import Fore
from colorama import Back

from l2term import Lines

SIZE = 25
SLEEP = .2
bright_yellow = Style.BRIGHT + Fore.YELLOW + Back.BLACK
blue = Style.BRIGHT + Fore.BLUE + Back.BLACK


class Game(object):
    """ Simple implementation of Conway's Game of Life
    """

    Alive = chr(9608)  # chr(9632)
    Dead = ' '
    Dying = chr(9617)

    def __init__(self, size, seed=True):
        """ class constructor
        """
        self.size = size
        self.grid = self._reset()
        self._grid = self._reset()
        if seed:
            self.add_random_seed()

    def _reset(self):
        """ return grid of dead cells
        """
        return [[Game.Dead for x in range(self.size)] for y in range(self.size)]

    def add_random_seed(self):
        """ add random seed to grid
        """
        choices = [Game.Alive, Game.Dead]
        self.grid = [[random.choice(choices) for x in range(self.size)] for y in range(self.size)]

    def add_glider_seed(self):
        """ add glider seed
        """
        self.grid[0][1] = Game.Alive
        self.grid[1][2] = Game.Alive
        self.grid[2][0] = Game.Alive
        self.grid[2][1] = Game.Alive
        self.grid[2][2] = Game.Alive

    def add_blinker_seed(self):
        """ add blinker oscillator seed
        """
        self.grid[4][3] = Game.Alive
        self.grid[4][4] = Game.Alive
        self.grid[4][5] = Game.Alive

    def add_beacon_seed(self):
        """ add beacon oscillator seed
        """
        self.grid[1][1] = Game.Alive
        self.grid[1][2] = Game.Alive
        self.grid[2][1] = Game.Alive
        self.grid[3][4] = Game.Alive
        self.grid[4][3] = Game.Alive
        self.grid[4][4] = Game.Alive

    def get_neighbor_count(self, y, x):
        """ return count of alive neighbors
        """
        neighbor_count = 0
        for dy in range(y - 1, y + 2):
            for dx in range(x - 1, x + 2):
                xx = dx % self.size
                yy = dy % self.size
                if not (xx == x and yy == y) and self.grid[yy][xx] == Game.Alive:
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
        current_state = self.grid[y][x]
        new_state = self.apply_rules(neighbor_count, current_state)
        # print(f'{y}.{x} : {current_state} - {neighbor_count} -> {new_state}')
        return new_state

    def cycle(self):
        """ cycle through grid - create new grid from existing grid by applying game rules
        """
        for y in range(self.size):
            for x in range(self.size):
                self._grid[y][x] = self.get_new_state(y, x)
        self.grid = self._grid
        self._grid = self._reset()

    def __str__(self):
        """ return string representation of Game instance
        """
        string = '   '
        for index in range(len(self.grid)):
            string += f'{str(index).zfill(2)} '
        string += '\n'
        for index, list1 in enumerate(self.grid):
            string += f'{str(index).zfill(2)}: ' + '  '.join(str(item) for item in list1)
            string += '\n'
        return string


def display_header():
    """ print header columns of numbers to terminal
    """
    colorama_init()
    bright_yellow = Style.BRIGHT + Fore.YELLOW + Back.BLACK
    top = [str(index).zfill(2)[0] for index in range(SIZE)]
    bot = [str(index).zfill(2)[1] for index in range(SIZE)]
    print(f"{bright_yellow}    {''.join(top)}{Style.RESET_ALL}")
    print(f"{bright_yellow}    {''.join(bot)}{Style.RESET_ALL}")
    colons = ':' * SIZE
    print(f"    {colons}")


def main():
    """ main program subroutine
    """
    display_header()
    try:
        # initialize the game
        game = Game(SIZE)
        # display grid on our terminal using the lines class
        with Lines(game.grid) as lines:
            while True:
                # run through one game cycle
                game.cycle()
                # update lines in our terminal
                for index in range(SIZE):
                    lines[index] = game.grid[index]
                # sleep a bit before the next cycle
                time.sleep(SLEEP)

    except KeyboardInterrupt:
        print('user ended game')


if __name__ == '__main__':  # pragma: no cover
    main()
