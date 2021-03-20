
li=[chr(i) for i in range(97,123)]
x=input()
for i in range(0,len(x)):
    if x[i] in li:
        li.remove(x[i])
print("".join(li))
