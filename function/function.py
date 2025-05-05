# def get_full_name(first_name:str, last_name:str):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name

# print(get_full_name("john","doe"))

# cities = ["NewYork", "Los Angeles", "Chicago", "Houston"]
# heroes = ["Superman", "Batman", "Wonder", "Spiderman", "Ironman"]

# def print_name(arr:list[str]):
#     for item in arr:
#         print(item, end=" ")

# print_name(cities)

def find_factorial(num:int):
    factorial = 1
    for el in range(1, num+1):
        factorial *= el
    print(factorial)

find_factorial(3)