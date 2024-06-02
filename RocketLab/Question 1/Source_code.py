#using Time module for logging the time
import time

'''
we can perform a binary search over the entire matrix.
treating matrix as a one-dimensional sorted list and use index manipulation to access the two-dimensional matrix.
'''

def search_in_matrix(matrix, target):

    #time before algorithm execution
    start_time = time.time()
    print(start_time)

    #Validating the Matrix
    if not matrix or not matrix[0]:
        return False

    #No. of Rows and Columns
    rows = len(matrix)
    cols = len(matrix[0])

    #left and right pointer
    left, right = 0, rows * cols - 1
    
    #A while Loop as left point is not equal to right pointer
    while left <= right:
        
        #calulating the middle index and retriving the corresponding value in the matrix
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        # if middle value is the targeted value, then returning True and calculating total execution time.
        if mid_value == target:
            end_time = time.time()
            print(end_time)
            execution_time = (end_time - start_time) * 1e6
            #print(execution_time)
            print(f"Total Execution Time: {execution_time: .2f} Microseconds")
            return True
        
        # if the middle value is less than the target, the left pointer right of the middle value
        elif mid_value < target:
            left = mid + 1
            
        # otherwise moving right pointer to the left of the middle value
        else:
            right = mid - 1
    
    end_time = time.time()
    print(end_time)
    execution_time = (end_time - start_time) * 1e6
    print(f"Total Execution Time: {execution_time: .2f} Microseconds")
    return False

if __name__ == "__main__":
    search_in_matrix()
