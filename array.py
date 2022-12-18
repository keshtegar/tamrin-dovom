#array
import random
n=int(input( "لطفا طول ارایه را وارد کنید : " ))
m=[]

for i in range(n):
    numbers=random.randint(0,n+1)
    m.append(numbers)
print(m)

