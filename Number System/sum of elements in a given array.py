# Function to return sum of 
# elements in an array
def sum_array(arr):
    total = 0  # initialize sum
    
    # Iterate through all elements
    # and add them to total
    for num in arr:
        total += num
    return total

# Driver code
arr = [12, 3, 4, 15]
print("Sum of given array is", sum_array(arr))