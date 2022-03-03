num = int(input())
for _ in range(num):
    sum = 0
    combo=[]
    test_data = input()
    for i in test_data:
        if i == 'O':
            combo.append(i)
            sum += len(combo)
        else:
            combo.clear()
    print(sum)