#linear search
l=[2,0,5,3,7,6]
l.sort()
s=6
for i in range(len(l)):
    if l[i]==s:
        print(i)
        break
else:
    print(-1)

#binary search
l=[5,2,9,7,1,35,20,18,13,3]
l.sort()
print(l)  
ll,hh=0,len(l)-1
s=int(input('enter a number to serach'))
pos=0
while ll<=hh:
    pos=int(ll+((hh-ll)/(l[hh]-l[ll]))*(s-l[ll]))
    if l[pos]<s:
        ll=pos+1
    elif l[pos]>s:
        hh=pos-1
    else:
        print(pos

              )
        break
else:
    print(-1)
#Bubble sort
l=[5,2,9,7,1,35,20,18,13,3]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
#selection sort
l=[5,2,9,7,1,35,20,18,13,3]
for i in range(len(l)-1):
    min=i
    for j in range(i+1,len(l)):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
print(l)
















