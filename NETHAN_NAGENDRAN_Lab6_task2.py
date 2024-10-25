file = open('words.txt', 'r')
words = file.read().splitlines()
file.close()
print('Number of words read:', len(words))

def linear_search(arr, target):
    num_of_iterations = 0
    for i in range(len(arr)):
        num_of_iterations += 1
        if arr[i] == target:
            print(f'Target = {target}, Found at index = {i}, Number of iterations = {num_of_iterations}')
            return i
    print(f'Target = {target}, Found at index = -1, Number of iterations = {num_of_iterations}')
    return -1

target = input('Enter search key: ').lower()

while target != 'exit':
    linear_search(words, target)
    target = input('Enter search key: ').lower()


