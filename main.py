def solveMaze(maze, start, end):
    path = ""
    if end[0] < 0 or end[1] < 0 or end[0] >= len(maze) or end[1] >= len(maze[0]):  # we verify if the end point is valid
        path += "-_-"
        return path
    if start[0] < 0 or start[1] < 0 or start[0] >= len(maze) or start[1] >= len(
            maze[0]):  # we verify if the start point is valid
        path += "-_-"
        return path

    result_dict = {}  # we save all the positions in a list as tuples for the elements that have a 1
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1:
                key1 = (i, "x")  # create the key
                if key1 not in result_dict:
                    result_dict[key1] = []
                result_dict[key1].append((i, j))

    if maze[start[0]][start[1]] == 0:  # we first transform the starting point into a 1 if it is the case
        maze[start[0]][start[1]] = 1

    posWeHaveBeenTo = []  # we are going to use this list to save the positions we have been
    curr = start  # we use curr for the current position we are on
    last = (-1, -1)  # we are going to use last for the last position we were on
    while curr != end:
        ok = 0
        for key in result_dict:  # for every key in dictionary
            for val in result_dict[key]:  # for every tuple in the list
                if curr[0] == val[0] and last != val and val not in posWeHaveBeenTo and curr[1] != val[1]:
                    # same line and last position is different from the next, and we have not been to val before and columns are different
                    # jump to next position, append it to list, check if we went right or left and break
                    last = curr
                    posWeHaveBeenTo.append(last)
                    ok = 1
                    if curr[1] > val[1]:
                        path += "Left "
                    else:
                        path += "Right "
                    curr = val
                    break
                elif curr[1] == val[1] and last != val and val not in posWeHaveBeenTo and curr[0] != val[0]:
                    last = curr
                    posWeHaveBeenTo.append(last)
                    ok = 1
                    if curr[0] < val[0]:
                        path += "Down "
                    else:
                        path += "Up "
                    curr = val
                    break
        if ok == 0:
            # if from the current position we cannot advance anymore we are going to delete this one from the dictionary
            # and go back to the last one until we find a way to go, or we are back to the start
            for key in result_dict:
                if curr in result_dict[key]:
                    result_dict[key].remove(curr)  # we delete the current position
            if (len(posWeHaveBeenTo) - 1) < 0:  # we check to see if we are back to the start
                path = "-_-"
                return path
            else:
                curr = posWeHaveBeenTo[len(posWeHaveBeenTo) - 1]  # we jump back one position
            posWeHaveBeenTo.pop()  # we delete the last position we have been to from the list
            path2 = path.split()
            path = ' '.join(path2[:-1]) + ' '  # we delete the last move from the path
    return path


maze = [[0, 0, 0, 1, 1],  # 00 01 02 03 04
        [0, 1, 1, 0, 0],  # 10 11 12 13 14
        [0, 0, 0, 0, 1],  # 20 21 22 23 24
        [0, 0, 1, 0, 1]]  # 30 31 32 33 34
start = (1, 1)
end = (0, 3)

path = solveMaze(maze, start, end)
print(path)

