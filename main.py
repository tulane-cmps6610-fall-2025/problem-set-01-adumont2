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


