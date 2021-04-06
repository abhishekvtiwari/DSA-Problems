import array as ar
arr = ar.array('i',[2,7,5])
l = list(arr)
s = list()
for i in range(len(l)):
    for j in range(i,len(l)+1):
        p = (l[i:j])
        if p not in s and p!=[]:
          s.append(p)

print(*s)