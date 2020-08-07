# Torus-8-Puzzle-A-Search
Goal State
The goal state of the puzzle is [1, 2, 3, 4, 5, 6, 7, 8, 0]

Heuristic
Since we are using the A* search algorithm, we should agree on a heuristic. For simplicity, we will use the count of tiles which are not in their goal spaces.

In the images provided in the summary, the h() value for the second and third states is 5 (tiles 4, 6, and 7 are in their goal locations). The first standard example and the horizontal wrapping example each have an h() value of 6, since we moved tiles out of their goal locations.

Functions

print_succ(state) — given a state of the puzzle, represented as a single list of integers with a 0 in the empty space, print to the console all of the possible successor states
solve(state) — given a state of the puzzle, perform the A* search algorithm and print the path from the current state to the goal state
