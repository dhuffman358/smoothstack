#Exercise 1

print("Hello World"[8])

#Exercise 2

print("thinker"[2:5])
S = 'hello'

#Output of h[1] is an error because h has not been defined

#Exercise 3

S = 'Sammy'
print(S[2:])

#Exercise 4

mips = "".join(set("Mississippi"))

print(mips)

#Exercise 5

lines = int(input("Input data:"))
answers = []
for i in range(0,lines):
    data = input()
    data = [ character.upper() for character in data if character.isalnum() ]
    if data == data[::-1]:
        answers.append('Y')
    else:
        answers.append("N")
print(" ".join(answers)) 

