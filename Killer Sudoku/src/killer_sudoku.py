# pylint: disable=undefined-variable, redefined-outer-name, line-too-long
# datas from: https://github.com/heetbeet/purge-and-merge
from z3 import *
import ast
from pathlib import Path
from pprint import pprint

def read_answers(file):
    with open(file, 'r',encoding='utf-8') as f:
        answers = f.read()
    answers = [ast.literal_eval(x) for x in answers.strip().split('\n')]
    return answers

# From UvA-KR16
def read_sudoku(filename):
    # print 'the constraints from file ', filename, ' are:'
    file_reader = open(filename, 'r')
    lines = file_reader.readlines()
    killerRules = []
    f = lambda x: (int(x[0]) , int(x[1]))

    for l in lines:
        # print l
        (s, t) = int(l.split(' ')[0]), l.split(' ')[1:]
        lst = list(map(f, t))
        killerRules.append((int(s), lst))
    return killerRules

def killer_solver(killer_name:Path):
    width = 9 # Should be fixed

    text_constraints = read_sudoku(killer_name)

    solver = Solver()
    sudoku = [IntVector(f'{i}',width) for i in range(width)]


    # Add constraints
    for i in range(width):
        for j in range(width):
            solver.add(1 <= sudoku[i][j], sudoku[i][j] <= 9) # All numbers must be between 1 and 9

    for column in sudoku:
        solver.add(Distinct(column)) # All numbers in a column must be distinct
    for row in zip(*sudoku):
        solver.add(Distinct(row)) # All numbers in a row must be distinct

    block_size = 3 # Should be fixed
    for i in range(0,width,block_size): # Iterate over all blocks
        for j in range(0,width,block_size):
            block = [sudoku[x][y] for x in range(i,i+block_size) for y in range(j,j+block_size)]
            solver.add(Distinct(block)) # All numbers in a block must be distinct

    for constriant in text_constraints: # Iterate over all constraints
            cage = [sudoku[x][y] for x,y in constriant[1]]
            solver.add(Sum(cage)==constriant[0]) # Sum of all numbers in a cage must be equal to the constraint
            solver.add(Distinct(cage)) # All numbers in a cage must be distinct

    if solver.check() == sat:
        model = solver.model()
        result = [[model[sudoku[i][j]].as_long() for j in range(width)] for i in range(width)]
        return result
    else:
        raise Exception('No solution found')

def validate(ans, constraints):
    for constraint in constraints:
        cage = [ans[x][y] for x,y in constraint[1]]
        if sum(cage) != constraint[0]:
            return False
        if len(set(cage)) != len(cage):
            return False
    return True

if __name__ == '__main__':
    killer = Path('data/puzzle00003.txt')
    # print(killer_solver(killer, ans))
    #print(read_sudoku(killer))
    solution = killer_solver(killer)
    pprint(solution)
    print(validate(solution, read_sudoku(killer)))