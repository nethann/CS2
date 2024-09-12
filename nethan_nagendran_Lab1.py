def max_of_list(list):
    max_value_in_list = list[0]
    
    # finding the max val in list
    for number in list:
        if number > max_value_in_list:
            max_value_in_list = number
    
    return max_value_in_list

#output for part 1
print(max_of_list([5,4,3,6,7]))

def sum_of_list(list):
    sum = 0  #setting sum to 0
    
    #looping through elements in list
    for numbers in list:
        sum += numbers
    
    return sum

#output for part 2
print(sum_of_list([10,20,30,40,50]))


# List of numbers from 10 to 20 
list1 = [i for i in range(10, 21)]
print(list1)

#list jumping from 10
list2 = [i for i in range(10, 101, 10)]
print(list2)

# list substracting by 10
list3 = [i for i in range(100, 9, -10)]
print(list3)
