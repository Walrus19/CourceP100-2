# TODO Напишите функцию для поиска индекса товара
from idlelib.debugobj_r import remote_object_tree_item


def get_index(items, f_item):
    for i,item in enumerate(items):
        if item == f_item:
             rezult = i
             return rezult




items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = get_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
        #111


