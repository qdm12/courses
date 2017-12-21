# Real time Big Data Analytics: Final exam


## Exercises

- Short answers
- Programming questions
- True/False
- Multiple choice
- Hive code to interpret


## Hadoop

- Components: [**HDFS**](#hdfs) + [**MapReduce**](#mapreduce) (+*Hive*+*HBase*+*ZooKeeper*+*Oozie*+*Flume*+...)
- Hadoop cluster drawing
    - Node Manager ?
    - Resource Manager ?
    - Application master service ?
- Hadoop in YARN
- Hadoop in MR1
- Failure cases are handled with... and detected with...
- Failures in YARN ?
- Failures in MR2 ?


## HDFS

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
    - Additional namenode is a *Standby NameNode for **High Availability** * (HA)
    - Not involved in bulk data transfer keeping its overhead minimal
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


## MapReduce

### How does it work?

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
- Run in parallel on multiple **PM**s or **VM**s


## HBase

### NoSQL

- **N**ot **O**nly **S**QL databases, for storing huge datasets effectively
- No guarantee of ACID properties
- **Eventual** consistency
- Designed to be distributed and to scale up with commodity servers
- Flexible schema
- Optimized for retrieval and append operations (key-value store)
- Use cases
    - Indexing huge amount of documents
    - Streaming media

### Hbase

- Distributed column-family-oriented database built on top of HDFS
- Suitable for:
    - Billions of rows, millions of columns
    - Near realtime / soft realtime read/write random access
    - Sparse data as unpopulated fields are not allocated space
- Distributed, fault-tolerant and data is *sharded* across many servers
- Versioning of cells (fixed number of versions)
- Not fully ACID compliant
- No JOIN operations
- See the corresponding [**homework**](../homework9#hbase)

### Architecture

- Master nodes
    - Manages a cluster of *regionservers* (workers)
    - Bootstraps initial install
    - Assigns regions to registered regionservers
    - Recovers regionserver failures    
- Worker nodes
    - Carry >= 0 regions (**region** = subset of a table's row)
    - Handle read/write requests
    - Perform region splits if needed (and tell Master)
- Easily scalable vs RDBMS

## Hive

- Data warehousing framework developed by Facebook built on top of MapReduce
- HiveQL is a dialect of SQL
- Converts your query into one or more MapReduce jobs
    - Batch oriented
    - Long response times
- User data is organized into tables
- Unlike RDBMS, it uses schema on read (enforced when the query is issued)
    - Faster
    - Flexible: Multiple simultaneous schemas
- See the corresponding [**homework**](../homework8#hive)
- External vs internal tables??
- Multi table insert, partitions, schemas??

## Impala

- Uses massively parallel processing, using a lot of memory (unlike Hive)
- Daemons running on all nodes caching HDFS data (no cold start unlike Hive)
- Not fault resistant

## Sqoop

- Tool to move data between HDFS and an external database (i.e. MySQL)
    - Also supports Hive tables (schema inference)
- Uses MapReduce job with 4 map tasks in parallel on worker nodes

## Flume

- Distributed system for moving large streaming datasets to HDFS reliably
- Flume nodes can be arranged to form a customized topology

## Oozie

- Workflow control in Hadoop and Spark, through an XML file

## Spark

- Cluster computing system for fast-running analytics
- Spark API + Interactive shell accepting Python or Scala
- Abstraction **RDD** (Resilient distributed dataset) in memory
- Advantages vs Hadoop MapReduce
    - Wider class of applications
    - Efficiently handles multi-pass applications (iterative algorithms)

## Cloud

- Hadoop cluster in public cloud
    - + Scalable
    - + Affordable
    - - Shared physical infrastructure
    - - No control over security / availability / visibility

## Distributed

- Behaviors of autonomic computing
    1. Self-configuring
    2. Self-healing (when service or node fails)
    3. Self-protecting (self redundant health assessments)
    4. Self-optimizing (self performance assessments: **load balancing**)