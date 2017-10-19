# Real time Big Data Analytics: Midterm


## Exercises
- Short answers: explain a pig program
- True/False
- Multiple choice
- MapReduce Pseudocode to solve programming problems
- *Shuffle and Sort*, page 197-201
- Match the speed of the drives to the processing power of the server


## Hadoop
### What is Hadoop?
- Distributed *storage* and *compute*
- Developed by Yahoo engineers, and now part of Apache Nutch (web search engine)
- Components: [**HDFS**](#HDFS) + [**MapReduce**](#MapReduce) (+*Hive*+*HBase*+*ZooKeeper*+*Oozie*+*Flume*+...)

### Why do we need Hadoop?
- Longer read/write times of disks (capacity grew quicker than read time)
- Drive business decisions with data

### What problems does it solve?
- Process vast quantities of data in real-time
- Low-cost platform for formulating Bigger Questions consuming Big Data
- Cluster management: At-scale hardware and software management problems
- Tools for analysts, data scientists, machine learning etc.
    

## HDFS
### What is HDFS?
- Apache **H**adoop **D**istributed **F**ile **S**ystem
- Developed by Google (*GFS* -> *Nutch DFS* -> *Apache HDFS*) and now *open source*
- Can de deployed on inexpensive non-custom hardware
- Unsuitable for
    - Low latency access
    - Many small files
    - Multiple writers
    - Updates to offsets within the file

### HDFS architecture
- **Namenodes** (Master): `>= 1 / cluster`
    - Manage filesystem (FS) namespace
    - Maintain FS tree
    - Maintain **metadata** for all files and directories in the FS tree
        - File names
        - Permissions
        - Locations (Datanodes - block #)
        - Saved in memory for fast access            
    - Maintain a list of datanodes on which blocks of a given file are located
    - Must be **resilient to failure**
    - Mark bad HDFS blocks and create **new good replicas**
    - Not involved in bulk data transfer keeping its overhead minimal
    - Additional namenode is a *Standby NameNode for **High Availability** (HA)
        - New way is to automatically switch to the HA namenode in case of failure
- **Datanodes** (workers): `Multiple / cluster`
    - Store and retrieve HDFS blocks
    - Compute checksums over HDFS blocks
    - Report to namenode periodically with a list of their blocks and checksum errors
- **Block size** of 128MB (for *optimal streaming*)
- Metadata
    - Can be modified *concurrently*
    - Synchronized though the **Namenode**
        
### How does HDFS operate?
- HDFS uses its own file system
    - Runs in a separate namespace
    - Comes with its own utilities for file management
    - Blocks for the HDFS files are in a directory managed by the *DataNode* service
    - **Replication of each block across 3 machines**
    - **WORM** model to access file data

### What is the advantage of using HDFS in a Hadoop cluster instead of using traditional networked storage?
- Store replicas of blocks to prevent **data loss from hardware failure**
- No noticeable interruption if a failure occurs
- Allows for **PB+** storage + Very large files (> than a single datanode i.e.)
- Creates and facilitates **parallelization opportunities**
- High performance streaming data access
- Remote parallel processing


## MapReduce
### What is MapReduce?
- Developed by Google in 2004
- Data analysis capability of Hadoop
- Facilitates distributed computing
- Fault tolerance built-in
- Leverages **data locality** for performance
- Batch Query processor
- Assumes the whole dataset will be processed
- Different phases
    - Map phase: interprets data at processing time
        - Schema-free
        - Data not normalized (local operations)
    - Reduce phase
    - Job control program
- Suitable
    - For **write once** - **read many** (*WORM*) applications
    - Unstructured data (log files, plaintext files...)
- Unsuitable
    - If the dataset needs updates (use *HBase* or relational database instead)

### Where does a MapReduce program run?
- Run in parallel on multiple **PM**s or **VM**s

### What is data locality optimization?
- Avoid **copying** data around the cluster whenever possible, as **network bandwidth** is at a premium
- *Bring the computation to the data*: try to run the *map task* on a node where the input data resides in HDFS
- Data is co-located with the **compute node**
- 3 types
    1. Data-local
        - Schedule mapper task to run in the **same server** containing the data block to be processed
        - Each server runs a NodeManager daemon
            - Monitor the node & its running tasks
            - Communicate with the ApplicationMaster, which is issued *containers* by the ResourceManager
            - ApplicationMaster -> *Containers* (Permission slips) -> NodeManager
    - Rack-local (all 3 nodes hosting the block replica are saturated)
        - Schedule mapper task to run in the **same rack** containing the desired block replica
        - >= 1 nodes in the rack contain the desired block replica
        - **Intra-rack** transfer (cheap) to copy block replica to the node which will run the mapper task
    - Non-local, otherwise
        - **Inter-rack** transfer (expensive) to copy block replica to the right rack
            - Go through multiple switches, use precious network resources: slow and expensive
- Rack Awareness
    1. Admin creates a file capturing topology info
        - Creates file relating each host to its enclosing rack & datacenter
    2. Admin supplies utility returning topology info
        - Utility accepts host name and returns `/datacenter/rack`


### Does data locality optimization apply equally to Map tasks and Reduce tasks?
- Map Tasks **benefit** from optimized placement
    - 1 Map task / 1 split (= 1 HDFS block by default)
    - Read their input from HDFS
    - Write data to local disks
- Reduce Tasks **do not generally benefit** from optimized placement
    - 1 Reduce task / outputs from multiple cluster-distributed map tasks
    - Reduce tasks are scheduled to run in containers (**YARN**)
    - Reduce task waits for all mappers' outputs required to be transferred

### How does Hadoop decide where a Map task should run (distance computation)?
- Using the host to rack mapping to compute *distances* between every 2 nodes: 
  ```
  /datacenter-id/rack-id/node-id
  ```
| Distance | Given that                                       |
| -------- | ------------------------------------------------ |
| 0        | 2 containers on the same node                    |
| 2        | 2 containers on different nodes in the same rack |
| 4        | 2 containers on nodes in different racks         |
| 6        | 2 containers on nodes in different datacenters   |
- We basically add 1 each time we move up or back down the hierarchy of (node, rack, datacenter (Network switch))

### What does a Mapper do?
- **Input**: key-value pairs, from the raw dataset
- **Output**: key-value pairs
- **Goal**: *Data conditioning* and *sorting+grouping by key*

### What does a Reducer do?
- **Input**: key-value pairs, from the Mapper
- **Output**: key-value pairs
- **Goal**: *Process the data collected and filtered*

### What are Map tasks and Reduce tasks?
- Each Map task outputs an *intermediate* file on the local hard drive
- Each Reduce task outputs a file in HDFS and writes to it

### What is a Combiner?
- Optimization between the Mapper phase and the Reducer phase
- Acts as a local reducer before transferring to the reducer task

### What is the shuffle phase?
- Sorting of the map tasks' outputs (in memory and is disk)
- Transfer of this sorted data to the reducers

### Speculative execution (what are backup tasks)?
- Master schedules **one** backup execution for each remaining in-progress tasks when a MapReduce phase is nearly complete
- Counters stragglers

## Pig
- Scripting language for exploring large datasets
- Developed by Yahoo and now open source at Apache
- Executes in parallel on Hadoop, generating MapReduce programs
- Suited for batch processing of data
- Describes a Directed Acyclic Graph
    - Edges = data flows
    - Nodes = Operators to process the data

### Advantages
- Faster to code a solution
- Easier to use for non-programmers

### Characteristics
- Pig program can also run in *local mode* for testing
- Pig program reads input and can write output to HDFS
- Schema is optional
- Random reads (or queries) take ~10MS
- Random writes (or updates) are not supported
- Default column separator: **tab**

### Operators
- FILTER: ```bigsales = FILTER sales BY price > 100;```
- BAG: Collection of tuples (unordered)
- DISTINCT: To eliminate duplicates
- LIMIT: ```tenSales = LIMIT sales 10;``` reduces the number of output records
- FLATTEN
- COUNT_STAR: Number of all elements in the bag (including Null)
- Example from homework 5:
   ```pig
   -- Pig script to search inputs file for hackathon, Dec, Chicago, Java
   -- It counts the number of lines each of these term occur in
   
   -- Loads the input file
   LINES = LOAD 'class5/input.txt' AS (line:chararray);
   
   -- Checks each search term for each line. Writes 1 if the term is existing, 0 otherwise. 
   OCCURRENCES = FOREACH LINES GENERATE 'Dec' AS term:chararray, (UPPER(line) matches '.*DEC.*' ? 1 : 0) AS existing;
   TEMP = FOREACH LINES GENERATE 'hackathon' AS term:chararray, (UPPER(line) matches '.*HACKATHON.*' ? 1 : 0) AS existing;
   OCCURRENCES = UNION OCCURRENCES, TEMP;
   TEMP = FOREACH LINES GENERATE 'Chicago' AS term:chararray, (UPPER(line) matches '.*CHICAGO.*' ? 1 : 0) AS existing;
   OCCURRENCES = UNION OCCURRENCES, TEMP;
   TEMP = FOREACH LINES GENERATE 'Java' AS term:chararray, (UPPER(line) matches '.*JAVA.*' ? 1 : 0) AS existing;
   OCCURRENCES = UNION OCCURRENCES, TEMP;
   
   -- Group the (term, 0/1) tuples by term, to sum all the 1s for a particular search term
   OCCURRENCES_GROUP = GROUP OCCURRENCES BY term;
   SOLUTION = FOREACH OCCURRENCES_GROUP GENERATE group AS term:chararray, SUM(OCCURRENCES.existing) AS lines:int;
   
   -- Sorts the results by ascending order
   SOLUTION = ORDER SOLUTION BY term ASC;
   
   -- Displays and stores the results
   DUMP SOLUTION;
   STORE SOLUTION INTO '/user/qm301/class5/output';
   ```
