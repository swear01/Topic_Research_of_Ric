# Topic Research Dominosa

This project is aim to use SAT solver to solve a real problem.  

## Dataset

The dataset is from Simon Tatham's Portable Puzzle Collection.  
The dataset is named by its random seed.  

[Data Source](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/dominosa.html)

I manually type the numbers into the file.  

## Generate Dataset

The Author (Simon Tatham) didn't have a good way.  
He generate the dataset randomly (with ambiguous section avoidance).  
And use solver to test if it has unique solution.  

## Modeling

Each possible domino own a literal.  
literal = 1 is choosen, literal = 0 is not.  
Group all possible dominos with the same pair of numbers. (call it a bundle)

1. No 2 dominos (or more) from the same bundle can be choosen.  
2. No 2 dominos (or more) which share a number can be choosen.  
3. Can't choose 0 domino from a bundle.  
