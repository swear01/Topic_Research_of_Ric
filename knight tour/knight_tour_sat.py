# this code transform knight challange to DIMAC sat form by Hamiliton path

width = 6
height = 6

total_nodes = width * height
pathes = []
clauses = []

def get_node(x, y):
    return (y-1) * width + x

def get_literal(node, position):
    return (node-1) * total_nodes + position

# shape
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16

# knight problem to bidirection path set

for x in range(1, width):
    for y in range(1, height-1):
        pathes.append((get_node(x, y), get_node(x+1, y+2))) # \
        pathes.append((get_node(x+1, y), get_node(x, y+2))) # /

for x in range(1, width-1):
    for y in range(1, height):
        pathes.append((get_node(x, y+1), get_node(x+2, y))) # _/
        pathes.append((get_node(x, y), get_node(x+2, y+1))) # \_

#print(pathes)
# Hamiliton path to SAT

# 1. Each node must appear in the path

for node in range(1, total_nodes+1):
    clause = []
    for i in range(1, total_nodes+1):
        clause.append(get_literal(node, i))
    clauses.append(clause)

# 2. Every position in the path must be occupied by some node

for position in range(1, total_nodes+1):
    clause = []
    for node in range(1, total_nodes+1):
        clause.append(get_literal(node, position))
    clauses.append(clause)

# 3. No node appears in a position in the path more than once

for node in range(1, total_nodes+1):
    for pos_i in range(1, total_nodes+1):
        for pos_j in range(pos_i+1, total_nodes+1):
            clauses.append([-get_literal(node, pos_i), -get_literal(node, pos_j)])

# 4. No two nodes occupy the same position in the path

for position in range(1, total_nodes+1):
    for node_i in range(1, total_nodes+1):
        for node_j in range(node_i+1, total_nodes+1):
            clauses.append([-get_literal(node_i, position), -get_literal(node_j, position)])

# 5. Non adjacent nodes cannot be adjacent in the path

path_set = set(pathes)
for node_j in range(1, total_nodes+1):
    for node_i in range(1, node_j):
        if (node_i, node_j) not in path_set and (node_j, node_i) not in path_set:
            for position in range(1, total_nodes):
                clauses.append([-get_literal(node_i, position), -get_literal(node_j, position+1)])
                clauses.append([-get_literal(node_j, position), -get_literal(node_i, position+1)])
            ## Code for closed path (Hamiliton cycle)
            # clauses.append([-get_literal(node_i, total_nodes), -get_literal(node_j, 1)])
            # clauses.append([-get_literal(node_j, total_nodes), -get_literal(node_i, 1)])




# Save the clauses to DIMAC file

with open(f'knight_{width}x{height}.cnf', 'w', encoding="utf-8") as f:
    f.write(f'p cnf {total_nodes*total_nodes} {len(clauses)}\n')
    for clause in clauses:
        f.write(' '.join(map(str, clause)) + ' 0\n')
