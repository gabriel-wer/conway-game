# GAME OF LIFE

### ABOUT
Based on the Conway game of life model [LINK](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

### RULES
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

### NOTES
If you just run the program normally, the cells are generated automagically using randomInts (0, 1)

If you set the flag '-e' or '--empty' the program will start with an empty array and you can draw on it and press space when you're finished

### COMMANDS
```bash
-e or --empty = Starts with an empty canvas
-c or --columns = Set the starting number of columns
-r or --rows = Set the starting number of rows
-cs or --cell= Set the starting cell size

```

![image](https://i.imgur.com/N8tGFz9.gif)
