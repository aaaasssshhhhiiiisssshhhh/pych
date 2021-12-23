'''
10. Write a Python program that accepts an 
integer (n) and computes the value of n+nn+nnn
'''

# n = int (input("enter the value:"))
# value = n+n*n+n*n*n
# print(value)
#Not this way

#like this way
#  """
#     5
#     55
#     555
#     |
#     |
#     |
    
#     5+55+555
    
#     615
    
#  """

num = int (input ('enter a value:'))
num1= int ("%d" %num)
num2 = int ("%d%d" %(num, num))
num3 = int ("%d%d%d" %(num,num,num))
sum = num1+num2+num3
print(sum )