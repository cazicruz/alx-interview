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
    for i in range(len(boxes)):
        if len(boxes[i]) == 0:
            return False
              
        for j in range(len(boxes[i])):
              if boxes[i][j] in newboxes or boxes[i][j] > len(boxes) - 1:
                  break
              else:
                  newboxes.append(boxes[i][j])
    if len(newboxes) == len(boxes):
        return True
    else:
         return False
    
boxes = [[1], [2], [3], [4], [0]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))