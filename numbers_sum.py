# 25.10.2026
# PyMentor
# Numbers' Sum
# Find the number's sum for given N positive number

# ////////////////////////////////////////////////////////////////////////////////////////////////
def numbers_summ(n):
    summ = 0
    while n > 0:
        summ += n % 10 
        n = n // 10    
    return summ 
# ///////////////////////////////////////////////////////////////////////////////////////////////
  
# In this question
# We need to find the number's summ for given N positive number
# Extract the last digit: Take the remainder of the number when divided by 10 (number % 10).
# Add it to the total sum. Remove the last digit: Divide the number by 10 using integer division (number // 10).
# Repeat steps 1–3 until the number becomes 0

# Here we are using 2 types of dividing numbers in python which is % and //
# The % can divide your number and take only residue number 
# E.g: 139 % 10 --> 9
# Because when you divide 139 by 10 you get 13 and 9 residue
# It's not that complicated
# The second divider is // it can divide things and take only whole part of the number
# E.g: 139 // 10 --> 13
# It's really like & but the opposite one
