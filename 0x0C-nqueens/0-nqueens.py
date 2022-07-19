#!/usr/bin/python3
import sys


def start(en):
    solutions = []
    for row in range(0, en):
        solve(en, 0, row, solutions)
    for solution in solutions:
        print(solution)


def solve(size, col, row, sol_set, sol=[]):
    e = evaluate(col, row, sol)
    if e is False:
        return
    s = sol.copy()
    s.append([col, row])
    if col == size - 1:
        accept(sol_set, s)
    for new_row in range(0, size):
        solve(size, col + 1, new_row, sol_set, s)


def evaluate(col, row, sol):
    for queen in sol:
        if queen[0] == col or queen[1] == row:
            return False
        if queen[0] - queen[1] == col - row:
            return False
        if queen[0] + queen[1] == col + row:
            return False
    return True


def accept(sol_set, sol):
    sol_set.append(sol)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
else:
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
        start(n)
    except Exception:
        print("N must be a number")
        exit(1)
