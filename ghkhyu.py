x=input().split()
freq=dict()
for item in x:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)
