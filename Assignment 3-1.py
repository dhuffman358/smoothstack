import random

from numpy import append

#Exercise 1

answer = []

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0 :
        answer.append(i)
print(answer)

#Exercise 2

def temp_converter(degree, type):
    if(type == 'F' or type == 'f'):
        return((degree -32) / 1.8)
    if(type == 'C' or type == 'c'):
        return(degree * 1.8 + 32)
print(temp_converter(100, 'C'))

#Exercise 3

"""answer = random.randint(1,10)
correct = False
while not correct:
    guess = int(input('Enter a number between 0 and 9:'))
    if(guess == answer):
        correct = True
    else:
        print("Wrong! Try again.")
print("You guessed correctly!")
"""
#Exercise 5
output = ''
for i in range(0,9):
    if i < 5:
        for j in range(0,i):
            output += '*'
    else:
        for j in range(0,8-i):
            output += '*'

    output += '*\n' 
print(output)


#Exercise 6

word = input('Enter a word:\n')
print(word[::-1])

#Exercise 7
def odd_even(number_series):
    odd = 0
    even = 0
    for number in number_series:
        if number % 2 == 0:
            even +=1
        else:
            odd +=1
    return (odd,even)

print(odd_even([1,2,3,4,5,6,7,8,9]))

#Exercise 8
def return_type(obj_lst):
    result = []
    for item in obj_lst:
        result.append(type(item))
    return result
data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
datat = return_type(data)
i = 0
for item in data:
    print(f'{item} is of type: {datat[i]}')
    i +=1
#Exercise 9
answer = []
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    answer.append(i)
print(answer)

