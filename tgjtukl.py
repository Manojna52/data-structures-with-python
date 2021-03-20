x=input().split()
y=input().split()

ex1=set(x)
ex2=set(y)

if len(ex1&ex2)==len(ex2):
    print("Yes")
else:
    print("No")
