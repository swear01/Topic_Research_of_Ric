from src.killer_sudoku import killer_solver, read_sudoku, validate
import pathlib

if __name__ == '__main__':
    data_folder = pathlib.Path('./data')
    for killer_file in list(data_folder.glob(f'*.txt'))[:10]:
        answer = killer_solver(killer_file)
        result = 'Valid' if validate(answer, read_sudoku(killer_file)) else 'Invalid'
        print(f'{killer_file.name}: {result}')
        if result == 'Valid':
            with open(f'./solution/{killer_file.stem}.ans', 'w') as f:
                for row in answer:
                    f.write(' '.join(map(str, row)) + '\n')
                
            
