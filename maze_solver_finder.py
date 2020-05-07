#!/usr/bin/env python3

"""
Script:	maze_solver_finder.py
Date:	2020-04-24

Platform: MacOS/Window/Linux

Description:
Created as an attempt to bog down the process to test the speed differences in windows.
I found noticeable difference when running code in macOS, Windows and the Windows subsystem, I wanted to explore this
Performance was too good so needed to loop it to get some data

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Developer'

import argparse
import random
import time


def main():

    # Initialise counters
    counter_tried = 0
    counter_found = 0
    start_time = time.time()

    if options.size[0] > options.size[1]:
        options.size[0] = options.size[1]
    if options.seed[0] > options.seed[1]:
        options.seed[0] = options.seed[1]

    for size in range(options.size[0], options.size[1] + 1):
        print('Size:', size, ' ' * 40)
        start_end = int(size / 2)

        for seed in range(options.seed[0], options.seed[1] + 1):
            random.seed(seed)

            print('Trying seed : {}'.format(seed), end='\r')

            # Count the tries
            counter_tried += 1

            # If debugging stick to a fixed puzzle
            if options.debug:
                size = 10
                start_end = int(size / 2)

                maze = [
                    [2, 2, 2, 3, 3, 2, 2, 2, 2, 3],
                    [2, 2, 2, 3, 2, 1, 2, 2, 2, 3],
                    [2, 2, 2, 2, 0, 1, 2, 2, 2, 3],
                    [2, 2, 2, 2, 1, 2, 2, 2, 2, 3],
                    [2, 2, 2, 2, 2, 2, 2, 3, 4, 0],
                    [2, 2, 2, 2, 2, 2, 2, 3, 2, 3],
                    [2, 2, 2, 2, 2, 2, 2, 3, 2, 3],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
                    [2, 2, 1, 4, 4, 4, 4, 4, 4, 4],
                ]

            else:
                # Generate a maze
                maze = []
                for _ in range(size):
                    row = []
                    for _ in range(size):
                        row.append(random.randint(0, 4))
                    maze.append(row)

                # Make sure the start and the exit as feasible directions
                maze[0][start_end - 1] = random.choice([0, 2, 3, 4])
                maze[size - 1][start_end - 1] = 3

            # Get the paths
            path = []
            get_path(0, start_end - 1, maze, [], [], path)

            # If a solution was found
            if len(path) != 0:
                # Count found
                counter_found += 1

                # Print puzzle
                print('Puzzle:', seed, ' ' * 40)
                print('Size:', size)
                print(' ' * ((start_end * 2) - 3), '↓')
                for x in maze:
                    for y in x:
                        direction = '+'
                        direction = '↑' if y == 1 else direction
                        direction = '→' if y == 2 else direction
                        direction = '↓' if y == 3 else direction
                        direction = '←' if y == 4 else direction
                        print(direction, end=' ')
                    print()
                print(' ' * ((start_end * 2) - 3), '↓')

                # Print all the ways to go
                print('Solution(s):')
                print(' ' * ((start_end * 2) - 3), '↓')
                for x in range(size):
                    for y in range(size):
                        direction = ' '
                        for coordinate in path:
                            if coordinate[0] == x and coordinate[1] == y:
                                direction = '+' if coordinate[2] == 0 else direction
                                direction = '↑' if coordinate[2] == 1 else direction
                                direction = '→' if coordinate[2] == 2 else direction
                                direction = '↓' if coordinate[2] == 3 else direction
                                direction = '←' if coordinate[2] == 4 else direction
                        print(direction, end=' ')
                    print()
                print(' ' * ((start_end * 2) - 3), '↓')

                if options.debug:
                    exit()

    # Print options used
    print('Tested sizes from {} to {} and seeds {} to {}'.format(options.size[0], options.size[1],
                                                                 options.seed[0], options.seed[1]))

    # Print results of finds
    print('Tried {} and found {}'.format(counter_tried, counter_found))

    # Time runtime
    runtime = (time.time() - start_time)
    minutes, seconds = divmod(runtime, 60)
    hours, minutes = divmod(minutes, 60)
    print('Total runtime for all modules: {0:.0f}:{1:.0f}:{2:.3f}'.format(hours, minutes, seconds))


def get_path(x, y, maze, used_coordinates, path, found_path):
    """
    Get paths from beginning to end
    Recursive
    :param x: (int) Position to start or continue from in recursion
    :param y: (int) Position to start or continue from in recursion
    :param maze: (list(list)(int) Matrix puzzle
    :param used_coordinates: (list)(tuples) Coordinates that have already been traced so we avoid loops
    :param path: (list)(tuples) Temporary buffer to store the paths being tried
    :param found_path: (list)(tuples) Validated positions
    :return: (void)
    """
    end_position = len(maze)

    # If the position is out of range of the puzzle
    if x < 0 or y < 0 or x >= end_position or y >= end_position:
        return
    else:
        # If the coordinate was already used
        if (x, y) in used_coordinates:
            return
        else:
            # Track with coordinate
            used_coordinates.append((x, y))

            # Add to the path we are following
            path.append((x, y, maze[x][y]))

            # Follow the direction of the arrow
            direction = maze[x][y]
            if direction == 1 or direction == 0:
                get_path(x - 1, y, maze, used_coordinates.copy(), path.copy(), found_path)
            if direction == 2 or direction == 0:
                get_path(x, y + 1, maze, used_coordinates.copy(), path.copy(), found_path)
            if direction == 3 or direction == 0:
                get_path(x + 1, y, maze, used_coordinates.copy(), path.copy(), found_path)
            if direction == 4 or direction == 0:
                get_path(x, y - 1, maze, used_coordinates.copy(), path.copy(), found_path)

            if x == end_position - 1 and y == int(end_position / 2) - 1:
                found_path.extend(path)
                return


if __name__ == '__main__':
    def parser_formatter(format_class, **kwargs):
        """
        Use a raw parser to use line breaks, etc
        :param format_class: (class) formatting class
        :param kwargs: (dict) kwargs for class
        :return: (class) formatting class
        """
        try:
            return lambda prog: format_class(prog, **kwargs)
        except TypeError:
            return format_class


    parser = argparse.ArgumentParser(description='Create a batch of mazes, solve and display the solvable ones.',
                                     formatter_class=parser_formatter(
                                         argparse.RawTextHelpFormatter,
                                         indent_increment=4, max_help_position=12, width=160))

    parser.add_argument('-d', '--size-range', type=int,
                        action='store', dest='size', default=[5, 10], nargs=2,
                        help='Minimum and maximum values'
                             '\nDefault: %(default)s')

    parser.add_argument('-s', '--seed-range', type=int,
                        action='store', dest='seed', default=[0, 320000], nargs=2,
                        help='Seed of the random range'
                             '\nDefault: %(default)s')

    # Testing and debugging
    parser.add_argument('--debug',
                        action='store_true', dest='debug', default=False,
                        help='Debug the program'
                             '\nDefault: %(default)s')

    options = parser.parse_args()

    main()
