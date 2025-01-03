from pprint import pprint
import operator
import os

# Создание словаря

with open('recipes.txt', encoding='utf-8') as file:
    cookbook = {}
    for line in file:
        dish = line.strip()
        dish_amount = int(file.readline())
        dish_list = []
        for _ in range(dish_amount):
            structure = file.readline().strip()
            ingredient, count, unit_measure = structure.split(' | ')
            dish_list.append(
                {'ingredient_name': ingredient,
                 'quantity': count,
                 'measure': unit_measure}
            )
        cookbook[dish] = dish_list
        file.readline()

pprint(cookbook, sort_dicts=False)

# Создание списка с ингредиентами и их количеством:

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_by_person_count = {}
    for one_dish in dishes:
        if one_dish in cookbook.keys():
            for ingredients in cookbook[one_dish]:
                if ingredients['ingredient_name'] not in ingredients_by_person_count:
                    new_quantity = person_count * int(ingredients['quantity'])
                    ingredients_by_person_count[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                                   'quantity': new_quantity}
                else:
                    ingredients_by_person_count[ingredients['ingredient_name']]['quantity'] += person_count * int(
                        ingredients['quantity'])
        else:
            print(f'Блюда - {one_dish} в книге рецептов нет!')
    return ingredients_by_person_count

print()
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос', 'Омлет'], 2), sort_dicts=False)

# Создание файла result из исходных файлов:

def get_info_and_writing_to_list(file_names):
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data


def writing_info_to_file(my_data, my_file):
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

print(writing_info_to_file(get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt']), 'result.txt'))