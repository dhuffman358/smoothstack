#Three is a Crowd
def crowd_test(people):
    if len(people) > 3:
        print("The room is crowded.")

names = ['Joe', 'Susan', 'Nathan', 'Clark']
crowd_test(names)
names.pop()
names.pop()
crowd_test(names)
print("---Next part---")
#Three is a Crowd - Part 2
def crowd_test2(people):
    if len(people) > 3:
        print("The room is crowded.")
    else:
        print("The room is not very crowded.")

names = ['Joe', 'Susan', 'Nathan', 'Clark']
crowd_test2(names)
names.pop()
names.pop()
crowd_test2(names)
print("---Next part---")
def crowd_test3(people):
    if len(people) > 5:
        print("There is a mob in the room.")
    elif len(people) > 3:
        print("The room is crowded.")
    elif len(people) == 0:
        print("The room is empty")
    else:
        print("The room is not very crowded.")
names = ['Joe', 'Susan', 'Nathan', 'Clark', 'Joe 2', 'Joe 3']
crowd_test3(names)
names.pop()
names.pop()
crowd_test3(names)
names.pop()
names.pop()
crowd_test3(names)
names.pop()
names.pop()
crowd_test3(names)