from itertools import combinations
import pathlib

def read_data(data_path):
    with open(data_path) as f:
        data = f.read()
    data = [list(map(int, line.split())) for line in data.split("\n")]
    return list(zip(*data))

def at_most_1(args:list[int]):
    constriant = list(combinations(args, 2))
    constriant = [(-x, -y,0) for x,y in constriant]
    return constriant

def dont_0(args:list[int]):
    return [(*args,0)]

def basic_constraint(w,h):
    # 2. No 2 dominos (or more) which share a number can be choosen.  
    # Horizontial is (w-1)*h, Vertical is w*(h-1)
    constraints = []
    v_start = (w-1)*h
    def hXYtoIndex(x,y):
        return y*(w-1) + x +1
    def vXYtoIndex(x,y):
        return v_start + y*w + x +1
    
    for x in range(w):
        for y in range(h):
            conflicts = []
            if x > 0: # not left most
                conflicts.append(hXYtoIndex(x-1,y))
            if x < w-1: # not right most
                conflicts.append(hXYtoIndex(x,y))
            if y > 0: # not top most
                conflicts.append(vXYtoIndex(x,y-1))
            if y < h-1: # not bottom most
                conflicts.append(vXYtoIndex(x,y))
            constraints += at_most_1(conflicts)
    return constraints

def create_dominos(data):

    w,h = len(data), len(data[0])
    v_start = (w-1)*h
    def hXYtoIndex(x,y):
        return y*(w-1) + x +1
    def vXYtoIndex(x,y):
        return v_start + y*w + x +1
    
    
    dominos : dict[tuple[int,int],list[int]] = {}
    for j in range (h):
        for i in range (j+1):
            dominos[(i,j)] = []

    # Horizontial dominos
    for x in range (w-1):
        for y in range(h):
            if data[x][y] < data[x+1][y]: domino = (data[x][y], data[x+1][y])
            else: domino = (data[x+1][y], data[x][y])
            dominos[domino].append(hXYtoIndex(x,y))
    # Vertical dominos
    for x in range (w):
        for y in range(h-1):
            if data[x][y] < data[x][y+1]: domino = (data[x][y], data[x][y+1])
            else: domino = (data[x][y+1], data[x][y])
            dominos[domino].append(vXYtoIndex(x,y))
    return dominos
                
def bundle_constraints(dominos: dict[tuple[int,int],list[int]] ):
    constraints = []
    for points, values in dominos.items():
        constraints.extend(dont_0(values)) # At least 1
        constraints.extend(at_most_1(values)) # At most 1
    return constraints

def write_constraints(constraints, write_path:pathlib.Path):
    with open(write_path, 'w') as f:
        for constraint in constraints:
            f.write(" ".join(map(str, constraint)) + "\n")