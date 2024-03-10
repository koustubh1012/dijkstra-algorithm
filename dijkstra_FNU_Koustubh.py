# Author: FNU Koustubh
# Email: koustubh@umd.edu
# Github repo: https://github.com/koustubh1012/enpm661_project2_dijkstra.git

# import libraries
import cv2
import numpy as np
import heapq as hq

canvas = np.ones((500,1200,3))   # creating a frame for video generation
obstacle_set = set()             # set to store the obstacle points
obstacle_list = []               # list to store the obstacle points in order for videp

node_grid = [[float('inf')] * 500 for _ in range(1200)]       # create a 2D array for storing cost to come
closed_set = set()               # set to store the value of visited and closed points
closed_list = []                 # list to store the closed nodes


'''
Loop to define the obstacle points oin the map
'''
for y in range(500):
    for x in range(1200):
        canvas[y,x] = [255,255,255]
        if (0<=y<=5):                      # points in the bottom boundary
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (0<=x<=5):                   # points in the left boundary
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (495<=y<500):                 # points in the top boundary
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (1195<=x<1200):               # points in the right boundary
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (95<=x<=180) and (95<=y<500):         # points in first rectangle
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        elif (270<=x<=355 and 0<=y<=405):          # points in second rectangle
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
            node_grid[x][y] = -1
        
        # Points int the C-shaped obstacle
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

        # Points in the hexagon obstacle
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


'''Function to generate 8-connected space'''
# Funtion to move to the up left node
def move_up_left(node):
    x = node[3][0]-1
    y = node[3][1]+1
    c2c = node[0] + 1.4
    return (x,y),c2c

# Funtion to move to the up node
def move_up(node):
    x = node[3][0]
    y = node[3][1]+1
    c2c = node[0] + 1
    return (x,y),c2c

# Funtion to move to the up right node
def move_up_right(node):
    x = node[3][0]+1
    y = node[3][1]+1
    c2c = node[0] + 1.4
    return (x,y),c2c

# Funtion to move to the left node
def move_left(node):
    x = node[3][0]-1
    y = node[3][1]
    c2c = node[0] + 1
    return (x,y),c2c

# Funtion to move to the right node
def move_right(node):
    x = node[3][0]+1
    y = node[3][1]
    c2c = node[0] + 1
    return (x,y),c2c

# Funtion to move to the down left node
def move_down_left(node):
    x = node[3][0]-1
    y = node[3][1]-1
    c2c = node[0] + 1.4
    return (x,y),c2c

# Funtion to move to the down node
def move_down(node):
    x = node[3][0]
    y = node[3][1]-1
    c2c = node[0] + 1
    return (x,y),c2c

# Funtion to move to the down right node
def move_down_right(node):
    x = node[3][0]+1
    y = node[3][1]-1
    c2c = node[0] + 1.4
    return (x,y),c2c

# Get the start point from the user
valid_start = False
while (not valid_start):
    start_x = int(input("Enter the Start Point X coordinate: "))
    start_y = int(input("Enter the Start Point Y coordinate: "))
    if (start_x,start_y) in obstacle_set: 
        print("Invalid Start Point, Enter Again")
    else:
        # cost to come, index, parent nodes as list and coordinate values (x,y)
        initial_node = (0, 1, [], (start_x,start_y))
        valid_start = True

# Get goal point from the user
valid_goal = False
while(not valid_goal):
    goal_x = int(input("Enter the Goal Point X coordinate: "))
    goal_y = int(input("Enter the Goal Point Y coordinate: "))
    if (goal_x,goal_y) in obstacle_set:
        print("Invalid Goal Point, Enter again")
    else:
        goal = (goal_x, goal_y)
        valid_goal = True

new_index = 1      # Variable to generate index of new nodes
open_list = []     # List to store the open nodes
hq.heappush(open_list,initial_node)        # Push initial node to the list
hq.heapify(open_list)       # covers list to heapq data type

# Mark the obstacle points in the frame, including points after bloating
for point in obstacle_list:
    canvas[point[1],point[0]] = [255, 0, 0]

# Draw the obstacles in the frame, excluding the points after bloating
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

# Loop to impllement Dijkstra's algorithm
while(open_list):
    # cost to come, index, parent node index and coordinate values (x,y)
    node = hq.heappop(open_list)       # pop the node with lowest cost to come
    closed_set.add(node[3])            # add the node coordinates to closed set
    closed_list.append(node)           # add the node to the closed list
    index = node[1]                    # store the index of the current node
    parent_index = node[2]             # store the parent index list of current node
    
    if node[3] == goal:                # if the node is goal position, exit the loop
        print("Goal reached")
        break

    point, c2c = move_up_left(node)                                     # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()       
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1 
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)                            # push the new node to the open list

    point, c2c = move_up(node)                                          # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)

    point, c2c = move_up_right(node)                                    # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)                            # push the new node to the open list

    point, c2c = move_left(node)                                        # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)                            # push the new node to the open list

    point, c2c = move_right(node)                                       # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)                            # push the new node to the open list

    point, c2c = move_down_left(node)                                   # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)                            # push the new node to the open list

    point, c2c = move_down_right(node)                                  # get the new node's coordinates and cost to come
    if point not in obstacle_set and point not in closed_set:           # check if the new node is in the obstacle set or visited list
        x = point[0]
        y = point[1]
        if c2c<node_grid[x][y]:                                         # check if the new cost to come is less than original cost to come
            new_parent_index = parent_index.copy()
            new_parent_index.append(index)                              # Append the current node's index to the new node's parent index list
            new_index+=1
            node_grid[x][y] = c2c                                       # Update the new cost to come
            new_node = (c2c, new_index, new_parent_index, point)
            hq.heappush(open_list, new_node)                            # push the new node to the open list
   
   
print("Processing Video...")

path = node[2]            # Get the parent node list 
counter = 0               # counter to count the frames to write on video

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
video_writer = cv2.VideoWriter('output.mp4', fourcc, 30, (1200, 500))

'''
Loop to mark the explored nodes in order on the frame
'''
for node in closed_list:
    canvas[node[3][1], node[3][0]] = [0, 255, 0]
    canvas_flipped = cv2.flip(canvas,0)
    counter +=1
    if counter%750 == 0 or counter == 0:
        canvas_flipped_uint8 = cv2.convertScaleAbs(canvas_flipped)
        video_writer.write(canvas_flipped_uint8)

'''
Loop to mark the path created
'''
for index in path:
    for node in closed_list:
        if node[1] == index:
            canvas[node[3][1], node[3][0]] = [0,0,0]
            canvas_flipped = cv2.flip(canvas,0)
            canvas_flipped_uint8 = cv2.convertScaleAbs(canvas_flipped)

'''
Loop to add some additional frames at the end of the video
'''
for i in range(150):
    video_writer.write(canvas_flipped_uint8)
    
print("Video Processed")

video_writer.release()