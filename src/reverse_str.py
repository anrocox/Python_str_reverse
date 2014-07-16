#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

How to reverse a string in python?

¿Como invertir un string en python?
'''

#create a str
s = 'fresh fried fish'
print(s)

#using slice notation, returning the full string and defining step to -1
#s[start:stop:step]
s_rev = s[::-1]
print(s_rev)
