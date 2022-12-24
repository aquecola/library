thisset = {"apple", "banana", "cherry"}
thisset2 = ['melon', 'raspberry']
N=0
for new_list in thisset2:
    thisset.add(thisset2[N])
    if N==1:
        break
    else:
        N=N+1
    
print(thisset)