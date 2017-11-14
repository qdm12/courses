# Real time Big Data Analytics: Homework 8

## Summary of research paper
*A Fistful of Bitcoins: Characterizing Payments Among Men with No Names*

See [homework.tex](homework.tex) for the summary

## Hive and Impala

1. Download the Cloudera Quickstart VM from [cloudera.com](https://www.cloudera.com/downloads/quickstart_vms/5-10.html). **Note** that your machine has to have more than **4GB of RAM** for it to work.
2. Setup a working directory and go to this one with:
   ```bash
   mkdir -p ~/homework8
   cd ~/homework8
   ```
   
3. Paste the content of the input file
   ```bash
   nano input.txt
   ```
  
### Hive

1. Put the input file on the HDFS
    ```bash
    hdfs dfs -mkdir -p hiveInput
    hdfs dfs -put input.txt hiveInput
    ```
   
2. Create a Hive external table
    ```sql
    beeline -u jdbc:hive2://quickstart:10000/default -n cloudera -d org.apache.hive.jdbc.HiveDriver
    
    CREATE EXTERNAL TABLE w1 (data1 string, year int, data2 string, temperature int, quality tinyint, data3 string)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    LOCATION '/user/cloudera/hiveInput/';
    
    SHOW TABLES;
    DESCRIBE w1;
    ```
    
3. View the data with **HiveQL**
    ```sql
    SELECT * FROM w1 WHERE year >= 1949;
    SELECT DISTINCT year FROM w1;
    SELECT DISTINCT year FROM w1; -- Still slow
    SELECT w.year, w.temp
    FROM (SELECT year, MAX(temperature) AS temp FROM w1 GROUP BY year) w;
    ```
   
4. You can also access files directly from the Hive command line
    ```sql
    dfs -cp hiveInput/input.txt hiveInput/input2.txt;
    SELECT * FROM w1;
    ```
   
### Impala

1. Put the input file on the HDFS
    ```bash
    hdfs dfs -mkdir -p impalaInput
    hdfs dfs -put input.txt impalaInput
    ```
   
2. Start Impala and check for Hive's tables
    ```sql
    impala-shell
    SHOW TABLES;
    invalidate metadata; -- force Impala to update its metadata
    SHOW TABLES;   
    ```
    
### 
    
3. Create a table
    ```sql
    CREATE EXTERNAL TABLE w10 (data1 string, year int, data2 string, temperature int, quality tinyint, data3 string)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    LOCATION '/user/cloudera/impalaInput/';
    
    DESCRIBE w10;
    ```
    
4. Send queries
    ```sql
    select * from w10 where year > 1949;
    SELECT DISTINCT year FROM w1;
    SELECT DISTINCT year FROM w1; -- Way faster than Hive the 2nd time
    ```
    
### Impala on Dumbo
1. Log into Dumbo with:
   ```bash
   ssh -t qm301@hpc2.nyu.edu ssh qm301@dumbo.es.its.nyu.edu
   ```
   
2. Launch Impala with the following commands:
   ```bash
   impala-shell
   connect compute-1-1;
   ```