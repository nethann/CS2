#task 1
def is_power_of_two(num):
    if num == 1:
        return True
    elif num == 0 or num % 2 != 0:
        return False
    else:
        return is_power_of_two(num // 2)

#task 2
def tribonacci(n, memorization_dictionary={}):
    if n in memorization_dictionary:
        return memorization_dictionary[n]
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memorization_dictionary[n] = tribonacci(n - 1, memorization_dictionary) + tribonacci(n - 2, memorization_dictionary) + tribonacci(n - 3, memorization_dictionary)
        return memorization_dictionary[n]
#Outputs

#task 1 outputs
print("task 1 output")
print(is_power_of_two(5))  
print(is_power_of_two(4)) 
print(is_power_of_two(16)) 
print(is_power_of_two(1)) 
print(is_power_of_two(-4)) 

print("\n")

#task 2 outputs
print("task 2 output")
print(tribonacci(0))  
print(tribonacci(1))  
print(tribonacci(2))  
print(tribonacci(6)) 
print(tribonacci(10))
print(tribonacci(33)) 
