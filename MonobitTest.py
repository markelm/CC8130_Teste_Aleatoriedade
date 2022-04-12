
hex_to_bin = {
    '0': 0,
    '1': 1,
    '2': 1,
    '3': 2,
    '4': 1,
    '5': 2,
    '6': 2,
    '7': 3,
    '8': 1,
    '9': 2,
    'A': 2,
    'B': 3,
    'C': 2,
    'D': 3,
    'E': 3,
    'F': 4,
    "'": 0,
    '\n': 0
}


result = {}
with open('keys.txt') as f:
    #print(f.readline())
    #for index, line in enumerate(f):
    #    print("Line {}: {}".format(index, line.strip()))

    for index, line in enumerate(f):
        count = 0
        line = line.strip("'")

        for c in line:
            count += hex_to_bin[c]
        result[index+1] = count



x1 = 9654
x2 = 10346

testResult = {}

for key in list(result.keys()):
    if result[key] > x1 and result[key] < x2:
        testResult[key] = ('PASSED', result[key])
    else:
        testResult[key] = ('FAILED', result[key])


print('\n>>>>>>>>>>>>> Monobit Test <<<<<<<<<<<<<<\n')

for index, key in enumerate(list(testResult.keys())):
    print(key,":", testResult[key])

            