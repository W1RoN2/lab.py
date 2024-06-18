
import re

def task1(s):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, s))

import re

def task2(s):
    pattern = r'[A-Z]'
    return bool(re.search(pattern, s))

import re

def task3(s):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, s))

import re

def task4(s):
    pattern = r'^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(pattern, s))

import re

def task5(s):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, s))

import re

def task6(s):
    pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pattern, s))

import re

def task7(s):
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    return bool(re.match(pattern, s))

import re

def task8(s):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, s))

import re

def task9(s):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%]).{8,}$'
    return bool(re.match(pattern, s))

import re

def task10(s):
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(pattern, s))

