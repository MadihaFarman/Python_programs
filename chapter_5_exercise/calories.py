def main():
    fat_grams = float(input('Enter the grams of fat that you consume daily: '))
    carbohydrate_grams = float(input('Enter the grams of carbohydrates that you consume daily: '))
    print('Calories from',fat_grams,' grams of fat =',fat_calories(fat_grams),'calories')
    print('Calories from',carbohydrate_grams,' grams of carbohydrate =',carbohydrate_calories(carbohydrate_grams),'calories')
def fat_calories(fat_grams):
    return fat_grams * 9
def carbohydrate_calories(carbohydrate_grams):
    return carbohydrate_grams * 4
main()