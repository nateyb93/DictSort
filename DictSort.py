##################################################################################
#                                                                                #
#    Sorts a dictionary based on the lexi-value of each value stored in keys.    #
#                                                                                #
#    This should only be used to sort dictionaries with lexi-sortable value      #
#    types. Behavior is not tested for other value-types.                        #
#                                                                                #
#    AUTHOR: Nathan Brown                                                        #
#    VERSION: 2/2/2015                                                           #
#                                                                                #
##################################################################################

from collections import namedtuple;

item = namedtuple('item', 'key value')

def sortByValue(dict):
    """Sorts a dictionary into a list of named tuples
       :param dict: dictionary to sort
       :returns: list of namedtuples"""
    sortedList = []
    for key in dict:
        sortedList.append(item(key, dict[key]))

    sortedList = sorted(sortedList, key=lambda item: item.value);
    
    return sortedList;

