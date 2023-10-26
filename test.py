#!/usr/bin/python3
import re

# Your key-value pair
key_value_pair = 'name="My_lit\"tle_house"'

match = re.search(r'([^=]+)="(.+)"', key_value_pair)

if match:
    key = match.group(1)
    raw_value = match.group(2)

print(f'key: {key} and value: {raw_value}')
