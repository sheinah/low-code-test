import re

def countSmileys(arr):
    if not arr:
        return 0

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
