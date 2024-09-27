import time

def num_paths(m, n):
    # Create a 2D list to store the number of paths at each grid cell
    dp = [[1]*n for _ in range(m)]
    
    # Iterating through the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

def num_paths_memo(m, n):
    # Memoization dictionary
    memorization_dictionary = {}

    # Creating a 2D grid to store the number of paths
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1:
                memorization_dictionary[(i, j)] = 1 
            else:
                memorization_dictionary[(i, j)] = memorization_dictionary[(i-1, j)] + memorization_dictionary[(i, j-1)]  
                
    return memorization_dictionary[(m, n)]

#driver code - you do not need to make any changes after this line.
#However, submit a screenshot of the output to report the execution time/elapsed time.
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")
