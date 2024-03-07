import cv2
import numpy as np

canvas = np.ones((500,1200,3))
obstacle_set = set()
obstacle_list = []

for y in range(0,500):
    for x in range(0,1200):
        if (0<=y<=5):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (0<=x<=5):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (495<=y<500):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (1195<=x<1200):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (95<=x<=180) and (95<=y<500):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (270<=x<=355 and 0<=y<=405):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (895<=x<=1020) and (45<=y<=130):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (1015<=x<1105 and 45<=y<=455):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))
        elif (895<=x<=1020 and 370<=y<=455):
            obstacle_set.add((x,y))
            obstacle_list.append((x,y))

for point in obstacle_list:
    canvas[point[1],point[0]] = [255, 0, 0]

cv2.rectangle(canvas, (100, 499), (175, 100), (0 , 0, 255), -1)
cv2.rectangle(canvas, (275, 400), (350, 0), (0 , 0, 255), -1)
cv2.rectangle(canvas, (900, 125), (1100, 50), (0 , 0, 255), -1)
cv2.rectangle(canvas, (900, 450), (1100, 375), (0 , 0, 255), -1)
cv2.rectangle(canvas, (1020, 450), (1100, 50), (0, 0, 255), -1)
canvas = cv2.flip(canvas,0)
    

cv2.imshow("dikjksra",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()