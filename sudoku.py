import time
from functools import wraps

def show_process_time(method):
    @wraps(method)
    def wrapper(self,*args, **kwargs):
        time_start = time.time()
        result = method(self,*args, **kwargs)
        time_diff = time.time() - time_start
        print(f"{method.__name__} ran in : {time_diff} sec")        

    return wrapper


class Sudoku:

    def __init__(self, fname):
        path = f"./sudoku/{fname}"
        with open(path) as f:
            data = f.read().split("\n")
        matrix = []
        for i in data:
            num = [int(j) for j in i.split(",")]
            matrix.append(num)
        self.fname = matrix
        

    def __str__(self):
        result = ""
        for row in self.fname:
            s = ""
            for num in row:
                s += f"{num} "
            s = s.strip(" ")
            result += f"{s}\n"
        return result.strip("\n")

    def check_block(self, block_idx):
        row,col = divmod(block_idx,3)
        num = []
        for i in range(row*3,(row+1)*3):
            for j in range(col*3,(col+1)*3):
                if self.fname[i][j] != 0:
                    num.append(self.fname[i][j])
        return len(num) == len(set(num))
        
    def check_row(self, row_idx):
        unique = list(filter(lambda a: a!= 0,self.fname[row_idx]))
        return len(unique) == len(set(unique))

    def check_col(self, col_idx):
        f = lambda matrix,i: [row[i] for row in matrix]
        unique = list(filter(lambda a: a!= 0,f(self.fname,col_idx)))
        return len(unique) == len(set(unique))

    def is_solved(self):

        target = set([i for i in range(1,10)])
        
        # check row
        for i in range(9):
            if set(self.fname[i]) != target:
                return False
            
        # check col
        f = lambda matrix,i: [row[i] for row in matrix]
        for i in range(9):
            if set(f(self.fname,i)) != target:
                return False
            
        # check block
        for i in range(9):
            row,col = divmod(i,3)
            block = []
            for j in range(row*3,(row+1)*3):
                for k in range(col*3,(col+1)*3):
                    block.append(self.fname[j][k])
            if set(block) != target:
                return False
            
        return True

    @show_process_time
    def solve(self):
        
        def find_empty(self):
            for i in range(len(self.fname)):
                for j in range(len(self.fname[0])):
                    if self.fname[i][j] == 0:
                        return (i, j)
            return None
        
        def valid(self,num,row,col):
            # check row
            for i in range(9):
                if self.fname[row][i] == num and col != i:
                    return False
            # check col
            for i in range(9):
                if self.fname[i][col] == num and row != i:
                    return False
            # check block
            block_row = row//3
            block_col = col//3
            for i in range(block_row*3, (block_row+1)*3):
                for j in range(block_col*3, (block_col+1)*3):
                    if self.fname[i][j] == num and (i,j) != (row,col):
                        return False
            return True
        
        def step(self):
            pos = find_empty(self)
            if not pos:
                return True
                # break
            else:
                row, col = pos[0], pos[1]


            for i in range(1,10):
                if valid(self, i, row, col):
                    self.fname[row][col] = i
                    if step(self):
                        return True
                        # break

            return False
        
        step(self)

sudoku1 = Sudoku("sudoku3.txt")
print(sudoku1,end="\n\n")
print(sudoku1.check_block(0))
print(sudoku1.check_block(3))
print(sudoku1.check_block(6))
print(sudoku1.check_row(0))
print(sudoku1.check_row(1))
print(sudoku1.check_row(2))
print(sudoku1.check_col(0))
print(sudoku1.check_col(1))
print(sudoku1.check_col(2))


print(sudoku1.is_solved())

sudoku1.solve()

print()
print(sudoku1,end="\n\n")

print(sudoku1.is_solved())
