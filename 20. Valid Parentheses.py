s = '([)))'

mymap = {')':'(', ']':'[', '}':'{'} #make a map for easier look up. The reason you want the close parentheses to be
                                    #the key is to look up the value and check against the last item in the stack

stack = [] #make an empty stack
for char in s: #go through each character of the string
    if char in mymap.values(): #if it is a open parentheses, we add it to the stack
        stack.append(char)
    elif char in mymap.keys(): #if it is a close parentheses
        if stack == [] or mymap[char] != stack.pop(): #check if the stack is empty, and check if the close parentheses goes with corresponding open parentheses
            print("False")
    else:
        print("False")
