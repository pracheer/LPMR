#!/usr/bin/env python
"""
Author: Akshay U. Bhat
    Description: Python file for setting up and executing Label Propgation job
    example call ./run.py Net.txt 4 17000000 
"""
import sys,os
exec_init_string = 'hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar  -input %s -output Label%d.txt -mapper "mapper.py %d" -reducer NONE -file mapper.py'
exec_string = 'hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar  -input %s -output Label%d.txt -mapper "mapper.py %d Label.txt" -reducer NONE -file mapper.py -file Label.txt'
get_string = 'hadoop fs -getmerge Label#.txt Label.txt'

if __name__ == '__main__':
    sizehint = 0
    infile = ''
    iterations = 0
    try:
        infile = sys.argv[1]
        iterations =  int(sys.argv[2])
        sizehint = int(sys.argv[3])
    except:
        print "Please specify infile, number of iterations, maximum node index"
        exit()
    os.system(exec_init_string%(infile,0,sizehint))
    os.system(get_string.replace('#','0'))
    for i in range(1,iterations):
        os.system(exec_string%(infile,i,sizehint))
        os.system('rm Label.txt')
        os.system(get_string.replace('#',str(i)))
    os.system('rm Label.txt')
