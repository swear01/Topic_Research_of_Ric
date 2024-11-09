from util import read_data
import pathlib

def read_result(result_path, w, r):
    def IndexToXY(index):
        index -= 1
        if index < (w-1)*r:
            return (0, index % (w-1), index // (w-1)) # Horizontal
        else:
            index -= (w-1)*r
            return (1, index % w, index // w) # Vertical

    with open(result_path, 'r') as f:
        line = f.readlines()[1]
    dominos = []
    for i in map(int, line.split()):
        if i <= 0: continue
        dominos.append(IndexToXY(i))
    return dominos

def domino_to_grid(dominos, w, h):
    grid = [["" for _ in range(h)] for _ in range(w)]
    for domino in dominos:
        x, y = domino[1], domino[2]
        if domino[0] == 0: # Horizontal
            grid[x][y] = "Right"
            grid[x+1][y] = "Left"
        else: # Vertical
            grid[x][y] = "Down"
            grid[x][y+1] = "Up"
    return grid

def blocks(num, dir) -> list[str]:
    match dir:
        case "Right":
            return ["┏━━━━", f"┃{num:2d}  ", "┗━━━━"]
        case "Left":
            return ["━━━━┓", f" {num:2d} ┃", "━━━━┛"]
        case "Down":
            return ["┏━━━┓", f"┃{num:2d} ┃", "┃   ┃"]
        case "Up":
            return ["┃   ┃", f"┃{num:2d} ┃", "┗━━━┛"]
        
    return ["      ", "      ", "      "] # should not reach here


def gen_print_grid(grid,data):
    #Each number occupie 3x3 space, the direction is where didn't have wall.
    w, h = len(grid), len(grid[0])
    text_grid = []
    for y in range(h):
        line = [[],[],[]]
        for x in range(w):
            block = blocks(data[x][y], grid[x][y])
            for i in range(3):
                line[i] += block[i]
        text_grid += line
    return "\n".join(["".join(line) for line in text_grid])

def write_result(text, result_path:pathlib.Path):
    with open(result_path, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    result_path = "./output.txt"
    #data_path = "./dataset/2_test/2_test_1.txt"
    #the_path = pathlib.Path("6_extreme/6_23208493975975672.txt")
    the_path = pathlib.Path("9_ambiguous/9_23398530460212129.txt")

    data_path = pathlib.Path("./dataset/") / the_path
    write_path = pathlib.Path("./result/") / the_path
    data = read_data(data_path)


    w, h = len(data), len(data[0])
    dominos = read_result(result_path, w, h)
    grid = domino_to_grid(dominos, w, h)
    text_grid = gen_print_grid(grid, data)
    write_result(text_grid, write_path)
    print(text_grid)
    

