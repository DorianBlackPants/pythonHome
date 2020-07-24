#Написать функцию которая будет простое число возводить в квардрат.
#
#Необходимо возвести в квадрат все простые числа в списке используя функцию map

def mult_1 (x):
    return x*x

list_1 = [i for i in range(1,24)]

for num in list_1:
    if num > 1:
        for i in range (2, num):
            if not num % i:
                break
        else:
            print(mult_1(num))

        
    

