# Real time Big Data Analytics: Homework 2

## Summary of "The Google File System" by Ghemawat, Gobioff, and Leung
You can download the document from [Google](http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)

Summary:
- Concerns the Google File System or *GFS*
- Built for distributed data intensive applications
- GFS has integrated constant monitoring, error detection, fault tolerance, and automatic recovery
- GFS is compatible with inexpensive commodity hardware
- The GFS is widely used at Google for their services and R&D
- IO operations and block sizes are adapted:
    - Sequential read of large files
    - Large files getting appended instead of overwritten or modified
- High sustained bandwidth is more important than low latency
- Flexibility: concurrent atomic append operation with low synchronization overhead, 
- Architecture consists in a master and multiple chunk servers
- The GFS master keeps in its memory metadata concerning the files, the chunks and the mapping between them.
- Chunks are distributed and copied generally 3 times across chunkservers to achieve fault tolerance.

## Simple Python WordCount solution
This counts the number of lines a certain search term occurs in.

1. Simply test the program with:
   
   ```bash
   cat ./tweetInputs.txt | ./TweetCounter.py
   ```
   
## Dumbo and Python MapReduce solution
This counts the number of lines a certain search term occurs in.

1. Log into Dumbo with:

   ```bash
   ssh -L 8026:prince:22 qm301@hpc2.nyu.edu
   ssh -Y qm301@dumbo.es.its.nyu.edu
   ```
   
2. Paste the content of the Python files and the input with the following:

   ```bash
   nano TweetMapper.py
   nano TweetReducer.py
   nano tweetInputs.txt
   ```
   
3. Make sure the Python files are executable
   
   ```bash
   chmod +x TweetMapper.py TweetReducer.py
   ```
   
4. Test your program locally without HDFS
   
   ```bash
   cat ./tweetInputs.txt | ./TweetMapper.py | sort | ./TweetReducer.py
   ```
   
   If the output is as expected, proceed to the following.

5. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class2
   hdfs dfs -put -f tweetInputs.txt /user/qm301/class2
   ```
   
6. Put the Python files on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class2/python_code
   hdfs dfs -put -f TweetMapper.py /user/qm301/class2/python_code
   hdfs dfs -put -f TweetReducer.py /user/qm301/class2/python_code
   hdfs dfs -chmod a+x /user/qm301/class2/python_code/TweetMapper.py
   hdfs dfs -chmod a+x /user/qm301/class2/python_code/TweetReducer.py
   ```
   
7. Run the Python code with Hadoop on the HDFS:

   ```bash
   hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -files hdfs://dumbo/user/qm301/class2/python_code/TweetMapper.py,hdfs://dumbo/user/qm301/class2/python_code/TweetReducer.py -mapper "python TweetMapper.py" -reducer "python TweetReducer.py" -input /user/qm301/class2/tweetInputs.txt -output /user/qm301/class2/output -numReduceTasks 1
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class2/output/part-00000
   ```
   
## Dumbo and Java MapReduce solution
This calculates the number of lines a certain search term occurs in.

1. Log into Dumbo with:

   ```bash
   ssh -L 8026:prince:22 qm301@hpc2.nyu.edu
   ssh -Y qm301@dumbo.es.its.nyu.edu
   ```
   
2. Paste the content of the Java files and the input with the following:

   ```bash
   nano TweetCounterMapper.java
   nano TweetCounterReducer.java
   nano TweetCounter.java
   nano tweetInputs.txt
   ```
   
3. Compile your code with Java:

   ```bash
   javac -classpath `yarn classpath` -d . TweetCounterMapper.java
   javac -classpath `yarn classpath` -d . TweetCounterReducer.java
   javac -classpath `yarn classpath`:. -d . TweetCounter.java
   ```
   
4. Compile the Jar file with:

   ```bash
   jar -cvf tweetCount.jar *.class
   ```
   
5. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class2
   hdfs dfs -put -f tweetInputs.txt /user/qm301/class2   
   ```
     
6. Run the Java code with Hadoop on the HDFS:

   ```bash
   hadoop jar tweetCount.jar TweetCounter /user/qm301/class2/tweetInputs.txt /user/qm301/class2/output
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class2/output/part-r-00000
   ```