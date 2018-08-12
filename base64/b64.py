#!/usr/bin/python3
import base64
ls = list(str(base64.b64encode(bytes(input('Place it here: '), 'utf-8'))))
print(''.join(ls[2:-1]))
