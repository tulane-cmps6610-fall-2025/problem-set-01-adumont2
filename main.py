"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        x, y = (min(a, b), max (a, b))
        return foo (y, y % x)


def longest_run(myarray, key):
    """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
    """
    current_run = 0
    longest_run = 0
    for item in myarray:
        if item == key:
            # If we find the key, we're in a run. Increment the current counter.
            current_run += 1
            # Use the max() function to update longest_run if necessary.
            # This is a concise way to write an if statement that updates longest_run
            # only if current_run is greater. Could also compare current_run to longest_run
            # with an if statement and update longest_run inside the if block if current_run > longest_run.
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0
    return longest_run



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    #Base case: If the list is empty or has one element, we can solve it directly.
    if len(mylist) <=1:
        if len(mylist) == 1 and mylist[0] == key:
            # A list of one element that matches the key has a longest run of 1.
            return Result(1, 1, 1, True)
        else:
            #Empt list or a list with one element that doesn't match the key has longest run of 0.
            return Result(0, 0, 0, False)
    
    #Recursive case: 
    # Divide: Split the list in half and solve each half recursively.
    mid = len(mylist) // 2
    left_half = mylist[:mid]
    right_half = mylist[mid:]

    #Conquer: Solve each half recursively.
    left_result = longest_run_recursive(left_half, key)
    right_result = longest_run_recursive(right_half, key)

    #Combine: Combine the results from the two halves to solve the original problem.

    #Calculate the combined left_size.
    combined_left_size = left_result.left_size
    if left_result.is_entire_range and len(left_half) > 0:
        combined_left_size += right_result.left_size
    
    #Calculate the combined right_size.
    combined_right_size = right_result.right_size
    if right_result.is_entire_range and len(right_half) > 0:
        combined_right_size += left_result.right_size
    
    #Calculate the longest run that could cross the midpoint.
    cross_midpoint_run = left_result.right_size + right_result.left_size

    # The new longest run is the max of the longest in the left, the longest in the right,
    # and the one that crosses the middle.
    combined_longest_size = max(left_result.longest_size, right_result.longest_size, cross_midpoint_run)

    # The entire range is the key only if both sub-ranges are.
    combined_is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    return Result(combined_left_size, combined_right_size, combined_longest_size, combined_is_entire_range)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

def test_longest_run_recursive():
    print("\n--- Running tests for longest_run_recursive ---")

    # Test Case 1: The example from the problem
    array1 = [2,12,12,8,12,12,12,0,12,1]
    key1 = 12
    result1 = longest_run_recursive(array1, key1)
    
    # We check the .longest_size attribute of the result object
    assert result1.longest_size == 3
    # Let's also check the other attributes for this case
    assert result1.left_size == 0 # Run does not start at the beginning
    assert result1.right_size == 0 # Run does not end at the end
    assert result1.is_entire_range == False
    print("Test 1 PASSED")

    # Test Case 2: Run at the end
    array2 = [1, 2, 5, 5, 5, 5]
    key2 = 5
    result2 = longest_run_recursive(array2, key2)
    assert result2.longest_size == 4
    assert result2.right_size == 4
    print("Test 2 PASSED")

    # Test Case 3: Empty array
    array3 = []
    key3 = 6
    result3 = longest_run_recursive(array3, key3)
    assert result3.longest_size == 0
    print("Test 3 PASSED")

    # Test Case 4: The entire array is a run
    array4 = [7, 7, 7, 7]
    key4 = 7
    result4 = longest_run_recursive(array4, key4)
    assert result4.longest_size == 4
    assert result4.left_size == 4
    assert result4.right_size == 4
    assert result4.is_entire_range == True
    print("Test 4 PASSED")

    print("\nAll recursive tests passed successfully!")

# Call to new test function in the main execution block
if __name__ == "__main__":
    # You can test both functions at once if you like
    # test_longest_run() 
    test_longest_run_recursive()
