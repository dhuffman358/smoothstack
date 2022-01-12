#Assignment 1-2 - Python Coding exercise 2
#Daniel Huffman


#Exercise 1: 
sum = 50 + 50
difference = 100 - 10

print(f"Sum of 50 + 50: {sum}\nDifference of 100 - 10:  {difference}")

#Exercise 2:
print(f"{30 * 6}\n {6 ^ 6}\n {6 ** 6} \n {6 + 6 + 6 + 6 + 6 + 6 + 6}")

#Exercise 3:
print("Hello World")
print("Hello World : 10")

#Exercise 4:

loan_size = int(input("Input loan size:"))
interest_rate = (.01 *float(input("Input yearly percentage:")))/12
payout_time = int(input("Input payout time in months:"))

P = loan_size
r = interest_rate
n = payout_time 

monthly_payment = P * r * ((1+r) ** n) / ((1 + r) ** n - 1)

print(f"For a loan of size {loan_size} with a monthly rate of {interest_rate} paid over {payout_time} months, the monthly payment would be {int(monthly_payment) + 1}")

