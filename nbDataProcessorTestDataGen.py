file=open('testDataProc.txt', 'w')
for row in range(30):
    if row > 0:
        file.write('\n')
    for col in range(6):
        file.write(str(row+col))
        file.write(',')

