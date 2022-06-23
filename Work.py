import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    result=v
    p=1
    divide=v//(k**p)
    
    while divide>=1:
        result+=(divide)
        p+=1
        divide=v//(k**p)
    
    return result




# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    pass



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    lo = 0
    hi = 10 ** 6
    
    mid = 500000
    
    v = 1
    
    while lo != hi:
        if sum_series(mid, k) >= n:
            hi = mid
            v = mid
        else:
            lo = mid + 1
        
        mid = (lo + hi) // 2
        
    return v
            



def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":    
    main()
