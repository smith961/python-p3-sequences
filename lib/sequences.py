#!/usr/bin/env python3
f_list = []

def print_fibonacci(length):
    pass
    fib_list = [0,1]
    index_1 = 0
    index_2 = 1
    if(length == 1):
        print([0])
    elif(length == 0):
         print([])
    else:
            while (index_2 <= length - 2):
                new_num = fib_list[index_1] + fib_list[index_2]
                fib_list.append(new_num)
                index_1 +=1
                index_2 +=1
            print(fib_list)