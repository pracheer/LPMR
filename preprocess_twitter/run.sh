#!/usr/bin/env sh
hadoop fs -put ../Data/twitter_rv.net twitter_rv.net
hadoop jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2+320.jar -input twitter_rv.net -output Net.txt -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -file exclude.txt
