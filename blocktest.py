
from numpy import *

#grid for the representation of the wall
wall =[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]
wall=reshape(wall,(8,8)) #to make the grid a matrix

#shapes of the blocks to be stacked
shapes = {
	'I':   [[0,0,0,0], 
                [0,0,0,0], 
		[0,0,0,0], 
		[1,1,1,1]],    #"I" block
		
	'J':   [[0,0,0], 
		[2,0,0], 
		[2,2,2]],      #"J" block
		
	'L':   [[0,0,0], 
                [0,0,3], 
		[3,3,3]],      #"L" block

	'O':   [[4,4], 
		[4,4]],        #"O" block
		
	'S':   [[0,0,0], 
		[0,5,5], 
		[5,5,0]],      #"S" block
		
	'T':   [[0,0,0], 
		[0,6,0], 
		[6,6,6]],      #"T" block

	'Z':   [[0,0,0], 
		[7,7,0], 
		[0,7,7]]       #"Z" block
}; 

#Block colors
colors = ["F92338", "C973FF", "1C76BC", "FEE356", "53D504", "36E0FF", "F8931D"];


def initialiseBlock(newBlock):
    # to identify the block to be stacked

    #VARIABLES
    #dimension* dimension of the block matrix
    #shape* shape of the identified block
    if ord(newBlock) == ord('I'):
        shape = shapes["I"]
        dimension = ['4','4']
    elif ord(newBlock) == ord('J'):
        shape = shapes["J"]
        dimension = ['3','3']
    elif ord(newBlock) == ord('L'):
        shape = shapes["L"]
        dimension = ['3','3']
    elif ord(newBlock) == ord('O'):
        shape = shapes["O"]
        dimension = ['2','2']
    elif ord(newBlock) == ord('S'):
        shape = shapes["S"]
        dimension = ['3','3']
    elif ord(newBlock) == ord('T'):
        shape = shapes["T"]
        dimension = ['3','3']
    elif ord(newBlock) == ord('Z'):
        shape = shapes["Z"]
        dimension = ['3','3']
    return shape, dimension


def isBlankSpaceLeft(dimension):
    #to check if the space is left in the row to stack the block

    #VARIABLES
    #wallRow* position of nth row in the wall
    #wallCols* position of nth column in the wall
    #flag* to get the position of first blank space
    #spaceLeft* Blank space left in the row
    #position* the posititon of the first blank space in the row

    
    

    wallRow=7                   #size of grid is 8*8, and the indexing is form 0
    while wallRow>=0:           #check for blank space till topmost line of the grid
        wallCols=0              
        flag=0                  
        spaceLeft=0             
        
        while wallCols<8:
            if wall[wallRow][wallCols]==0:   
                if flag==0:
                    position = [wallRow,wallCols]
                    flag=1
                spaceLeft = spaceLeft + 1
            wallCols = wallCols + 1
        
        if spaceLeft >= (int(dimension[1]) or int(dimension[1])):
            return spaceLeft, position
        
        if spaceLeft< (int(dimension[0]) or int(dimension[1])):
            wallRow=wallRow-1
        
        #conditin for rotation will occur hare   
          
def updateWall(shape,dimension,position):
    #stack the block in the wall

    #VARIABLES
    #lastRowBlank* lowest blank row in the column
    #firstaColumnBlank* first blank column in the row 
    #row* no of rows in the block
    #col* no of col in the block
    
    lastRowBlank = position[0]
    row=int(dimension[0])-1
    while row>=0:
        col= int(dimension[1])-1
        firstColumnBlank=position[1]+col
        while col>=0:
            if shape[row][column]==0:
                continue
            wall[lastRowBlank][firstColumnBlank]=shape[row][col]
            col=col-1
            firstColumnBlank=firstColumnBlank-1
        row=row-1
        lastRowBlank= lastRowBlank-1
        
        
    print(wall,end='\n',sep='\n')


    
for i in range(5):
    newBlock = input("enter the block u want to stack")         #next block to be stck in the wall
    shape, dimension= initialiseBlock(newBlock)                 #identifying the shape and size of the Block
    space, position = isBlankSpaceLeft(dimension)               #checking for the free space in the wall
    updateWall(shape,dimension,position)                        #stack the block in the wall

