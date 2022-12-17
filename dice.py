#dice and prize


import random

dice = random.randint(1, 6)
prize_dice = random.randint(1, 6)
while True:
    if dice != 6:
        print("Dice number= ", dice)
        break

    elif dice == 6:
        print("Dice number= ", dice)
        print("شما برنده شدید و میتوانیذ تاس را دوباره پرتاب کنید ")
        print("second Dice number= ", prize_dice)
        break

