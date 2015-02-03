##################################################################################
#                                                                                #
#    Sorts a dictionary based on the lexi-value of each value stored in keys.    #
#                                                                                #
#    AUTHOR: Nathan Brown                                                        #
#    VERSION: 2/2/2015                                                           #
#                                                                                #
##################################################################################

from collections import namedtuple;

item = namedtuple('item', 'key value')

def sortedList(dict):
    """Sorts a dictionary into a list of named tuples
       :param dict: dictionary to sort
       :return: list of namedtuples"""
    sortedList = []
    for key in dict:
        sortedList.append(item(key, dict[key]))

    sortedList = sorted(sortedList, key=lambda item: item.value);
    
    return sortedList;

