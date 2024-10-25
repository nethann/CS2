file = open('words.txt', 'r')
words = file.read().splitlines()
file.close()
print('Number of words read:', len(words))

def binary_search(arr, target):
    low_val = 0
    high_val = len(arr) - 1


    iteration_count = 0
    
    while low_val <= high_val:
        iteration_count += 1
        mid = (low_val + high_val) // 2
        if arr[mid] == target:
            print(f'Target = {target}, Found at index = {mid}, Number of iterations = {iteration_count}')
            return mid
        elif arr[mid] < target:
            low_val = mid + 1
        else:
            high_val = mid - 1
    
    print(f'Target = {target}, Found at index = -1, Number of iterations = {iteration_count}')
    return '-1'

target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()



