#!/usr/bin/env python2.5
"""
Remove 2.5 from the line above, its a hack needed for it to work on Fedora

Author: Akshay Bhat
Desc:  mapepr script which reverse id's in each pair, such that all lines will be sorted according to the id of the user following other user

"""
import sys

if __name__ == '__main__':
    Exclude = {} # an array might be used instead of dictionary. Though it is less memmory efficient but it gurrantees O(1) access time.
    try: 
	for line in file('exclude.txt').readlines():
            Exclude[line.strip().split('\t')[0]] = 1
    except:
	
        raise
    
    for line in sys.stdin:
        entries =  line.strip().split('\t')
        Following = entries[0]
        User = entries[1]
        if Exclude:
            if not(User in Exclude) and not(Following in Exclude):
                print User + '\t' + Following
        else:
            print User + '\t' + Following
