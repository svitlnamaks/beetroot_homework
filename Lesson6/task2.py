# stock = {
# "banana": 6,
# "apple": 0,
# "orange": 32,
# "pear": 15
# }
# prices = {
#   "banana": 4,
#  "apple": 2,
# "orange": 1.5,
# "pear": 3
# }
# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.
def total_price(dict1, dict2):
    total = 0
    for key in dict1:
        key = (dict1[key] * dict2[key])
        total = total + key

    return total


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print('Total price is : ', total_price(stock, prices))
