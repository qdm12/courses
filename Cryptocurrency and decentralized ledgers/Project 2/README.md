# Cryptocurrencies and decentralized ledgers

## Project 2
A project by Quentin McGaw (qm301) and Ismail Mustafa (im969)

- Use [**Maven**](https://maven.apache.org/install.html) to build the dependencies with:

   ```
   cd java
   mvn install
   ```
   
- You can use Eclipse for example as follows:
    1. `File`, `Import...`, `General/Projects from Folder or Archive`, `Next`
    2. `Directory...` and choose the **java** directory of this project, then `Finish`
    3. On the *Navigator*, go to `project1/src/test/bitcoin`
    4. Right click on `MiningSimulation.java` then `Run as...` and `1 JUnit Test`
    
### Understand the code
- Each miner has: (see [BaseMiner.java](src/main/java/edu/nyu/crypto/csci3033/miners/BaseMiner.java))
    - `id`
    - `connectivity`
    - `hashRate`
- Each miner implements the following methods: (see [Miner.java](src/main/java/edu/nyu/crypto/csci3033/miners/Miner.java))
    - `getId()`
    - `getHashRate()`
    - `setHashRate(int hashRate)`
    - `getConnectivity()`
    - `setConnectivity(int connectivity)`
    - `currentlyMiningAt()`: Returns the block the miner is extending (may not be published)
    - `currentHead()`: Returns the block seen as the head of the chain by the miner
    - `blockMined(Block block, boolean isMinerMe)`: Informs the miner of a new block
    - `networkUpdate(NetworkStatistics statistics)`: Update the miner's network to new changes
    - `initialize(Block genesis, NetworkStatistics statistics)`
- A basic behaviour miner is implemented as *CompliantMiner* in [CompliantMiner.java](src/main/java/edu/nyu/crypto/csci3033/miners/CompliantMiner.java)
- The main code running is [MiningSimulation.java](src/test/java/edu/nyu/crypto/csci3033/miners/MiningSimulation.java) as a JUnit test.
    - It runs with 6 [**CompliantMiner**](src/main/java/edu/nyu/crypto/csci3033/miners/CompliantMiner.java) instances
        - First a test with different hash rates and the same connectivity for all
        - Secondly a test with different hash rates and different connectivity for all (randomized)
    - You can check how to simulation works in the **runSimulation** method at the bottom of [*MiningSimulation.java*](src/test/java/edu/nyu/crypto/csci3033/miners/MiningSimulation.java)
        
### Adding attacking miners
1. **51 Percent attacker**
    - Miner performing a 51% attack if it is capable. It extracts as much relative profit as possible.
      *The network may have some natural churn, so the miner status as a majority miner may change.*
    - Implemented in [MajorityMiner.java](src/main/java/edu/nyu/crypto/csci3033/miners/MajorityMiner.java)
    - **Logic**:
        - If the attacker has less than **50%** of the total hash rate, then it acts as a compliant miner and accepts blocks found by other miners.
        - Otherwise, it ignores blocks found by others and keeps on broadcasting its blocks and mining on top of them.
        
2. **Selfish Miner**
    - Miner temporary withholding a block if it is profitable.
      See this strategy in [Chapter 5 of the NBFMG textbook](https://drive.google.com/uc?id=0B4-bDFu_72Beelkxd3VlbXoyd0E&export=download)
    - Implemented in [SelfishMiner.java](src/main/java/edu/nyu/crypto/csci3033/miners/SelfishMiner.java)
    - **Logic**:
        - If the attacker has less than **25%** of the total hash rate, then it acts as a compliant miner and does not withhold any block.
        - Otherwise, it *withholds* its chain (blocks) and *releases* it if:
            - it only withheld 1 block and the main chain caught up with the withheld chain
                - This might depend on the *connectivity* of the miner
            - it withheld more than 1 block and the main chain caught up one block behind our withheld chain
                - This is so to avoid risking a long chain if our *connectivity* is bad
            
3. **Fee Sniping Miner**
    - Miner forking the blockchain to steal unusually valuable blocks when profitable. *When a block with an unusually large transaction fee is mined, your miner should temporarily reject 
      that block and try to re-mine a longer fork where it keeps the large transaction fee for itself.*
    - Implemented in [FeeSnipingMiner.java](src/main/java/edu/nyu/crypto/csci3033/miners/FeeSnipingMiner.java)
    - **Logic**:
        - If the attacker has less than **??%** of the total hash rate, then it acts as a compliant miner and does *fee snipe* any block.
        - Otherwise:
            - if the attacker finds a block, it mines on it and keep broadcasting it
            - if the other miners find a block with a normal value, we accept it and mine on it
            - if the other miners find a block with an unusually high value, we start mining on the parent block of this block
    
4. **Custom Miner**
    - Implemented in [**fm1UCkJwvKfQL7zEEA2Miner.java**](src/main/java/edu/nyu/crypto/csci3033/miners/fm1UCkJwvKfQL7zEEA2Miner.java) (fm1UCkJwvKfQL7zEEA2 is the base58 of *imustafaqmcgaw*)
