UserNum = int(input("Give me a number: "))

line = [0]*100
i = 0
k = 0
peak_id = 0
line[i] = UserNum

while line[i] > 1 :
    if line[i]%2 == 0:
        next_num = line[i]/2
        k = k+1
        for j in range(k):
            print(" ",end='')
    else:
        next_num = line[i]*3+1
        for j in range(k):
            print(" ",end='')
    print(int(next_num))

    i=i+1   # next number

    line[i] = int(next_num)
    
    if line[i]>line[peak_id]:
        peak_id = i
    


print("-----------length:",i,"-----------------Peak@",line[peak_id],"--------------")