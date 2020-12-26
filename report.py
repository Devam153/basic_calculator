marks = int(input('enter marks: '))

if 85 <= marks <= 100:
    print('A+')
elif 80 <= marks <= 84:
    print('A')
elif 70 <= marks <= 79:
    print('B+')
else:
    print('FAIL')