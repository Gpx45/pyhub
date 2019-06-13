#!/usr/bin/python3
# Annotations are for information only,
# Its optional and used with functions to typically let
# programmers know what is passed and returned.

#ex. str
#ex. -> set

def search_vowels(word:str)->set:
    '''Return any vowels found in a supplied word.'''
    vowels = set('aeeeiouuu')
    common = vowels.intersection(set(word))
