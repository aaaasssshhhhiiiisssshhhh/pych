n = int (input("enter a number :"))

def nearthousand (n):
    return ((1000-n)<=100 or ((2000-n)<=100))
print(nearthousand(n))
    