#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(num):
  if int(num) == float(num):
    return True
  else:
    return False
  
