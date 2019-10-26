import ast
import random
import requests


FIRST_INIT_X = -120.983640
SECOND_INIT_X = -120.983540
THIRD_INIT_X = -120.983440
INIT_Y = 37.077644

# x = format(FIRST_INIT_X, '.4f')
# x = ast.literal_eval(x)
# y = format(INIT_Y, '.4f')
# y = ast.literal_eval(y)
x = FIRST_INIT_X
y = INIT_Y

def generate_rand() :
    rand = random.uniform(0.0001, 0.0009)
    return rand

url = 'our_domain'

for i in range(20):
    print(y, x)
    x = x + generate_rand()
    y = y + generate_rand()
    data = {
        'Latitude': format(x, '.4f'),
        'Longitude': format(y, '.4f'),
        'type': 'bee',
        'key': 'our_key'
    }
    print(data)
    # x = requests.post(url, data = data)


