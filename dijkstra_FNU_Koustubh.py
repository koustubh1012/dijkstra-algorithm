import cv2
import numpy as np
import heapq as hq
canvas = np.ones((500,1200,3))
obstacle_set = set()
obstacle_list = []


# cost to come, index, parent node index=0 and coordinate values (x,y)
initial_node = (0, 1, 0, (0,0))
goal = (5,5)
open_list = []
hq.heappush(open_list,initial_node)
hq.heapify(open_list)

node_grid = [[float('inf')] * 500 for _ in range(1200)]
closed_set = set()

for y in range(500):
    for x in range(0,1200):
        if (0<=y<=5):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (0<=x<=5):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (495<=y<500):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (1195<=x<1200):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (95<=x<=180) and (95<=y<500):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (270<=x<=355 and 0<=y<=405):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (895<=x<=1020) and (45<=y<=130):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (1015<=x<1105 and 45<=y<=455):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (895<=x<=1020 and 370<=y<=455):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1


def move_up_left(node):
    x = node[3][0]-1
    y = node[3][1]+1
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1.4
    else:
        c2c = node[0] + 1.4
    return (x,y),c2c

def move_up(node):
    x = node[3][0]
    y = node[3][1]+1
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1
    else:
        c2c = node[0] + 1
    return (x,y),c2c

def move_up_right(node):
    x = node[3][0]+1
    y = node[3][1]+1
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1.4
    else:
        c2c = node[0] + 1.4
    return (x,y),c2c

def move_left(node):
    x = node[3][0]-1
    y = node[3][1]
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1
    else:
        c2c = node[0] + 1
    return (x,y),c2c

def move_right(node):
    x = node[3][0]+1
    y = node[3][1]
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1
    else:
        c2c = node[0] + 1
    return (x,y),c2c

def move_down_left(node):
    x = node[3][0]-1
    y = node[3][1]-1
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1.4
    else:
        c2c = node[0] + 1.4
    return (x,y),c2c

def move_down(node):
    x = node[3][0]
    y = node[3][1]-1
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1
    else:
        c2c = node[0] + 1
    return (x,y),c2c

def move_down_right(node):
    x = node[3][0]+1
    y = node[3][1]-1
    if node_grid[x][y] == FloatingPointError('inf'):
        c2c = 1.4
    else:
        c2c = node[0] + 1.4
    return (x,y),c2c

while(open_list):
    node = hq.heappop(open_list)
    if node[3] == goal:
        print("Goal reached")
        break


# print(node[3])

























# for point in obstacle_list:
#     canvas[point[1],point[0]] = [255, 0, 0]

# cv2.rectangle(canvas, (100, 499), (175, 100), (0 , 0, 255), -1)
# cv2.rectangle(canvas, (275, 400), (350, 0), (0 , 0, 255), -1)
# cv2.rectangle(canvas, (900, 125), (1100, 50), (0 , 0, 255), -1)
# cv2.rectangle(canvas, (900, 450), (1100, 375), (0 , 0, 255), -1)
# cv2.rectangle(canvas, (1020, 450), (1100, 50), (0, 0, 255), -1)
# canvas = cv2.flip(canvas,0)
    

# cv2.imshow("dikjksra",canvas)

# cv2.waitKey(0)
# cv2.destroyAllWindows()