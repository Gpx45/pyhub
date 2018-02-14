#!/usr/bin/python3
import base64
main = base64.b64encode(bytes(input('Place it here: '), 'utf-8'))
ls = list(str(main))
print(''.join(ls[2:-1]))
