import pathlib
from util import *
    

if __name__ == "__main__":
    #data_path = pathlib.Path("dataset/6_extreme/6_23208493975975672.txt")
    the_path = pathlib.Path("9_ambiguous/9_23398530460212129.txt")
    #data_path = pathlib.Path("dataset/2_test/2_test_1.txt")
    write_path = pathlib.Path("constraints.txt")
    data_path = pathlib.Path("./dataset/") / the_path
    data = read_data(data_path)
    #print(data)
    dominos = create_dominos(data)
    constraints = []
    constraints += basic_constraint(len(data), len(data[0]))
    constraints += bundle_constraints(dominos)
    write_constraints(constraints, write_path)

    