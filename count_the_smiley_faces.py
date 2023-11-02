import re

def countSmileys(arr):
    if not arr:
        return 0
    
    """Count the number of smilies in a list of strings"""
    assert type(arr) == list, "arr must be list"
    assert all([type(s) == str for s in arr]), "all elements of arr must be strings"

    # Define a regular expression pattern to match valid smiley faces
    pattern = r"[:;][-~]?[)D]"

    # Use the re.findall() function to find all matches in the array
    matches = re.findall(pattern, ' '.join(arr))

    # Return the count of valid smiley faces
    return len(matches)

# Example test cases, including the case of an empty array
print(countSmileys([]))
print(countSmileys([':)', ';(', ';}', ':-D']))
print(countSmileys([';D', ':-(', ':-)', ';~)']))
print(countSmileys([';]', ':[', ';*', ':$', ';-D']))


# Example test cases, including the case of an empty array
assert countSmileys([]) == 0
assert countSmileys([":)", ";(", ";}", ":-D"]) == 2
assert countSmileys([";D", ":-(", ":-)", ";~)"]) == 3
assert countSmileys([";]", ":[", ";*", ":$", ";-D"]) == 1
assert countSmileys([";]", ":[", ";*", ":$", ";-D"]) == 1
assert countSmileys([";]", ":[", ";*", ":$", ";-D", "wefwe", "df", ""]) == 1
assert countSmileys([";", "df", "", ")))))))))))))))))", ";;", "(:"]) == 0

# Check the assertions
try:
    countSmileys(":)")
except AssertionError as _:
    pass
else:
    raise AssertionError("Bad input accepted")

try:
    countSmileys([":)", 220])
except AssertionError as _:
    pass
else:
    raise AssertionError("Bad input accepted")

