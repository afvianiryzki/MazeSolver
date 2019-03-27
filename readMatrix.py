import sys


def generateMatrix(file):
    infile = open(file).read()
    number = [item for item in infile.split('\n')]

    matrix = []
    for line in number:
        el = []
        for element in line:
            el.append(int(element))
        matrix.append(el)

    return matrix

def searchStartEnd(matrix, row, col):
    start = []
    end = []

    count = 0

    for x in range(row):
        if (matrix[x][0] == 0):
            if(count == 0):
                start.append(x)
                start.append(0)
                count += 1
            elif(count == 1):
                end.append(x)
                end.append(0)
        if(matrix[x][row-1] == 0):
            if(count == 0):
                start.append(x)
                start.append(row-1)
                count += 1
            elif (count == 1):
                end.append(x)
                end.append(row-1)
    
    for x in range(col):
        if (matrix[0][x] == 0):
            if(count == 0):
                start.append(0)
                start.append(x)
                count += 1
            elif(count == 1):
                end.append(0)
                end.append(x)
        if(matrix[col-1][x] == 0):
            if(count == 0):
                start.append(col-1)
                start.append(x)
                count += 1
            elif(count == 1):
                end.append(col-1)
                end.append(x)

    return start, end






