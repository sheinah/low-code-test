from itertools import permutations

def get_permutations(input_str):
    # Get all permutations of the input string
    all_permutations = set(permutations(input_str))

    # Convert permutations to strings and remove duplicates
    unique_permutations = [''.join(p) for p in all_permutations]

    return unique_permutations

# Example usage:
input_str = "abc"
permutations_list = get_permutations(input_str)
for perm in permutations_list:
    print(perm)

# Example usage2:
input_str = 'a'
print(get_permutations(input_str))

input_str = 'ab'
print(get_permutations(input_str))

input_str = 'abc'
print(get_permutations(input_str))

input_str = 'aabb'
print(get_permutations(input_str))

import unittest

class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        input_str = "abc"
        expected_permutations = ["abc", "acb", "bac", "bca", "cab", "cba"]
        result = get_permutations(input_str)
        self.assertEqual(sorted(result), sorted(expected_permutations))

if __name__ == '__main__':
    unittest.main()

