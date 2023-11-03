import random


def find_odd_int(arr):
    """Given an array of integers, find the one that appears an odd number of times.
    Note: This function works in linear time (except for sorted which is O(n logn), 
    and works for negative and positive integers and zero.
    """
    if len(arr) == 0:
        return None
    
    # Track both positive and negative results
    result_negative = 0
    result_positive = 0
    zero_count = 0

    result = 0
    for num in sorted(arr):
        # Handle the zero case separately
        if num == 0:
            zero_count += 1
            continue

        # use bitwise XOR ^= to flip the bits
        # cleverly, this will flip back and forth between 0 and the number,
        # leaving the result as the number which appears an odd number of times
        if num < 0:
            result_negative ^= -num
        else:
            result_positive ^= num

    # If zero repeats an odd number of times, return 0
    if zero_count % 2 != 0:
        return 0

    if result_negative > 0:
        # Restore the negative sign
        return -result_negative
    elif result_positive > 0:
        return result_positive
    else:
        # This is stated to be impossible but I want to handle this corner case anyway
        raise AssertionError("No integer repeats an odd number of times in the array.")


def get_random_array(num_pairs=50, min_i=-100, max_i=100):
    assert min_i < max_i
    # Create an array of 50 random integers from -100 to 100
    half_array = [random.randint(min_i, max_i) for _ in range(num_pairs)]
    # Add all the elements again so they all appear an even number of times
    full_array = half_array * 2
    # Add one more integer to make it the winner
    if len(full_array) > 0:
        winner = full_array[0]
        full_array.append(winner)
        # Shuffle it
        random.shuffle(full_array)
        return full_array, winner
    else:
        return [], None

# Unit test
def test_find_odd_int():
    assert find_odd_int([2, 2, 3, 3, 4, 4, 4]) == 4
    assert find_odd_int([1, 1, 2, 2, 3, 3, 3]) == 3
    assert find_odd_int([5, 5, 5, 8, 8]) == 8
    assert find_odd_int([1, 2, 3, 1, 2, 3, 4, 4, 5]) == 5

    # Run many test cases
    for i in range(100):
        full_array, winner = get_random_array(num_pairs=random.randint(0, 500))
        # print(f"CHECKING {full_array} against {winner}")
        if winner is None:
            assert find_odd_int(full_array) is None
        else:
            assert find_odd_int(full_array) == winner

if __name__ == "__main__":
    print("Running tests...")
    test_find_odd_int()

    assert find_odd_int([7]) == 7
    assert find_odd_int([0]) == 0
    assert find_odd_int([1, 1, 2]) == 2
    assert find_odd_int([0, 1, 0, 1, 0]) == 0
    assert find_odd_int([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]) == 4

    print("All tests passed!")

print(find_odd_int([7]))
print(find_odd_int([0]))  
print(find_odd_int([1, 1, 2]))  
print(find_odd_int([0, 1, 0, 1, 0]))  
print(find_odd_int([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  

