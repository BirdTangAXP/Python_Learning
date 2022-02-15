#UserNum = int(input("Give me a number:"))

#for i in range(UserNum):
#    print(i+1)


#for i in range(1,31):
#    print(i)

#for i in range(17):
#    print(i+7)

#for i in range(6,101,2):
#    print(i)

#for i in range(10,1001,10):
#    print(i)

#for i in range(100):
#    print((i+1)*10)

#UserNum = int(input("Give me a number:"))

#for i in range(1,UserNum+1):
#    if i%3==0 or i%5==0:
#        print(i)    

#UserNum = int(input("Give me a number:"))

#for i in range(1,UserNum+1):
#    for j in range(1, UserNum+1):
#        print( i,"X",j,"=",i*j)

UserNum = int(input("Give me a number:"))

is_prime=[True]*UserNum


for i in range(2,UserNum+1):
    for j in range(2, i):
        if i%j==0:
            is_prime[i-1]=False
            break

for i in range(1,UserNum):
    if is_prime[i] == True:
        print(i+1)


            