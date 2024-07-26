def main():
    foods = ['Burger','Shawarma','Hot wings']
    print('Here are the items in the food list: ')
    for food in foods:
        print(food)
    item = input('Which item do you want to change? ')
    try:
        item_index = foods.index(item)
        new_item = input('Enter new item: ')
        foods[item_index] = new_item
        print('The list has been updated.\nHere is the revised list : ')
        print(foods)
    except:
        print('That item was not found in the list.')
main()