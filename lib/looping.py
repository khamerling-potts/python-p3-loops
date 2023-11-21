#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    sq_list = [num ** 2 for num in int_list]
    return sq_list

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print ("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
