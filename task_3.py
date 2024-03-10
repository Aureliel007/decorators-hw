import datetime
from functools import wraps

from task_2 import logger

@logger('task_3.log')
def flat_generator(list_of_lists):

    for lst in list_of_lists:
        for char in lst:
            yield char


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

print(list(flat_generator(list_of_lists_1)))
