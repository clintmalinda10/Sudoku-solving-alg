from Depth-First import solve_dfs
from Depth-First import input
from Backtracking import solve_bt

board1 = input('Puzzle.txt',9)
board2 = input('test case 2.txt',9)
board3 = input('test case 3.txt',9)
board4 = input('test case 4.txt',9)
board5 = input('test case 5.txt',9)
print("First test")
solve_dfs(board1)
solve_bt(board1)

print("Second test")
solve_dfs(board2)
solve_bt(board2)

print("Third test")
solve_dfs(board3)
solve_bt(board3)

print("Fourth test")
solve_dfs(board4)
solve_bt(board4)

print("Fifth test")
solve_dfs(board4)
solve_bt(board4)