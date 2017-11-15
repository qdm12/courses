# Real time Big Data Analytics: Homework 10

## Spark

1. Download the Cloudera Quickstart VM from [cloudera.com](https://www.cloudera.com/downloads/quickstart_vms/5-10.html). **Note** that your machine has to have more than **4GB of RAM** for it to work.

2. Put the inputs in HDFS with:
    ```bash
    hdfs dfs -put inputs
    ```
   
3. Launch the Spark shell with:
    ```bash
    spark-shell
    ```
    
4. Enter the following commands:
    1. `sc` to display the *SparkContext* object
    2. `sc.` + **TAB** to display possible methods on that object
    3. `val all = sc.textFile("/user/cloudera/inputs")` to read the data in a Spark RDD
    4. `all.count()` to count the total number of lines (and to actually create and materialize the RDD)
    5. `all.take(6)` to display **6** lines
    6. `all.take(6).foreach(println)` to display **6** lines in the correct way
    7. `var errors = all.filter(line => line.contains("error")` to search all lines containing the word `error`
    8. `errors.count()` to count how many lines were found