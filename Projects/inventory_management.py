def create_inevntory(items,stock,price):
    num = int(input('How many items yo want to add : '))
    for i in range(num):
        item = input(f'Enter item {i+1} : ')
        items.append(item)
    
    for item in items:
        quantity = int(input(f'Enter quantity of {item} : '))
        stock[item] = quantity
        cost = int(input(f'Enter price of {item} : '))
        price[item] = cost

def display_stock(items,stock,price):
    print(f'Item \t Quantity \t Price')
    for item in items:
        print(f'{item} \t {stock[item]} \t\t {price[item]}')


#create_inevntory(items,stock,price)
#display_stock(items,stock,price)
