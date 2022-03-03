a = int(input())
b = int(input())
c = int(input())

num = a * b * c
num_list =[0,0,0,0,0,0,0,0,0,0]
while num > 0 :
    a = num % 10
    num = num//10
    num_list[a] += 1

for i in range(len(num_list)):
    print(num_list[i])