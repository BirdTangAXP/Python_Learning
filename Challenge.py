#UserNum = int(input("Give me a number:"))

#d=[0]*UserNum

#d[1]=1

#for i in range(2,UserNum):
#    d[i]=d[i-2]+d[i-1]


#for i in range(UserNum):
#    print(d[i])


from typing import Mapping

map = {}


def main():
    while True:
            n = int(input("n:"))
            print(fib(n,map))
            print(fibonacci(n))

def fib(n,map):
    if n < 0:
        return 'error'
    if n in map:
        return map[n]

        
    if n == 0 or n ==1:
        return n
    map[n] = fib(n-1,map) + fib(n-2,map)
    print(map)
    return map[n]

def fibonacci(n):
    if n < 0:
        return 'error'
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

main()