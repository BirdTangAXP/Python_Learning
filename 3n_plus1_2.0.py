def main():
    while True:
        user_num = int(input("Give me a number: "))
        peak_num = [0] * (user_num+1)
        peak_id = [0] * (user_num+1)
        length = [0] * (user_num+1)
        for j in range(1,user_num+1): 
            current_num = j
            i = 0
            peak_num[j] = current_num
            print(current_num,end='')
            while current_num > 1:
                i = i+1
                current_num = next(current_num)
                print('->',current_num,end='')
                if current_num > peak_num[j]:
                    peak_num[j] = current_num
                    peak_id[j] = i
            length[j] = i+1
            print('')

        print("")
        for k in range(1,user_num+1):
            print(k,' : lenght= ', length[k],', peak@', peak_num[k],' , id=',peak_id[k])
        #print("-------------lenght:",i,"-----------peak@",peak_num,"-----------")


def next(n):
    if n%2==0:
        return int(n/2)
    else:
        return n*3+1

main()

