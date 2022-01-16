item_number = int(input("input data:\n"))
i = 0
results = []
while i < int(item_number):
    interim1 = input()
    interim2 = input()
    interim = (float(interim1), float(interim2))
    results.append((lambda x: x[0] / x[1] ** 2)(interim))
    i += 1
for item in results:
    if item < 18.5:
        print('under')
    elif item < 25.0:
        print('normal ')
    else:
        print('over ')