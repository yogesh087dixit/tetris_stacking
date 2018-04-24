import numpy as np
from numpy import *

#grid for the representation of the wall

wall=np.zeros((8,8), dtype=int32)
print(wall)
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
        dimension = ['1','4']
    elif ord(newBlock) == ord('J'):
        shape = shapes["J"]
        dimension = ['1','3']
    elif ord(newBlock) == ord('L'):
        shape = shapes["L"]
        dimension = ['1','3']
    elif ord(newBlock) == ord('O'):
        shape = shapes["O"]
        dimension = ['2','2']
    elif ord(newBlock) == ord('S'):
        shape = shapes["S"]
        dimension = ['1','2']
    elif ord(newBlock) == ord('T'):
        shape = shapes["T"]
        dimension = ['1','3']
    elif ord(newBlock) == ord('Z'):
        shape = shapes["Z"]
        dimension = ['1','2']
    return shape, dimension


def isBlankSpaceLeft(dimension):
    #to check if the space is left in the row to stack the block

    #VARIABLES
    #wallRow* position of nth row in the wall
    #wallCols* position of nth column in the wall
    #flag* to get the position of first blank space
    #spaceLeft* Blank space left in the row
    #space2fill* contineous space in row
    #moreSpace* if the spaceLeft is more than that of the space2fill 
    #position* the posititon of the first blank space in the row

    
    

    wallRow=7                   #size of grid is 8*8, and the indexing is form 0
    while wallRow>=0:           #check for blank space till topmost line of the grid
        wallCols=0              
        flag=0
        space2fill=0
        spaceLeft=0             
        
        while wallCols<8:
            if wall[wallRow][wallCols]==0:   
                if flag==0:
                    position = [wallRow,wallCols]
                    flag=1
                space2fill = space2fill + 1    
                if wallCols!=7:
                    if wall[wallRow][wallCols+1]!=0:
                        break
            wallCols = wallCols + 1

        wallCols=0
        while wallCols<8:
            if wall[wallRow][wallCols]==0:   
                spaceLeft = spaceLeft + 1    
            wallCols = wallCols + 1

        if spaceLeft>space2fill:
            moreSpace= 1
        else:
            moreSpace= 0
        if spaceLeft<int(dimension[1]):
            wallRow=wallRow-1
            continue
        elif spaceLeft==0:
            wallRow=wallRow-1
            continue
        
        return moreSpace, space2fill, position
        
        #conditin for rotation will occur hare

def rotateShape(id, shape, moreSpace, space2fill, position):

    '''
    the function rotates the shape of the block
    VARIABLES:
    id* name of the shape of block
    times* no. of times the shape woud be rotated
    tos* try another shape
    '''

    wallRow = position[0]
    wallCols = position[1]
    
    def rotated(array_2d):
        #rotates the shape by 90 degree
        list_of_tuples = zip(*array_2d[::-1])
        return [list(elem) for elem in list_of_tuples]
        # return map(list, list_of_tuples)

    ornt1=1
    ornt2=1
    ornt3=1
    ornt4=1
    
    if id=='I':
        for i in range(4):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
        if ornt1==1:
            times=0
            tos=0
        elif ornt2==1:
            times=1
            tos=0
        else:
            times=0
            tos=1
            
    elif id=='J':
        for i in range(3):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            try:
                if wall[wallRow-1][wallCols - i] !=0:
                    ornt3 = 0
            except IndexError:
                ornt3=0
            try:
                if wall[wallRow -i][wallCols+1] !=0:
                    ornt4 = 0
            except IndexError:
                ornt4 = 0

        for i in range(2):
            try:
                if wall[wallRow-i][wallCols] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -2][wallCols+i] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            try:
                if wall[wallRow-i][wallCols] !=0:
                    ornt3 = 0
            except IndexError:
                ornt3=0
            try:
                if wall[wallRow][wallCols+i] !=0:
                    ornt4 = 0
            except IndexError:
                ornt4 = 0

            
                
        if ornt1==1:
            times=0
            tos=0
        elif ornt4==1:
            times=3
            tos=0
        elif ornt3==1:
            times=2
            tos=0
        elif ornt2==1 and position[1]!=6:
            times=1
            tos=0
        else:
            times=0
            tos=1
            
        
            
    elif id=='L':
        for i in range(3):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            try:
                if wall[wallRow-1][wallCols + i] !=0:
                    ornt3 = 0
            except IndexError:
                ornt3=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt4 = 0
            except IndexError:
                ornt4 = 0

        for i in range(2):
            try:
                if wall[wallRow-i][wallCols+2] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow][wallCols+i] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            try:
                if wall[wallRow-i][wallCols] !=0:
                    ornt3 = 0
            except IndexError:
                ornt3=0
            try:
                if wall[wallRow-2][wallCols-i] !=0:
                    ornt4 = 0
            except IndexError:
                ornt4 = 0

            
                
        if ornt1==1:
            times=0
            tos=0
        elif ornt2==1:
            times=1
            tos=0
        elif ornt3==1:
            times=2
            tos=0
        elif ornt4==1:
            times=3
            tos=0
        else:
            times=0
            tos=1


    elif id=='O':
        for i in range(2):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
        for i in range(2):
            try:
                if wall[wallRow-i][wallCols] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
        if ornt1==1:
            times=0
            tos=0
        else:
            times=0
            tos=1

    elif id=='S':
        for i in range(2):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            

        for i in range(2):
            try:
                if wall[wallRow-1][wallCols+i+1] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow-i-1][wallCols-1] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
        
                
        if ornt1==1 and position[1]!=5:
            times=0
            tos=0
        elif ornt2==1:
            times=1
            tos=0
        else:
            times=0
            tos=1



    elif id=='T':
        for i in range(3):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            try:
                if wall[wallRow-1][wallCols + i-1] !=0:
                    ornt3 = 0
            except IndexError:
                ornt3=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt4 = 0
            except IndexError:
                ornt4 = 0

        for i in range(2):
            try:
                if wall[wallRow-i][wallCols+1] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow-1][wallCols+i] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            try:
                if wall[wallRow-i][wallCols] !=0:
                    ornt3 = 0
            except IndexError:
                ornt3=0
            try:
                if wall[wallRow-1][wallCols-i] !=0:
                    ornt4 = 0
            except IndexError:
                ornt4 = 0

            
                
        if ornt1==1:
            times=0
            tos=0
        elif ornt4==1:
            times=3
            tos=0
        elif ornt3==1 and position[1]!=6:
            times=2
            tos=0
        elif ornt2==1 and position[1]!=6:
            times=1
            tos=0
        else:
            times=0
            tos=1


        

    elif id=='Z':
        for i in range(2):
            try:
                if wall[wallRow][wallCols + i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow -i][wallCols] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
            

        for i in range(2):
            try:
                if wall[wallRow-1][wallCols-i] !=0:
                    ornt1 = 0
            except IndexError:
                ornt1=0
            try:
                if wall[wallRow-i-1][wallCols+1] !=0:
                    ornt2 = 0
            except IndexError:
                ornt2 = 0
        
                
        if ornt1==1 and position[1]!=0:
            times=0
            tos=0
        elif ornt2==1 and position[1]!=6:
            times=1
            tos=0
        else:
            times=0
            tos=1
        


    for i in range(times):
        #rotates the shape n times
        shape=rotated(shape)

    #converet into numpy array       
    shape=reshape(shape, (len(shape),len(shape[0])))

    #removes the rows of zeros
    shape=shape[~np.all(shape == 0, axis=1)]

    #removes the columns of zeros
    if times==(1) or times ==3:
        if id=='I':
            shape=shape[0:,0]
            shape=shape.reshape(4,1)
        elif times==1:
            shape=shape[:,:-1]
            shape=shape.reshape(3,2)
        elif times==3:
            shape=shape[:,1:]
            shape=shape.reshape(3,2)
            
    return shape, tos, times

          
def updateWall(id,shape,position,times):
    #stack the block in the wall

    #VARIABLES
    #lastRowBlank* lowest blank row in the column
    #firstaColumnBlank* first blank column in the row 
    #row* no of rows in the block
    #col* no of col in the block


    lastRowBlank = position[0]
    row=shape.shape[0]-1
    
    while row>=0:                   #conditions for the starting position in the wall to update the block
        col= shape.shape[1]-1
        if id=='J' and times==2:
            firstColumnBlank=position[1]+col-2
        elif id=='T' and times==2:
            firstColumnBlank=position[1]+col-1
        elif id=='L' and times==3:
            firstColumnBlank=position[1]+col-1
        elif id=='T' and times==3:
            firstColumnBlank=position[1]+col-1
        elif id=='S' and times==1:
            firstColumnBlank=position[1]+col-1
        elif id=='Z' and times==0:
            firstColumnBlank=position[1]+col-1
        else:
            firstColumnBlank=position[1]+col
        while col>=0:
            wall[lastRowBlank][firstColumnBlank]=wall[lastRowBlank][firstColumnBlank]^shape[row][col]
            col=col-1
            firstColumnBlank=firstColumnBlank-1
        row=row-1
        lastRowBlank= lastRowBlank-1
        
        
    print(wall,end='\n',sep='\n')

def main(visibleBlocks):
    while len(visibleBlocks)!=0:
        newBlock = visibleBlocks[0]         #next block to be stck in the wall
        shape, dimension= initialiseBlock(newBlock)                 #identifying the shape and size of the Block
        moreSpace, space2fill, position = isBlankSpaceLeft(dimension)        #checking for the free space in the wall
    
        if space2fill<int(dimension[0]):        #if the space is less than the required space check for the another block
            visibleBlocks.append(visibleBlocks[0])
            visibleBlocks.pop(0)
            continue
        shape, tos, times = rotateShape(newBlock, shape, moreSpace, space2fill, position)
        if tos == 1:
            visibleBlocks.append(visibleBlocks[0])
            visibleBlocks.pop(0)
            continue
        updateWall(newBlock,shape,position,times)                        #stack the block in the wall
        visibleBlocks.pop(0)                #pop the used block



stacked=0;                              #no. of blocks stacked
visibleBlocks=[]                        #identified blocks
while(stacked<28):
    visible=int(input("how many shapes are visible to u"))      #no. of identified blocks
    if visible>(28-stacked):
        print("only ",28-stacked," blockes can be stacked")
        continue
    while len(visibleBlocks)!=visible:
        visibleBlocks.insert(0,input("nameof blocks"))
        if visibleBlocks[0]!='I' and visibleBlocks[0]!='J' and visibleBlocks[0]!='L' and visibleBlocks[0]!='O' and visibleBlocks[0]!='S' and visibleBlocks[0]!='T' and visibleBlocks[0]!='Z':
            visibleBlocks.pop(0)
            print('can not identify the block. please, enter again')
        continue;
    main(visibleBlocks)
    stacked=stacked+visible
