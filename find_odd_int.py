def find_odd_int(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Unit test
def test_find_odd_int():
    assert find_odd_int([2, 2, 3, 3, 4, 4, 4]) == 4
    assert find_odd_int([1, 1, 2, 2, 3, 3, 3]) == 3
    assert find_odd_int([5, 5, 5, 8, 8]) == 8
    assert find_odd_int([1, 2, 3, 1, 2, 3, 4, 4, 5]) == 5

if __name__ == "__main":
    test_find_odd_int()
    print("All tests passed!")

print(find_odd_int([7]))
print(find_odd_int([0]))  
print(find_odd_int([1, 1, 2]))  
print(find_odd_int([0, 1, 0, 1, 0]))  
print(find_odd_int([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  

