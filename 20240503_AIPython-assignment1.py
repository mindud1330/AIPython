# fruits number
n = int(input())

# make fruit dictionary
fruit_dict = {}
for _ in range(n):
    fruit, price = input().split()
    fruit_dict[fruit] = int(price)
# print(fruit_dict)

# calculate total price    
def total_price(n):
    tot = 0
    for _ in range(n):
        fruit, count = input().split()
        tot += fruit_dict[fruit] * int(count)
    return tot
    
tot_price = total_price(int(input()))

# print result
print(tot_price)