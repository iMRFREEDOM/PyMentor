# [PyMentor]
# 20.10.2026
# Write a function that reverses the given word 
# E.g Hello --> olleH

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def reversed_line(s):
    check = s[::-1] # Here we reverse the argument with opposite slicing 
    return check
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Slicing is grat thing if you need to cut things like: Touples, Strings, Lists....
# To slice something you need just write the name of the thing you want to slice and give the starting point and ending point. X[Starting point, Ending point] E.g: A = (1,2,3,4,5,6,7,8) A[1,5] => 1,2,3,4
# Notice how the last element is not involved
# Sometimes you need to slice things and let some parts of it just let go.So you can use the EXACT same slicing with steps.X[Starting point, Ending point, Steps] E.g: A = (1,2,3,4,5,6,7,8) A[1,7,2] => 1,3,5
# Notice how the last element is not involved here 😅
# If this was really helpful don't forget to comment and give some stars :)
