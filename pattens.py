
#1
n=5
stars=1
for i in range(n):
    for j in range(stars):
        print('*',end='')
    print()
    stars+=1
#2
n=5
stars=1
sp=n-1
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('*',end='')
    print()
    sp-=1
    stars+=1
#3
n=5
stars=5
for i in range(n):
    for j in range(stars):
        print('*',end='')
    print()
    stars-=1
#4
n=5
stars=5
sp=0
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('*',end='')
    print()
    sp+=1
    stars-=1
#5
n=5
stars=1
sp=0
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('*',end=' ')
    print()
    sp+=1
#6
n=5
stars=1
sp=n-1
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('*',end=' ')
    print()
    sp-=1
#7
n=5
stars=1
sp=0
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('A',end=' ')
    print()
    sp+=1
#8
n=5
stars=1
sp=n-1
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('M',end=' ')
    print()
    sp-=1
#9
n=5
stars=1
for i in range(n):
    for j in range(stars):
        print('A',end='')
    print()
    stars+=1
#10
n=5
stars=1
sp=n-1
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('B',end='')
    print()
    sp-=1
    stars+=1
#11
n=5
stars=5
for i in range(n):
    for j in range(stars):
        print('C',end='')
    print()
    stars-=1
#12
n=5
stars=5
sp=0
for i in range(n):
    for l in range(sp):
        print(' ',end='')
    for j in range(stars):
        print('D',end='')
    print()
    sp+=1
    stars-=1
#13
n=5
stars=1
dummy=ord('A')
for i in range(n):
    for j in range(stars):
        print(chr(dummy),end='')
        dummy+=1
    print()
    stars+=1
#14
n=5
stars=1
sp=n-1
dummy=ord('A')
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(chr(dummy),end='')
        dummy+=1
    print()
    stars+=1
    sp-=1
#15
n=5
stars=5
dummy=ord('A')
for i in range(n):
    for j in range(stars):
        print(chr(dummy),end='')
        dummy+=1
    print()
    stars-=1
#14 and 16
n=5
stars=1
sp=n-1
dummy=ord('A')
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(chr(dummy),end='')
        dummy+=1
    print()
    stars+=1
    sp-=1
#17
n=5
stars=1
dummy=1
for i in range(n):
    for j in range(stars):
        print(dummy,end='')
    print()
    stars+=1
#18
n=5
stars=1
sp=n-1
dummy=2
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
    print()
    stars+=1
    sp-=1
#19
n=5
stars=5
dummy=3
for i in range(n):
    for j in range(stars):
        print(dummy,end='')
    print()
    stars-=1
#20
n=5
stars=5
dummy=4
sp=0
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
    print()
    stars-=1
    sp+=1
#21
n=5
stars=1
for i in range(n):
    dummy=1
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    print()
    stars+=1
#22
n=5
stars=1
sp=n-1
for i in range(n):
    dummy=1
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    print()
    stars+=1
    sp-=1
#23
n=5
stars=5
for i in range(n):
    dummy=1
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    print()
    stars-=1
#24
n=5
stars=5
sp=0
for i in range(n):
    dummy=1
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    print()
#25
n=5
stars=1
dummy=1
for i in range(n):
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    stars+=1
    print()
#26
n=5
stars=1
dummy=1
sp=n-1
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    stars+=1
    sp-=1
    print()
#27
n=5
stars=5
dummy=1
sp=0
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    stars-=1
    sp+=1
    print()
#28
n=5
stars=5
dummy=1
for i in range(n):
    for j in range(stars):
        print(dummy,end='')
        dummy+=1
    stars-=1
    print()
#29
n=5
stars=1
dummy=ord('A')
for i in range(n):
    for j in range(stars):
        print(chr(dummy),end='')
    dummy+=1
    stars+=1
    print()
#30
n=5
stars=1
dummy=ord('A')
sp=n-1
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(chr(dummy),end='')
    dummy+=1
    stars+=1
    sp-=1
    print()
#31
n=5
stars=5
dummy=ord('A')
for i in range(n):
    for j in range(stars):
        print(chr(dummy),end='')
    dummy+=1
    stars-=1
    print()
#32
n=5
stars=5
dummy=ord('A')
sp=0
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(chr(dummy),end='')
    dummy+=1
    stars-=1
    sp+=1
    print()
#33
n=5
stars=1
dummy=1
for i in range(n):
    for j in range(stars):
        print(dummy,end='')
    dummy+=1
    stars+=1
    print()
#34
n=5
stars=1
dummy=1
sp=n-1
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
    dummy+=1
    stars+=1
    sp-=1
    print()
#35
n=5
stars=5
dummy=1
for i in range(n):
    for j in range(stars):
        print(dummy,end='')
    dummy+=1
    stars-=1
    print()
#36
n=5
stars=5
dummy=1
s=0
for i in range(n):
    for k in range(sp):
        print(' ',end='')
    for j in range(stars):
        print(dummy,end='')
    dummy+=1
    stars-=1
    sp+=1
    print()

