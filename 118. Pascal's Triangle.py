#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it.
def generate(numRows):
    result = [] #the result is a list of list, with the number of list equals to numRows
    for i in range(0,numRows): #create numRows (in this case, 5) list in the result list
        result.append([])
        for j in range(0,i+1): #use (i+1) because the row would have i element
            if j in (0,i): #if this is the first and last element, it will be 1
                result[i].append(1)
            else: #if not, we take the sum of the second and third element of the last row
                result[i].append(result[i-1][j-1]+result[i-1][j])

    return print(result)

generate(7)