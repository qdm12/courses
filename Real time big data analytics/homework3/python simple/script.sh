#!/bin/sh

set -e
# Build class files
chmod +x PageRankMapper.py PageRankReducer.py
cat ./pageInputs.txt | ./PageRankMapper.py | sort | ./PageRankReducer.py
read -p "Press [Enter] if the output is correct..."

# Creates or cleans hdfs directory
hdfs dfs -mkdir -p /user/qm301/class3
hdfs dfs -put -f pageInputs.txt /user/qm301/class3
hdfs dfs -rm -r -f /user/qm301/class3/output
hdfs dfs -mkdir -p /user/qm301/class3/python_code
hdfs dfs -put -f PageRankMapper.py /user/qm301/class3/python_code
hdfs dfs -put -f PageRankReducer.py /user/qm301/class3/python_code
hdfs dfs -chmod a+x /user/qm301/class3/python_code/PageRankMapper.py
hdfs dfs -chmod a+x /user/qm301/class3/python_code/PageRankReducer.py

set +e
# Runs the program and checks outputs
hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -files hdfs://dumbo/user/qm301/class3/python_code/PageRankMapper.py,hdfs://dumbo/user/qm301/class3/python_code/PageRankReducer.py -mapper "python PageRankMapper.py" -reducer "python PageRankReducer.py" -input /user/qm301/class3/pageInputs.txt -output /user/qm301/class3/output -numReduceTasks 1
hdfs dfs -cat /user/qm301/class3/output/part-00000