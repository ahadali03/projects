# define the Sudoku grid as a 2D list
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# define the function to print the grid
def print_grid(grid):
  for i in range(9):
    for j in range(9):
      print(grid[i][j], end=' ')
    print()

# define the function to find the next empty cell
def find_next_empty(grid):
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        return (i, j)
  return None

# define the function to check if a given number is valid in the current position
def is_valid(grid, num, pos):
  # check the row
  for i in range(9):
    if grid[pos[0]][i] == num and pos[1] != i:
      return False

  # check the column
  for i in range(9):
    if grid[i][pos[1]] == num and pos[0] != i:
      return False

  # check the box
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y*3, box_y*3 + 3):
    for j in range(box_x*3, box_x*3 + 3):
      if grid[i][j] == num and (i,j) != pos:
        return False

  return True

# define the function to solve the Sudoku
def solve(grid):
  # find the next empty cell
  next = find_next_empty(grid)
  if not next:
    return True
  else:
    row, col = next

  # try each number from 1 to 9
  for num in range(1,10):
    if is_valid(grid, num, (row, col)):
      grid[row][col] = num

      if solve(grid):
        return True

      grid[row][col] = 0

  return False

# solve the Sudoku
solve(grid)

# print the solved grid
print_grid(grid)