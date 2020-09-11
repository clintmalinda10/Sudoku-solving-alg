import time

class Problem(object):

    def __init__(self, initial):
        self.initial = initial
        self.type = len(initial) # Defines board type, either 6x6 or 9x9
        self.height = int(self.type/3) # Defines height of quadrant (2 for 6x6, 3 for 9x9)

    def goal_test(self, state):
        total = sum(range(1, self.type+1))

        
        for row in range(self.type):
            if (len(state[row]) != self.type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(self.type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        for column in range(0,self.type,3):
            for row in range(0,self.type,self.height):

                block_total = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
                    return False

        return True

    def filter_values(self, values, used):
        return [number for number in values if number not in used]

    def get_spot(self, board, state):
        for row in range(board):
            for column in range(board):
                if state[row][column] == 0:
                    return row, column

    def filter_row(self, state, row):
        number_set = range(1, self.type+1)
        in_row = [number for number in state[row] if (number != 0)]
        options = self.filter_values(number_set, in_row)
        return options

    def filter_col(self, options, state, column):
        in_column = []
        for column_index in range(self.type):
            if state[column_index][column] != 0:
                in_column.append(state[column_index][column])
        options = self.filter_values(options, in_column)
        return options

    def filter_quad(self, options, state, row, column):
        in_block = []
        row_start = int(row/self.height)*self.height
        column_start = int(column/3)*3

        for block_row in range(0, self.height):
            for block_column in range(0,3):
                in_block.append(state[row_start + block_row][column_start + block_column])
        options = self.filter_values(options, in_block)
        return options

    def actions(self, state, row, column):
        options = self.filter_row(state, row)
        options = self.filter_col(options, state, column)
        options = self.filter_quad(options, state, row, column)

        return options

def backtracking(board):
    problem = Problem(board)
    if problem.goal_test(board):
        return board

    row,column = problem.get_spot(problem.type, board)
    options = problem.actions(board, row, column)

    for option in options:
        board[row][column] = option
        if backtracking(board):
            return board
        else:
            board[row][column] = 0

    return None

def solve_bt(board):

    print ("\nSolving with Backtracking DFS...")
    start_time = time.time()
    solution = backtracking(board)
    elapsed_time = time.time() - start_time

    if solution:
        print ("Found solution")
        for row in solution:
            print (row)
    else:
        print ("No possible solutions")

    print ("Elapsed time: " + str(elapsed_time))

def input(filename, grid_number):
    f = open(filename,"r")
    numbers = []
    grid = []
    for x in f:
        for i in range(len(x)):
            if (i%2) == 0:
                numbers.append(int(x[i]))

    start = 0
    end = grid_number
    while end != (grid_number*grid_number)+grid_number:
        grid.append(a[start:end])
        start = end
        end = end + grid_number

    return grid
