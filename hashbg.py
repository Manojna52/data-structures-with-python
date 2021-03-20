freq=dict()
t=0
for i in range(0,5):
    x=input()
    t=hash(x)%1000
    if t not in freq:
        freq[t]=1
    else:
        print("loop found")
print(freq)
    
