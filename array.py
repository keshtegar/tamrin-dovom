#array
import random
n=int(input( "لطفا طول ارایه را وارد کنید : " ))
start=int(input("لطفا ابتدای یازه را وارد کنید : "))
end=int(input("لطفا انتهای بازه را وارد کنید : "))

numbers = random.sample(range(start, end), n)
print(numbers)
