# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end of the string to hold the
# additional characters, and that you are given the "true" length of the string.
# Do it in place.
# Input: "Mr 3ohn Smith"
# Output: "Mr%203ohn%20Smith" 
import re

def URLify(s):
    arr = re.split("\\s+", s)
    result = ""
    for c in arr:
        result += c
        result += '02%'
    return result.strip('02%')

def URLify2(s):
    return re.sub('\\s+', '02%', s)


if __name__ == "__main__":
    c = "le hong   phong"
    print(URLify2(c))