# Real time Big Data Analytics: Homework 9

## HBase

1. Download the Cloudera Quickstart VM from [cloudera.com](https://www.cloudera.com/downloads/quickstart_vms/5-10.html). **Note** that your machine has to have more than **4GB of RAM** for it to work.
2. Check *HMaster*, *HRegionServer* and *QuorumPeerMain* are running already
    ```bash
    sudo jps
    ```
3. Launch the HBase shell
    ```bash
    hbase shell
    ```
4. Enter the following commands
    ```bash
    status
    whoami
    create 'table1', 'family1'
    describe 'table1'
    alter 'table1', NAME=>'family1', VERSIONS =>2
    put 'table1', '1000', 'family1:col1', 'value1'
    put 'table1', '2000', 'family1:col1', 'value2-1'
    scan 'table1'
    put 'table1', '2000', 'family1:col1', 'value2-2'
    count 'table1'
    scan 'table1'
    scan 'table1', VERSIONS => 3
    get 'table1', '2000'
    get 'table1', '2000', {COLUMN=>'family1:col1', VERSIONS=>2}
    ```  
    Note that all the 2 versions are only shown when `VERSIONS=>2` is mentioned
5. Now try this:
    ```bash
    put 'table1', '2000', 'family1:col1', 'value2-3'
    get 'table1', '2000', {COLUMN=>'family1:col1', VERSIONS=>3}
    ```
    This won't show more than 2 versions, because the table was defined to only store the 2 last versions