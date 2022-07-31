import requests

def recipe_search(ingredient):
    app_id = '53386141'
    app_key = 'e544fdb59d6845fb635843509e4899fc'
    mealtype = input('Enter a meal type: ')
    health = input('Enter a diet: ')
    result = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}&mealType={}&health={}'.format(ingredient,app_id,app_key, mealtype,health))
    data = result.json()
    return data['hits']
#cross reference to Edamam
ingredient = input('Enter an ingredient for its nutitional values: ')
url = 'https://api.edamam.com/api/nutrition-data?app_id=9d1995fa&app_key=ff9ab085330208f30783bd2645ab0514&nutrition-type=logging&ingr={}'.format(ingredient)
response = requests.get(url)
ingredient = response.json()
print("here you can find more information ", ingredient['uri'])
print("the calories are ", ingredient['calories'])
print(ingredient['totalNutrients'])

def run():
    ingredient = input('Enter an ingredient for recipies: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print("calories ", recipe['calories'], " kcal")
        print("time needed ", recipe['totalTime'], " min")
        print(recipe['totalNutrients'])
        with open('Recipe.txt', 'a') as text_file:
                list1 = recipe['label']
                list2 = recipe['url']
                text_file.write(list1)
                text_file.write('\n')
                text_file.write(list2)
                text_file.write('\n')
run()