#!/usr/bin/python3
""" Lockboxes """

def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    if type(boxes) is not list or len(boxes) == 0:
        return False

    """if len(boxes) == 1:
        return True"""
    newboxes = []

    for i in range(len(boxes)):
        """if len(boxes[i]) == 0:
            return False """
              
        for j in range(len(boxes[i])):
            """ checks every item in the internal list"""
            if boxes[i][j] in newboxes or boxes[i][j] > len(boxes) - 1:
                  break
            elif boxes[i][j] == 0:
                break
            else:
                newboxes.append(boxes[i][j])

    if len(newboxes) == len(boxes) -1:
        return True
    else:
         return False