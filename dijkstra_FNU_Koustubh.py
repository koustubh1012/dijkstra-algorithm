import cv2
import numpy as np
import heapq as hq
import sys

canvas = np.ones((500,1200,3))
obstacle_set = set()
obstacle_list = []

node_grid = [[float('inf')] * 500 for _ in range(1200)]
closed_set = set()
closed_list = []

for y in range(500):
    for x in range(1200):
        canvas[y,x] = [255,255,255]
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

        elif(515<=x<=785) and (170<=y<=330):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif(330<=y<=405) and (-75*x+135*y-5925<=0) and (-75*x-135*y+103425>=0):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif(95<=y<=170) and (-75*x-135*y+61575<=0) and (-75*x+135*y+35925>=0):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1


def move_up_left(node):
    x = node[3][0]-1
    y = node[3][1]+1
    c2c = node[0] + 1.4
    return (x,y),c2c

def move_up(node):
    x = node[3][0]
    y = node[3][1]+1
    c2c = node[0] + 1
    return (x,y),c2c

def move_up_right(node):
    x = node[3][0]+1
    y = node[3][1]+1
    c2c = node[0] + 1.4
    return (x,y),c2c

def move_left(node):
    x = node[3][0]-1
    y = node[3][1]
    c2c = node[0] + 1
    return (x,y),c2c

def move_right(node):
    x = node[3][0]+1
    y = node[3][1]
    c2c = node[0] + 1
    return (x,y),c2c

def move_down_left(node):
    x = node[3][0]-1
    y = node[3][1]-1
    c2c = node[0] + 1.4
    return (x,y),c2c

def move_down(node):
    x = node[3][0]
    y = node[3][1]-1
    c2c = node[0] + 1
    return (x,y),c2c

def move_down_right(node):
    x = node[3][0]+1
    y = node[3][1]-1
    c2c = node[0] + 1.4
    return (x,y),c2c


new_index = 1

# cost to come, index, parent node index=0 and coordinate values (x,y)
start_x = int(input("Enter the Start Point X coordinate: "))
start_y = int(input("Enter the Start Point Y coordinate: "))
if (start_x,start_y) in obstacle_set:
    print("Invalid Start Point")
    sys.exit()
else:
    initial_node = (0, 1, [], (start_x,start_y))

goal_x = int(input("Enter the Goal Point X coordinate: "))
goal_y = int(input("Enter the Goal Point Y coordinate: "))
if (goal_x,goal_y) in obstacle_set:
    print("Invalid Goal Point")
    sys.exit()
else:
    goal = (goal_x, goal_y)

open_list = []
hq.heappush(open_list,initial_node)
hq.heapify(open_list)

for point in obstacle_list:
    canvas[point[1],point[0]] = [255, 0, 0]

cv2.rectangle(canvas, (100, 499), (175, 100), (0 , 0, 255), -1)
cv2.rectangle(canvas, (275, 400), (350, 0), (0 , 0, 255), -1)
cv2.rectangle(canvas, (900, 125), (1100, 50), (0 , 0, 255), -1)
cv2.rectangle(canvas, (900, 450), (1100, 375), (0 , 0, 255), -1)
cv2.rectangle(canvas, (1020, 450), (1100, 50), (0, 0, 255), -1)
pts = np.array([[650, 400], [780, 325], 
                [780, 175], [650, 100], 
                [520, 175], [520, 325]],
                np.int32)
canvas = cv2.fillPoly(canvas, [np.array(pts)], color=(0, 0, 255))

while(open_list):
    # cost to come, index, parent node index and coordinate values (x,y)
    node = hq.heappop(open_list)
    closed_set.add(node[3])
    closed_list.append(node)
    index = node[1]
    parent_index = node[2]
    if node[3] == goal:
        print("Goal reached")
        break

    point, c2c = move_up_left(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_up(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_up_right(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_left(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_right(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_down_left(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_down_right(node)
    if point not in obstacle_set and point not in closed_set:
        x = point[0]
        y = point[1]
        # c2c = round(c2c,2)
        if c2c<node_grid[x][y]:
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)
            new_index+=1
            node_grid[x][y] = c2c
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)
   
   
print("Processing Video...")
path = node[2]

counter = 0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format (lowercase 'v' is crucial)
video_writer = cv2.VideoWriter('output.mp4', fourcc, 30, (1200, 500))

for node in closed_list:
    canvas[node[3][1], node[3][0]] = [0, 255, 0]
    canvas_flipped = cv2.flip(canvas,0)
    counter +=1
    if counter%500 == 0 or counter == 0:
        canvas_flipped_uint8 = cv2.convertScaleAbs(canvas_flipped)
        video_writer.write(canvas_flipped_uint8)
        

# for node in closed_list:
#     canvas[node[3][1], node[3][0]] = [0, 255, 0]
#     canvas_flipped = cv2.flip(canvas,0)
#     counter +=1
#     if counter%1000 == 0:
#         cv2.imshow("project2",canvas_flipped)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

for index in path:
    for node in closed_list:
        if node[1] == index:
            canvas[node[3][1], node[3][0]] = [0,0,0]
            canvas_flipped = cv2.flip(canvas,0)
            canvas_flipped_uint8 = cv2.convertScaleAbs(canvas_flipped)

for i in range(150):
    video_writer.write(canvas_flipped_uint8)
    
# cv2.imshow("project2",canvas_flipped)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

print("Video Processed")


# cv2.destroyAllWindows()
video_writer.release()