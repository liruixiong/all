import random
import time

"""
a= 1
while a <= 11:
    a=random.randint(1,5)
    if a == 1:
        print(" *  *  *  *")
    elif a == 2:
        print("* *  *  *  *   *  ")
    elif a == 3:
        print(" *  *  *  *  *   *  ")
    elif a == 4:
        print(" * * * * * * *  * * *  *  ")
    elif a == 5:
        print("*  *  *  *  *  *  *  *  *  *")
    time.sleep(0.2)
    a+=1
"""


def a(b):
    num = random.randint(1, 12)
    snow = random.randint(1, 5)
    print(b * num, end='')
    print('❁' * snow)
    time.sleep(0.2)
    a(b)


a("\t")
