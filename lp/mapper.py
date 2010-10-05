#!/usr/bin/env python


"""
Mapper for Label Propagation algorithm using map-reduce

Author:
Name:       Akshay Bhat
WebSite:    http://www.akshaybhat.com

"""
import os, random, time, sys, array, logging, collections

def ParseOptions(argv):
    """
    Parse the Command line Options
    """
    SizeHint = 0
    if len(argv) > 1:
        SizeHint = int(argv[1])
    if len(argv) > 2:
        Labels = argv[2]
    else:
        Labels  = ''
    return [SizeHint,Labels]


def ApplyAndVote(line,delim = '\t'):
    """
    Applies the value of label for each neighbor
    and calls maxVote function
    """
    entry =  line.strip().split(delim)
    del line
    node = int(entry[0])
    
    if len(entry) != 1:     # handles cases where a node is not connected to any other node
        nLabels = [Label[int(k)] for k in entry[1:]]
        return node, maxVote(nLabels)
    else:
        return node, node


def maxVote(nLabels):
    """
    This function is used byt map function, given a list of labels of neighbors
    this function finds the most frequent labels and randomly returns one of them
    """
    cnt = collections.defaultdict(int)
    for i in nLabels:
        cnt[i] += 1
    del nLabels
    maxv = max(cnt.itervalues())
    return random.choice([k for k,v in cnt.iteritems() if v == maxv])

                
if __name__ == '__main__':
    [SizeHint,Labels]=ParseOptions(sys.argv) # Parse the command line options
    Label = array.array('i',range(SizeHint))    
    if Labels:
        for line in file(Labels):
            entries = line.strip().split('\t') 
            Label[int(entries[0])] = int(entries[1])
    for line in sys.stdin:
        try:
            node, newLabel = ApplyAndVote(line)
            print str(node) + '\t' + str(newLabel)
        except:
            print line
            raise
