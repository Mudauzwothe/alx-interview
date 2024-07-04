#!/usr/bin/python3
"""The N queens solution finder module.
"""
import sys


solutions = []
"""List of possible solutions to N queens problem.
"""
n = 0
"""size of a chessboard.
"""
pos = None
"""List of possible positions on a chessboard.
"""


def get_input():
    """Retrieve and validate the program's argument.

    Returns:
        int: size of a chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be the number")
        sys.exit(1)
    if n < 4:
        print("N must be atleast 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Check if a positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): first queen's position.
        pos1 (list or tuple): second queen's position.

    Returns:
        bool: True if queens are in the attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Check if the group exists in the list of solutions.

    Args:
        group (list of integers): group of possible positions.

    Returns:
        bool: True when it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """Build the solution for the n queens problem.

    Args:
        row (int): current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Get the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution
