# Real time Big Data Analytics: Homework 5

## Dumbo Pig WordCount
This counts the number of lines a certain search term occurs in.

1. Log into Dumbo with:

   ```bash
   ssh -t qm301@hpc2.nyu.edu ssh qm301@dumbo.es.its.nyu.edu
   ```
   
2. Launch **Grunt** for **Pig** with:

   ```bash
   pig
   ```
   
   so that you can test commands one by one if you want to.
   
3. Paste the content of the Pig script file and the input with the following:

   ```bash
   nano script.pig
   nano input.txt
   ```

4. Put the input file on the HDFS

   ```bash
   hdfs dfs -mkdir -p /user/qm301/class5
   hdfs dfs -put -f input.txt /user/qm301/class5
   ```
   
5. Run the Pig script with:

   ```bash
   pig script.pig
   ```

6. Check that the output is correct:

   ```bash
   hdfs dfs -cat /user/qm301/class5/output/part-r-00000
   ```