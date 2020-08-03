#!/usr/bin/env python3.7
# simple script showing how to work with If/Else statements

users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1
