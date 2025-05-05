# def recursion(n):
#     if(n == 0):
#         return
#     print(n)
#     recursion(n - 1)

# recursion(5)

# def sum_natural_number(num:int):
#     if(num == 0):
#         return 0
#     return sum_natural_number(num - 1) + num

# sum_natural_number(5)

list = ["a","b","c","d"]

def list_print(index:int):
    if(index == len(list)):
        return
    print(list[index])
    list_print(index + 1)

list_print(0)