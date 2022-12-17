import random
pc_number=random.randint(0, 20)
count=0
while True:
    user_number=int(input("enter number: "))
    if pc_number==user_number:
        print("you win")
        print("count= ", count)
        break
    elif pc_number>user_number:
        print("boro balatar")
        count=count+1
    elif pc_number<user_number:
        print("boro payintar")
        count=count+1
