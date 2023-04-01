# Maze-Jump-Between-Ones
This is a game we have invented, by combining multiple practical problems. The purpose of this exercise is to write a program - using a programming language of your desire - that generates a path between the entry point and the exit point, for any given bi-dimensional array.  


Here is an example of inputs:

[[0, 0, 1, 0], [1, 0, 1, 0], [0,0,0,0], [1,0,0,1]].  

An entry point example { i: 0, j: 3 }  

An exit point {i:3, j: 0} 

Here is one solution for the above input:  

[LEFT, DOWN, LEFT, DOWN] 

 
Rules:  

You can use commands - RIGHT, LEFT, UP, DOWN - to “jump” between 1’s. Each command is self-explanatory for the direction on which you can go - RIGHT for right, UP for up and so on. You should figure out how to implement these commands. 

You cannot start on a point marked with 0. If that happens, transform it into 1. 

There is no circular navigation, meaning that you cannot go past the “edge” of the bi-dimensional array.  

You cannot “jump” to a point marked with 0.  

The goal is to reach the exit point, while keeping a record of your path. 

There might be cases where you cannot reach your destination, in that case, return this string “-_-“.  

Solution:
As a solution for this problem I marked the elements that have as value 1 of the bi-dimensional array in a dictionary . For the key i used the this format :(1,"x") indicating line 1 , unkown colum. For every key in the dictionary there is a list of tuples that contain the position of the 1's. I used a list of past positions to remember the positions I have been to. While the current position and the end are different I go thourgh every tuple to check if there is any line or colum corelation. If there is we are jumping to that position. If we cannot advance anymore, I delete that position and go back to the previous until I reach the end of go back to the start.

Some personal examples:

maze = [[0,0, 0, 1, 0],
        [0,0, 1, 1, 0],
        [0,1, 1, 0, 0],
        [0,0, 0, 1, 1]]
start = (0, 0)
end = (2, 1)

maze = [[0,0, 0, 1, 0],
        [0,0, 1, 1, 0],
        [0,1, 1, 0, 1],
        [0,0, 0, 1, 1]]
start = (0, 0)
end = (2, 1)

maze = [[0,0, 0, 1, 1],
        [0,1, 1, 0, 0],
        [0,0, 0, 0, 1],
        [0,0, 1, 0, 1]]
start = (1,1 )
end = (0, 3)

maze = [[0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 1]]
start = (0, 3)
end = (3, 0)
