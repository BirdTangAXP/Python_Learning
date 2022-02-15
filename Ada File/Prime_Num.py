num = int(input("Enter a number")) 
is_divisible=False 
for i in range(2,num):
    if num%i==0:
        is_divisible=True
        print("it is not a prime number")
        break
if is_divisible==False:
    print("it is a prime number")