#Exercise 1

#no coding

#Exercise 2
information = [[34587, 'Learning Python, Mark Lutz', 4, 40.95], 
               [98762, 'Programming Python, mark Luzt', 4, 56.80],
               [77226, 'Head First Python, Paul Berry', 3, 32.95], 
               [88112, 'Einfuhrun in Python3, Bernd Klein', 3, 24.99]]

answer = list(map(lambda x : (x[0], x[2] * x[3] +10) if ( x[2] * x[3] < 100) else (x[0], x[2] * x[3]) , information) )
print(answer)

#Exercise 3

information = [[34587, ('Learning Python, Mark Lutz', 4, 40.95)], 
               [98762, ('Programming Python, mark Luzt', 4, 56.80)],
               [77226, ('Head First Python, Paul Berry', 3, 32.95)], 
               [88112, ('Einfuhrun in Python3, Bernd Klein', 3, 24.99)]]

answer = list(map(lambda x : (x[0], x[1][1] * x[1][2] +10) if ( x[1][1]  * x[1][2] < 100) else (x[0], x[1][1]  * x[1][2]) , information) )
print(answer)