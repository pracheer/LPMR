#!/usr/bin/env sh
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input twitter_rv.net -output Net.txt -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -file exclude.txt
