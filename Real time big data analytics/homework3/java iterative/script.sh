#!/bin/sh

set -e
# Build class files
javac -classpath `yarn classpath` -d . PageRankMapper.java
javac -classpath `yarn classpath` -d . PageRankReducer.java
javac -classpath `yarn classpath`:. -d . PageRank.java

# Build jar file
jar -cvf PageRank.jar *.class

# Creates or cleans hdfs directory
hdfs dfs -mkdir -p /user/qm301/class3
hdfs dfs -put -f pageInputs.txt /user/qm301/class3
hdfs dfs -rm -r -f /user/qm301/class3/output*

set +e
# Runs the program and checks outputs
hadoop jar PageRank.jar PageRank /user/qm301/class3/pageInputs.txt /user/qm301/class3/output
hdfs dfs -cat /user/qm301/class3/output/part-r-00000