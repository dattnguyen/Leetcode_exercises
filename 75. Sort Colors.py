# Given an array with n objects colored red, white or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

#red : 0, white : 1, blue : 2
#we need three pointers, the red one goes from left to right,
#only go forward if anything on its left is in correct order
#the blue one goes from right to left, only go backward if anything on
#its right is in correct order

def sortColors(arr):
    red, white, blue = 0, 0, len(arr)-1

    while white <= blue: #red is left pointer, blue is right pointer
                         #white is the moving pointer
        if arr[white] == 0: #if you see '0', you swap the numbers at position white and red
                            #and move both pointers because left of red is now in correct order ('0')
            arr[white], arr[red] = arr[red], arr[white]
            white += 1
            red += 1

        elif arr[white] == 2: #if you see '2', swap the numbers
            arr[white], arr[blue] = arr[blue], arr[white]
            blue -= 1

        else:
            white += 1 #if you see '1', move forward because you don't need to swap its place

    return print(arr)
sortColors([2,0,1])





arr = [1,2,0,2,1,1,2,2,1,0]

