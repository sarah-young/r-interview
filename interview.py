# Write a function to retrieve the response from the following API endpoint: https://csrng.net/csrng/csrng.php?min=0&max=10000. Example response: "[{"status":"success","min":0,"max":10000,"random":634}]"

import requests

def get_api_response():
    response = requests.get('https://csrng.net/csrng/csrng.php?min=0&max=10000')
    return response.json()

# get_api_response()

# 2 - Write a function that accepts a string representation of a number (the random value from the above response), e.g.: '123' and generate all unique permutations of the given string. i.e.: 123, 132, 213, 231, 321, 312

#  Idea: https://docs.python.org/2/library/itertools.html

from itertools import permutations

def generate_permutations(str):
    lists = list(permutations(str, len(str)))
    final_array = []
    for item in lists:
        final_array.append(''.join(item))
    return final_array


p = generate_permutations('123')
print(p)

from collections import defaultdict

def parse_permutations(lst):
    new_array = []
    for i in lst:
        new_array.append(int(i))
    print(sum(new_array))
    return sum(new_array)


pp = parse_permutations(p)

# 4 - Write unit tests: see tests.py

