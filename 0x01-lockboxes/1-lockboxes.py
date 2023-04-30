#!/bin/python3
""" Lockboxes """

def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    if type(boxes) is not list:
            return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    newboxes = []
    i=0
    while (i < len(boxes)):
        if i == len(boxes) - 1:
            return True
        
        for j in range(len(boxes[i])):
            if not boxes[i]:
                return False
            if boxes[i][j] == i+1:
                i += 1
                break
            elif boxes[i][j] == boxes[i][-1]:
                return False


boxes = [[1], [2], [3], [4], [0]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))