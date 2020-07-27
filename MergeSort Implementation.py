def merge(A, left, middle, right): #example [4,2,3,7,8,3,1]. left = 0, right = 7-1 =6. middle = (0+6)//2 =3
    n1 = middle - left + 1 #middle is at 3, we +1 to account for the first index starting at 0
    n2 = right - middle
    L = [0] * n1 #create empty arrays
    R = [0] * n2

    #copy data to temp arrays L and R
    for i in range (0, n1):
        L[i] = A[left+i]

    for j in range (0, n2):
        R[j] = A[middle+1+j] #starting at middle. We +1 to move to the next element

    #return print('L is: ', L, '\n', 'R is: ', R)

    #merge the temp arrays using two pointer technique

    i = 0 #initial pointer of L
    j = 0 #initial pointer of R
    k = left #initial pointer of merged subarray

    while i < n1 and j < n2:
    #use 'and' in the case of L[2,3,4] and R[7,8,9]
    #once i reached 2, j is still 0, we copy over element in R to the subarray
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    #copy the remaining elements of L and R if any
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort(A, first, middle)
        merge_sort(A, middle+1, last)
        merge(A, first, middle, last)

    return A
merge_sort([4,2,3,7,8,3,1],0,6)