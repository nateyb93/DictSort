from collections import namedtuple;

item = namedtuple('item', 'key value')

def sortedList(dict):
    sortedList = []
    for key in dict:
        sortedList.append(item(key, dict[key]))

    sortedList = sorted(sortedList, key=lambda item: item.value);
    
    return sortedList;

