
source = "puzzle.sav"
size = 400
output = "./dataset/large_ambiguous/400_358360975447045.txt"

def load(source):
    with open(source, "r",encoding="utf-8") as f:
        puzzle = f.readlines()[6][16:]
    return puzzle

data = load(source)
print(data[:10])
    