# Real time Big Data Analytics: Homework 1

## Summary of "MapReduce: Simplified Data Processing on Large Clusters" by Jeffrey Dean and Sanjay Ghemawat
The original document is available [here](http://static.usenix.org/event/osdi04/tech/full_papers/dean/dean.pdf)

This paper concerns the MapReduce programming model for large data sets and was written in 2004 by Jeffrey Dean and Sanjay Ghemawat from Google. It explains how the Map and Reduce operate, highlights implementation details and extensions to the model. The Map processes large amount of data and generates key – value pairs from it. The Reduce is applied to all intermediate values sharing the same intermediate key. Multiple examples such as the distributed sort are given. The execution of the MapReduce is detailed, highlighting where the data is partitioned, distributed to the workers of a cluster and combined back in the final solution. The role of the master is to supervise the workers and reassemble the solutions together. The MapReduce implementations are also described as fault tolerant, as worker can fail (and even the master can) without making the entire problem solving procedure fail. More information on the dynamic adaptability of the MapReduce implementation with backup tasks or task granularity is provided. Finally, information regarding extensions such as counters, debugging and status information is given. The paper concludes by stating that MapReduce was a success at Google because it is easy to use and because it hides away from the user all its details about parallelization, fault-tolerance and various other optimizations. 

## Cloudera VM with Java
1. Download the Cloudera Quickstart VM from [cloudera.com](https://www.cloudera.com/downloads/quickstart_vms/5-10.html). **Note** that your machine has to have more than **4GB of RAM** for it to work.
2. Setup a working directory and go to this one with:

   ```bash
   mkdir -p ~/homework1/java
   cd ~/homework1/java
   ```
   
3. Paste the content of the Java files and the input with the following:

   ```bash
   nano MaxTemperatureMapper.java
   nano MaxTemperatureReducer.java
   nano MaxTemperature.java
   nano temperatureInputs.txt
   ```
   
4. Compile your code with Java:

   ```bash
   yarn classpath
   javac -classpath `yarn classpath` -d . MaxTemperatureMapper.java
   javac -classpath `yarn classpath` -d . MaxTemperatureReducer.java
   javac -classpath `yarn classpath`:. -d . MaxTemperature.java
   ```
   
5. Compile the Jar file with:

   ```bash
   jar -cvf maxTemp.jar *.class
   ```
   
6. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/cloudera/class1
   hdfs dfs -put -f temperatureInputs.txt /user/cloudera/class1   
   ```
     
7. Run the Java code with Hadoop on the HDFS:

   ```bash
   hadoop jar maxTemp.jar MaxTemperature /user/cloudera/class1/temperatureInputs.txt /user/cloudera/class1/output
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/cloudera/class1/output/part-r-00000
   ```


## Dumbo

### Python
1. Log into Dumbo with:

   ```bash
   ssh -L 8026:prince:22 qm301@hpc2.nyu.edu
   ssh -Y qm301@dumbo.es.its.nyu.edu
   ```
   
2. Paste the content of the Python files and the input with the following:

   ```bash
   nano MaxTemperatureMapper.py
   nano MaxTemperatureReducer.py
   nano temperatureInputs.txt
   ```
   
3. Make sure the Python files are executable
   
   ```bash
   chmod +x MaxTemperatureMapper.py MaxTemperatureReducer.py
   ```
   
4. Test your program locally without HDFS
   
   ```bash
   cat ./temperatureInputs.txt | ./MaxTemperatureMapper.py | sort | ./MaxTemperatureReducer.py
   ```
   
   If the output is as expected, proceed to the following.

5. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class1
   hdfs dfs -put -f temperatureInputs.txt /user/qm301/class1   
   ```
   
6. Put the Python files on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class1/python_code
   hdfs dfs -put -f MaxTemperatureMapper.py class1/python_code
   hdfs dfs -put -f MaxTemperatureReducer.py class1/python_code
   hdfs dfs -chmod a+x class1/python_code/MaxTemperatureMapper.py
   hdfs dfs -chmod a+x class1/python_code/MaxTemperatureReducer.py
   ```
   
7. Run the Python code with Hadoop on the HDFS:

   ```bash
   hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -files hdfs://dumbo/user/qm301/class1/python_code/MaxTemperatureMapper.py,hdfs://dumbo/user/qm301/class1/python_code/MaxTemperatureReducer.py -mapper "python MaxTemperatureMapper.py" -reducer "python MaxTemperatureReducer.py" -input /user/qm301/class1/temperatureInputs.txt -output /user/qm301/class1/output -numReduceTasks 1
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class1/output/part-00000
   ```
   
### Java
1. Log into Dumbo with:

   ```bash
   ssh -L 8026:prince:22 qm301@hpc2.nyu.edu
   ssh -Y qm301@dumbo.es.its.nyu.edu
   ```
   
2. Paste the content of the Java files and the input with the following:

   ```bash
   nano MaxTemperatureMapper.java
   nano MaxTemperatureReducer.java
   nano MaxTemperature.java
   nano temperatureInputs.txt
   ```
   
4. Compile your code with Java:

   ```bash
   javac -classpath `yarn classpath` -d . MaxTemperatureMapper.java
   javac -classpath `yarn classpath` -d . MaxTemperatureReducer.java
   javac -classpath `yarn classpath`:. -d . MaxTemperature.java
   ```
   
5. Compile the Jar file with:

   ```bash
   jar -cvf maxTemp.jar *.class
   ```
   
6. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class1
   hdfs dfs -put -f temperatureInputs.txt /user/qm301/class1   
   ```
     
7. Run the Java code with Hadoop on the HDFS:

   ```bash
   hadoop jar maxTemp.jar MaxTemperature /user/qm301/class1/temperatureInputs.txt /user/qm301/class1/output
   ```

8. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class1/output/part-r-00000
   ```
