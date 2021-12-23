"""
14. Write a Python program to calculate 
number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
"""
# a=(2014,7,2)

# b=(2014,7,11)

# diffdate= a[-1]-b[-1]
# print(diffdate)

#lets try another method

from datetime import date
lastdate = date  (2015,8,11)
firstdate = date (2014,7,2)
diff = lastdate - firstdate

print(diff.days) # gets only day
