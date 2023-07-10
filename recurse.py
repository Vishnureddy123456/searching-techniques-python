#special numbers
def fact(a):
    if a==0:
        return 1
    return a*fact(a-1)
def spe(n):
    if n==0:
        return 0
    return fact(n%10)+spe(n//10)
n=145
num=n
b=spe(n)
if b==num:
    print('spe')
else:
    print('not spe')



#adding two lists
a=[1,9,6,8,3,5,2]
a.sort()
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e,o)
if len(e)>len(o):
    
    print(e)
else:
    
    print(o)
        
                                                                    
    
    
