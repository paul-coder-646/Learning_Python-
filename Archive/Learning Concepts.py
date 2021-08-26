'''
from collections import deque
from itertools import permutations
mystr = "                   Hello World"
mystrsub = mystr[::-1]
print(mystrsub.upper())
mystr = mystr.strip()
my_list = mystr.split()
var = 3.143245
myvarstr = f"the var is {var*2}"
print (myvarstr)
d = deque()
d.append(15)
d.append(2)
d.append(3)
d.appendleft(4)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

from itertools import permutations, accumulate, groupby

def codecracker(lenofcode, digits_up_to):
    a = range(0, digits_up_to)
    perm = permutations(a, 6)
    print(len(list(perm)))

def smaller_than_3(x):
    return x < 3

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func= )
group_oj = groupby(a, key=smaller_than_3())
print (list(acc))
print(key, list(value))



import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5,backupCount=5)
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)
logger.addHandler(handler)

logger.warning('this is a warning')
logger.error('this is an error')

try:
    a = [1, 2, 3]
    a[3] = 4
    
except IndexError:
    logging.error('this went wrong')

for _ in range(6):
    logger.info('Hello World!')
    time.sleep(5)



import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

with open('person.json', 'r') as readfile:
    persons = json.load(readfile)

print(persons)

'''


def hello(person, name, age, *args, **kwargs):
    x = 10
    x = lambda x: x+1
    print(f"hello {person} i see that you are {age} old")
    print(x)