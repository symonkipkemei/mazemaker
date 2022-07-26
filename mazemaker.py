import random
from colorama import init, Fore


# initialize colorama
init()

# identity
walls = "w"
cell = "c"
unvisted_blocks = "u"



# 1. START WITH A GRID FULL OF WALLS

#  a function that create a maze with fixed heigh and width

def init_maze(width, height):
    """a maze"""
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            # generate an horizontal line
            line.append("u")
        #generate the vertical line
        maze.append(line)
    # a 2d list 
    return maze


# color code maze with colorama
def print_maze(maze):
    # loop through the vertical length of the maze
    for i in range(0, len(maze)):
        # loop through the horizontal length of the maze
        for j in range(0, len(maze[0])):
            # color code according to the identity
            if maze[i][j] == "u":
                print(Fore.WHITE, f"{maze[i][j]}",end = "")
            elif maze[i][j] == "c":
                print(Fore.GREEN, f"{maze[i][j]}",end = "")
            else:
                print(Fore.RED, f"{maze[i][j]}",end = "")
        print("\n")


# set width and height
height = 11
width = 27

maze = init_maze(width, height)

print_maze(maze)


# 2. PICK A CELL,SET IT AS A FREE SPOT

# pick starting point

starting_height = int(random.random() * height)
starting_width = int(random.random() * width)

# do not start on the block that is on the edge of the maze

if starting_height == 0:
    starting_height += 1
if starting_height == height -1:
    starting_height -= 1


if starting_width == 0:
    starting_width += 1
if starting_width == width- 1:
    starting_width -= 1


# add surrounding walls to the list

maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height-1, starting_width])
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])


# denote the block around the starting cell as walls
wall = None
maze[starting_height-1][starting_width] = wall
maze[starting_height][starting_width-1] = wall
maze[starting_height][starting_width+1] = wall
maze[starting_height+1][starting_width] = wall

# pick a random wall

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]