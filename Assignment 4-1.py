#Exercise 1

from re import X

from sqlalchemy import true


def func():
    print('Hello World')

func()

#Exercise 2

def func1(name):
    print(f"Hi My name is {name}")

func1('Dan')

#Exercise 3

def func3(x,y,z):
    if z:
        return x
    else:
        return y

func3(True, 'a','b1')

#Exercise 4

def func4(x,y):
    return x * y

func4(2,31)

#Exercise 5

def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False
is_even(4)

#Exercise 6

def func6(x,y):
    if x > y:
        return True
    else:
        return False

#Exercise 7

def func7(*args):
    return sum(args)

#Exercise 8

def func8(*args):
    return [items for items in args if items % 2 == 0]

print(func8(2,3,1,4,5,6,8))

#Exercise 9

def func9(value):
    answer = ''
    for i in range(0,len(value)):
        if i %2 == 0:
            answer += value[i].upper()
        else:
            answer += value[i].lower() 
    return answer

print(func9('string'))

#Exercise 10

def func10(x,y):
    if x % 2 == 0 and y % 2 == 0:
        return True
    else:
        return False

print(func10(2,4))
print(func10(1,2))

#Exercise 11

def func11(x,y):
    if x[0] == y[0]:
        return True
    else:
        return False

print(func11('kitten', 'kit-kat'))

#Exercise 12

def func12(x):
    return x ** 2

print(func12(8))

#Exercise 13

def func13(value):
    if value == None or value == '':
        return None
    elif len(value) == 1:
        return value.upper()
    elif len(value) < 4:
        return value[0].upper() + value[1:]
    else:
        return value[0].upper() + value[1:2] + value[3].upper() + value[4:]

print(func13(''))
print(func13('tan'))
print(func13('fantastic'))

