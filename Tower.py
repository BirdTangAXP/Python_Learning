n = 2

Step_from = {}
Step_to = {}
transit = {}

# to initialize the Rod A
def set_up(R):
    blocks = []
    for i in range(n):
        R.blocks.append(i+1)

# Setting the Rod as an object
class Rod:
    def __init__(self, id, blocks):
        self.id = id
        self.blocks = blocks
        self.o_length = len(blocks)
    
    def get(self):
        the_block = self.blocks[0]
        self.blocks.pop(0)
        return the_block

    def put(self, the_block):
        self.blocks.insert(0,the_block)

    def is_in_order(self):
        in_order_n = 0
        n = self.count()
        for i in range(n):
            if self.blocks[i] == i+1:
                in_order_n += 1
        if in_order_n == n and n != 0:
            return True
        else:
            return False

    def count(self):
        return len(self.blocks)
    
    def display(self):
        print(self.blocks)



def display_all():
    print(Rod_A.blocks,Rod_B.blocks,Rod_C.blocks)


def moving_step(n, origin, destination, transit):
    if n < 1:
        return 'error'
    if n == 1:
        print("Move ",n, " From ",origin," to ",destination)
        
    if n > 1:
        moving_step(n-1,origin, transit, destination)
        print("Move ",n, " From ",origin," to ",destination)
        moving_step(n-1, transit, destination, origin)


n = 10


moving_step(n,"A","C","B")





Rod_A = Rod("A", [])
Rod_B = Rod("B", [])
Rod_C = Rod("C", [])

set_up(Rod_A)
display_all()






# Rod_A.display()
# print(Rod_A.count(), Rod_B.count())

# print(Rod_A.blocks, Rod_B.blocks)
# print(Rod_A.is_in_order(),Rod_B.is_in_order())


# the_block = Rod_A.get()
# Rod_B.put(the_block)

# print(the_block)

# print(Rod_A.blocks, Rod_B.blocks)
# print(Rod_A.count(), Rod_B.count())
# print(Rod_A.is_in_order(),Rod_B.is_in_order())




####    filling all collumns with fix position


# rod_a = [0]*n
# rod_b = [0]*n
# rod_c = [0]*n

# def set_up(n):
#     origin = [0]*n 
#     for i in range(n):
#         origin[i] = i + 1
#     return origin

# def move(origin,destination,n):
#     moving_block = 0

#     for i in range(n):
#         if origin[i] != 0:
#             moving_block = origin[i]      #saving the block size
#             origin[i] = 0                 #removing the block at top
#             break
#         if i == n - 1:
#             return print("nth can be moved")
    
#     for i in  range(n):
#         if destination[i] != 0:
#             destination[i-1] = moving_block
#             break
#         elif i == n-1:
#             destination[i] = moving_block

#     return origin, destination



# rod_a = set_up(n)


# if n%2 == 1:
#     destination = rod_c



# print(rod_a, rod_b, rod_c)

# rod_a, rod_b = move(rod_a,rod_b,n)

# print(rod_a, rod_b, rod_c)

# rod_a, rod_c = move(rod_a,rod_c,n)

# print(rod_a, rod_b, rod_c)

# rod_c, rod_a = move(rod_c,rod_a,n)

# print(rod_a, rod_b, rod_c)



