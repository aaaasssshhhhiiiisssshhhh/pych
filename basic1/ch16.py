'''
16. Write a Python program to get the 
difference between a given number and 17,
if the number is greater than 17 return 
double the absolute difference.

'''

# a = int (input("enter a number:"))
# b =17 

# if a > b:
#     diff= a-b
#     print (diff*2)
# else:
#     diff= a-b 
#     print(diff )    


#lets try next method using function:
n = int (input ("enter a number:"))
def difference(n):
    if n <= 17:
        return 17-n
    else:
        return (n-17)*2
    
print (difference(n))    
    