#	maze_solver.py and maze_solver_finder.py

Creates a maze and attempts to solve it \
Created as an attempt to bog down the process to test the speed differences in windows. \
I found noticeable difference when running code in macOS, Windows and the Windows subsystem, I wanted to explore this \
Performance was too good so needed to loop it, so I created maze_solver_finder.py for that


Example is --seed 16723 --size 30
```
                            ↓
← ↓ ← ← → ↓ ↓ ← ↓ ← + ← + + ← ← ↑ ← ↑ → ↑ → ↑ + ↓ ← ← → ↑ →
↑ ↑ ← ↓ ↓ ← ← + + + + ↑ ← ↓ + ← ↑ ↑ + → ← → → ← → ↓ ← ← ↑ ↑
→ ↓ ↑ + ↑ → ← ↑ ↑ ↓ ↓ + → ↑ ← ← ↓ ↓ ↑ + ↓ ↑ → ← ← + + → → ↓
← ↓ ↓ ↓ + ↑ ↑ → ↑ ↓ + + + ← ↑ ← → → ↓ → ↓ ↓ ← ↓ → ← → ↑ ← ↑
↑ ↑ + + → ↓ ↑ → ← ↓ + ↑ → ← ↓ + ← + ↓ ← + ↓ ← ↑ → ↑ → ← → ↑
← ↓ + ↑ ← ↑ → → ↑ ↑ ↓ ↑ → ↓ ← → ↑ ↑ ↓ ← ← ← ↓ ↓ ↑ + ← + + →
+ ↑ → ↓ ↓ ↓ ↑ ↑ + ↓ + → ↓ ↓ ↑ + ← ↓ ← + → ↓ ← ↑ ↓ ↑ ← ↑ ↓ ←
→ → ↓ ← ↓ ↓ ↓ + ← ← → → ↓ + + → ↓ ← ↑ → ← ↓ ← ← → + ← ← ← +
↓ ← ↓ + ← ↑ ↓ ↓ → + + ↓ + ← → ↓ ← ↑ ← → ↑ ↑ ← ↑ ← ← → ↑ ↓ ↑
+ + ↑ → ↑ ↓ → + ← + ← + ← ↓ ↑ → ← → + → → → + ↓ → + → ↓ ← ↓
↑ ← → → → + + ↓ ↑ ↓ ← + ← + ↑ ↑ + ↓ + ↓ ← ← → ← ← ← ← → ↑ ↑
← + ↓ ↓ ↑ → + → ↓ ↓ ↑ → ↓ + ↓ ↑ ↑ ↑ ↓ ↑ + + + ↓ ← ↓ + + → ↓
+ → ← + ↑ + ↓ → + → ← + ← ↓ ↑ ↑ ← ↓ → → + + ← + ← ↑ ↑ + + ←
+ + → ↑ → → + + → → + ↓ + ← → → ↓ ↑ ↑ + ← + ↓ ↑ ← ↑ ← → ↑ →
+ ↓ ↓ → + → ↓ + → → ↓ ← ← → ← ↑ ↓ ↓ ↓ ← ↑ ← ↓ + ↑ → ↓ ↑ ← ↑
→ ← ↓ + ← ↓ + → ↑ ↓ + ↑ ↑ + → ← ← → + + → → → → ↓ → ↓ ← ↓ +
← → ← ↓ + ↑ + ↓ ↑ + + ↑ + ← → ← ↑ + ← ← + ↓ + ↓ ← ← ← ↓ ← ↓
+ → ↓ ← + + + ← ↑ ↓ + ↑ + + ← ↑ → ← ↑ ↓ ↓ ← ← + ↓ → ↓ ↓ ← +
↓ + ← ↑ ← ← ← → ↑ ↓ + ↓ + ← ← ← → → ← ↑ → ↑ ↓ → ↓ ↑ → → ← ↓
↓ → ← ↓ ↑ → ← + → → ↓ → ↓ ↓ ↓ ↑ + ↑ ← → → ↓ ↓ ← → ↓ ↓ ← ↑ →
← ↓ → → → → + ← → ↓ ← → + → + + ↓ → → → → + ↓ ↑ ↓ ← + + ↑ +
→ ← ↓ ↑ ← ← + ↑ + + ↑ + ↑ + → + + + ↑ ← ← → ↓ → ← ↓ ← + + →
← ← ← + → → ↓ ← ↑ ← + + → + + + → ↓ → + ↓ ← ← → + ← ↑ ↓ ↑ ←
← → ↓ ↑ ↑ + → + ↑ → → ↓ ↓ + ↓ → → + + + → ↑ + + ← ↓ ↓ ↓ → +
+ ↓ ↑ ← → ← ← ← + + ↓ ← → ← + + + ← ↓ ↑ → ← ↓ ↑ + ← ↑ → + ←
→ + ↓ ↓ ↓ + ↑ ↓ + ↑ ↓ → ← ↓ + ↑ ↓ + ↓ ↑ + ↑ ↓ + → ← → ← + ↓
↑ → → ↓ → → ↑ ← ↑ ↑ ↓ ↑ ↑ ← → ↓ ↑ ↓ + ← → + ↑ ↑ ↓ ↑ ↑ → + ↓
↓ ↓ ← + + ↓ ← ← → ← + → ↓ → → + ← ↑ ← ↓ → ← → → → → ← ↑ + ↓
↑ + + ↓ → + ↓ + ↓ + ↓ + → + + ↓ → + ← ↓ ↓ → ← ← + ← ↓ + ↓ →
↑ → ↑ + ↓ ← → ↑ → ↓ + → ← ↓ ↓ + ↑ + ← ← → + → + ↑ ← ↓ ↓ → ←
                            ↓
Solution(s):
                            ↓
                ↓ ← + ← + + ←
                + + + ↑ ←
                    ↓
                    +
                    +
                    ↓
                  ↓ + → ↓
            ↓ + ← ← → → ↓
            ↓ ↓   +   ↓ +
            → + ← + ← + ←
              ↓       +
              → ↓     → ↓
                +     + ←
                → → + ↓
                    ↓ ←
                  ↓ +
                  + +
                    +
                    + ↓
                      → ↓
                        + → + + ↓
                            → + + +
                          + + + → ↓
                          + ↓ → → +
                            + + + ←
                            +
                            → ↓
                              +
                              ↓
                            ↓ +
                            ↓
```
## What?

### maze_solver.py
Create a maze and solve it or use maze_solver_finder to get a maze

You can use a custom the size of the maze or the seed used to randomly generate it

```bash
usage: maze_solver.py [-h] [-d SIZE] [-s SEED] [--single] [--debug]

Create a maze and solve it

optional arguments:
    -h, --help
            show this help message and exit
    -d SIZE, --size SIZE
            Size of the puzzle
            Default: 10
    -s SEED, --seed SEED
            Seed the random to set reproducible results
            Default: None
    --single
            Return only one path
            Default: False
    --debug
            Debug the program
            Default: False
```

### maze_solver_finder.py
```bash
usage: maze_solver_finder.py [-h] [-d SIZE SIZE] [-s SEED SEED] [--debug]

Create a batch of mazes, solve and display the solvable ones.

optional arguments:
    -h, --help
            show this help message and exit
    -d SIZE SIZE, --size-range SIZE SIZE
            Minimum and maximum values
            Default: [5, 10]
    -s SEED SEED, --seed-range SEED SEED
            Seed of the random range
            Default: [0, 320000]
    --debug
            Debug the program
            Default: False

```


## Why?
I was trying to find why the Windows python was so much slower and looking for a potentially tasking process and through a maze solver might do the trick.  I was very incorrect.  So I created a maze_solver_finder.py that will create 1000s of mazes and solve them for a bigger time delta.  

End result was unimpressive.  Might be string related methods.  Expect to see more.

## Improvements?

Multitasking?  I don't think it can run too much faster though.

## State?
Tested and working. No know bugs.
