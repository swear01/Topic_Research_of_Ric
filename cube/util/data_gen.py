from random import choices, choice

sav_locs = [f"./data/{i:05d}.icosah" for i in range(1, 11)]

for sav_loc in sav_locs:
    possible_blocks = []
    for x in range(0,6):
        for y in range(0,6):
            for b in (0,1):
                total = x + y + b
                if 3 <= total <= 8:
                    possible_blocks.append((x,y,b))
                    
    colored = choices(possible_blocks, k=20)

    remaining = list(set(possible_blocks) - set(colored))

    start = choice(remaining)

    with open(sav_loc, "w") as f:
        f.write(f"{start[0]} {start[1]} {start[2]}\n\n")
        for x,y,b in colored:
            f.write(f"{x} {y} {b}\n")