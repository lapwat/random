#!/usr/bin/env python
import string, random

# alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
alphabet = string.ascii_letters + string.digits + '-' + '_'

# use urandom to pick up 24 random characters from the alphabet
r = random.SystemRandom()
password = ''.join([r.choice(alphabet) for _ in range(24)])

print(password)
