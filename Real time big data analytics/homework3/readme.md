# Real time Big Data Analytics: Homework 3

  
## Dumbo and Java basic PageRank solution
This calculates the page ranks with only one iteration. 

Follow the same procedure for the iterative PageRank (only PageRank.java is modified).

1. Log into Dumbo with:

   ```bash
   ssh -L 8026:prince:22 qm301@hpc2.nyu.edu
   ssh -Y qm301@dumbo.es.its.nyu.edu
   ```
   
2. Paste the content of the Java files and the input with the following:

   ```bash
   nano PageRankMapper.java
   nano PageRankReducer.java
   nano PageRank.java
   nano pageInputs.txt
   ```
   
3. Compile your code with Java:

   ```bash
   javac -classpath `yarn classpath` -d . PageRankMapper.java
   javac -classpath `yarn classpath` -d . PageRankReducer.java
   javac -classpath `yarn classpath`:. -d . PageRank.java
   ```
   
4. Compile the Jar file with:

   ```bash
   jar -cvf PageRank.jar *.class
   ```
   
5. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class3
   hdfs dfs -put -f pageInputs.txt /user/qm301/class3
   ```
     
6. Run the Java code with Hadoop on the HDFS:

   ```bash
   hadoop jar PageRank.jar PageRank /user/qm301/class3/pageInputs.txt /user/qm301/class3/output
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class3/output/part-r-00000
   ```
   
## Dumbo and Python basic PageRank solution

1. Log into Dumbo with:

   ```bash
   ssh -L 8026:prince:22 qm301@hpc2.nyu.edu
   ssh -Y qm301@dumbo.es.its.nyu.edu
   ```
   
2. Paste the content of the Python files and the input with the following:

   ```bash
   nano PageRankMapper.py
   nano PageRankReducer.py
   nano pageInputs.txt
   ```
   
3. Make sure the Python files are executable
   
   ```bash
   chmod +x PageRankMapper.py PageRankReducer.py
   ```
   
4. Test your program locally without HDFS
   
   ```bash
   cat ./pageInputs.txt | ./PageRankMapper.py | sort | ./PageRankReducer.py
   ```
   
   If the output is as expected, proceed to the following.

5. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class3
   hdfs dfs -put -f pageInputs.txt /user/qm301/class3
   ```
   
6. Put the Python files on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class3/python_code
   hdfs dfs -put -f PageRankMapper.py class3/python_code
   hdfs dfs -put -f PageRankReducer.py class3/python_code
   hdfs dfs -chmod a+x class3/python_code/PageRankMapper.py
   hdfs dfs -chmod a+x class3/python_code/PageRankReducer.py
   ```
   
7. Run the Python code with Hadoop on the HDFS:

   ```bash
   hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -files hdfs://dumbo/user/qm301/class3/python_code/PageRankMapper.py,hdfs://dumbo/user/qm301/class3/python_code/PageRankReducer.py -mapper "python PageRankMapper.py" -reducer "python PageRankReducer.py" -input /user/qm301/class3/pageInputs.txt -output /user/qm301/class3/output -numReduceTasks 1
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class3/output/part-00000
   ```