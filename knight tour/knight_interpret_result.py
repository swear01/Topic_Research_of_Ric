width = height = 6

file_name = f"./knight_{width}x{height}.result"
with open(file_name, 'r', encoding="utf-16-le") as f:
    line = f.readlines()[-1]

#print(line)

total_nodes = width * height
grid = [[0 for _ in range(width)] for _ in range(height)]

def to_node(literal):
    return ((literal-1) // total_nodes) + 1, ((literal-1) % total_nodes) +1

def to_xy(pos):
    return ((pos-1) % width) + 1, ((pos-1) // width) + 1

# for num in line.split():
#     num = int(num)
#     if num <= 0: continue
#     node, pos = to_node(num)
#     print(num, end=" ")
# print()
# for num in line.split():
#     num = int(num)
#     if num <= 0: continue
#     node, pos = to_node(num)
#     print(node, end=" ")
# print()

for num in line.split():
    num = int(num)
    if num <= 0: continue
    node, pos = to_node(num)
    x, y = to_xy(node)
    grid[x-1][y-1] = pos

for row in grid:
    for node in row:
        print(f"{node:2d}", end="|")
    print()
