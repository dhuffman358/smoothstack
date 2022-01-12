#Exercise 1

my_values = [1, "Smoothstack", 1.231]

print(my_values)

#Exercise 2

my_values = [1, 1, [1,2]]

print(my_values[2][1])

#Exercise 3

lst = ['a','b','c']
print(lst[1:])

#Exercise 4

days = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

print(days)

#Exercise 5

D = {'k1':[1,2,3]}
print( D['k1'][1]) #corrected from D[k1][1] which is invalid

#Exercise 6

ltot = (1, [2,3]) #is this what was being looked for? Not clear from the assignment

print(ltot)

#Exercise 7

mips = set("Mississippi")

print(mips)

#Exercise 8

mips.add('X')

print(mips)

#Exercise 9

print(set[1,1,2,3])

#Question 1
answer = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        answer.append(str(i))
print(",".join(answer))

#Question 2
data = 1
numbers = []
print('Type integer inputs. When ready to finish, type -1')
while data >= 0:
    data = int(input())
    numbers.append(data)
numbers.pop()
for i in range(len(numbers)):
    orig_number = numbers[i]
    while orig_number > 1:
        numbers[i] *= (orig_number -1)
        orig_number -= 1
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
print(",".join(numbers))
    
#Question 3
amount = int(input("Input number:"))
answers = {}

for i in range(1,amount + 1):
    answers[i] = i * i
print(answers)

#Question 4

data = input("Input a string of numbers, seperated only by a comma:")
data = data.split(',')
datatuple = tuple(data)

print(data)
print(datatuple)

#Question 5:
class Test_Cl():
    def __init__(self):
        _string = ''
    def getString(self):
        self._string = input("Type in a string:")
    def printString(self):
        print(self._string.upper())
example = Test_Cl()
example.getString()
example.printString()

#Question 6:





