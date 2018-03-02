#!/usr/bin/env python3
import binascii
key = "kJaeYzXn"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
        print(r)
    return r


for char in  cross:
    for i in 



def solve(s):
    quest = binascii.unhexlify(s)
    return quest

def main():
    phrase = "kJaeYzXn"
    ans = mystery(phrase)
    print(mystery(phrase))
    #print(binascii.b2a_uu(solve(ans)))

if __name__ == '__main__':
    main()
