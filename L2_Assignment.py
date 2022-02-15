def largest(list):
    input_list = list.copy()  # why the order change if I dont use ".copy()"????
    input_list.sort(reverse=True)
    return input_list[0]

def reverse(list):
    list_len = len(list)
    rev_list = []
    for i in range(list_len):
        id = list_len - i -1
        rev_list.append(list[id])   
    return rev_list

def check_exist(list, check_num):
    list_len = len(list)
    is_here = False
    for i in range(list_len):
        if list[i] == check_num:
            is_here = True
            break
    return is_here

def show_odd(list):
    list_len = len(list)
    odd_list = []
    for i in range(list_len):
        if (i+1) % 2 == 1:
            odd_list.append(list[i])   
    return odd_list

def sum(list):
    total = 0
    for num in list:
        total += num
    return total

def is_palindrome(list):
    list_len = len(list)
    if list == reverse(list):
        return True
    else:
        return False


n = [1,2,3,2,1]
print(largest(n))
print(n)
print(reverse(n))
print(check_exist(n,3))
print(show_odd(n))
print(sum(n))
print(n)
print(is_palindrome(n))

