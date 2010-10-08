#!/usr/bin/env sh
# Generic Usage:
# ./run.sh twitter_rv.net
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input $1 -output Net.txt -mapper 'mapper.py Reverse' -reducer reducer.py -file mapper.py -file reducer.py -file exclude.txt