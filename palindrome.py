# Checking the palindrome
# Check a given string $s$. If the string reads the same forwards and backwards (a palindrome), return True; otherwise, return False.
# Example: "racecar" → palindrome, because it reads the same in both directions.
def palindrom(s):
    check = s[::-1]
    if check == s:
        return True
    else:
        return False
# As we know from my last repo we can use the slicing method in this task to reverse the given object.
# And in any list or touple... the items are indexsed from 0 to infinity but the have 2nd hidden index which starts is from minus 1
# it's like starting from the end of the list from -1 then -2 then -3 ..... and [::-1] is can be translated as start slicing the object from the end to start.
