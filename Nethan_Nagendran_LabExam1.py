def ternary_search(ascending_arr, target):
    def search(left, right):
        if left > right:
            return -1
        
        #first third of the current search space.
        mid1 = left + (right - left) // 3
        #second third of the search space.
        mid2 = right - (right - left) // 3
        
        if ascending_arr[mid1] == target:
            return mid1
        if ascending_arr[mid2] == target:
            return mid2
        
        if target < ascending_arr[mid1]:
           #search in the left third.
            return search(left, mid1 - 1)
        elif target > ascending_arr[mid2]:
            #searches the right third
            return search(mid2 + 1, right)
        #if between mid1 and mid2, searches middle third
        else:
            #searches in the middle third
            return search(mid1 + 1, mid2 - 1)
    
    return search(0, len(ascending_arr) - 1)

print(ternary_search([1,4,5,6,7,8,9,11,17,202,231,333,339,443], 11))  
print(ternary_search([1,4,5,6,7,8,9,11,17,202,231,333,339,443], 111))
