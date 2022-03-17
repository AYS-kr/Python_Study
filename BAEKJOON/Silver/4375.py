while True:
    try:
        num = int(input())
    except EOFError:
        break
    check = '1'
    while True:
        if int(check) % num == 0 :
            print(len(check))
            break
        check += '1'
