package bitcoin.miners;

import java.util.HashMap;

import bitcoin.blockchain.Block;
import bitcoin.blockchain.NetworkStatistics;

public class fm1UCkJwvKfQL7zEEA2Miner extends BaseMiner implements Miner {
    private Block myHead, mainHead;
    private double hashRateShare = 0.4;
    
    private boolean enoughBlocks = false; // Selfish Miner
    private double feeThreshold = 9.5; // Fee Sniping
    
    private boolean busy = false;

    public fm1UCkJwvKfQL7zEEA2Miner(String id, int hashRate, int connectivity) {
        super(id, hashRate, connectivity);
    }

    @Override
    public Block currentlyMiningAt() {
        return this.myHead;
    }

    @Override
    public Block currentHead() {
        return this.mainHead;
    }    
    
    private void feeSnipingMining(Block block, boolean isMinerMe) {
        if (isMinerMe) {
            this.myHead = this.mainHead = block;
        } else if (block.getHeight() > this.mainHead.getHeight()) { //TODO: maybe >= if another fee sniper
            this.mainHead = block;
            if (this.myHead.getHeight() <= this.mainHead.getHeight()) {
                // we are 1 or more blocks behind
                // or we are not fee sniping (= 0)
                this.myHead = this.mainHead;
            }
            if (block.getBlockValue() > this.feeThreshold) {
                this.myHead = block.getPreviousBlock();
            }
        }
    }
    
    
    private void selfishMining(Block block, boolean isMinerMe) {
        this.busy = true;
        boolean found = true;
        if (isMinerMe && block.getHeight() > this.myHead.getHeight()) { // we find a block
            this.myHead = block;
        } else if (block.getHeight() > this.mainHead.getHeight()) { // they find a block
            this.mainHead = block;
        } else { // no block found
            found = false;
        }
        if (found) {
            int blocksAhead = this.myHead.getHeight() - this.mainHead.getHeight();
            if (blocksAhead < 0) {
                this.myHead = this.mainHead; // we give up
                this.busy = false;
            } else if (blocksAhead == 0) { // only when network catches us when we're 1 ahead ONCE
                this.mainHead = this.myHead; // we try desperately this
                this.busy = false;
            } else if (blocksAhead == 1 && this.enoughBlocks) {
                this.enoughBlocks = false;
                this.mainHead = this.myHead;
                this.busy = false;
            } else {
                this.enoughBlocks = true;
                this.busy = true;
            }
        }
    }
    
    private void compliantMining(Block block, boolean isMinerMe) {
        if (block.getHeight() > this.mainHead.getHeight()) {
            this.mainHead = this.myHead = block;
        }
    }
    
    private boolean isLargestHashRateShare(Block block, String id) {
            HashMap<String, Integer> blocksPerId = new HashMap<String, Integer>();
        HashMap<String, Double> hashRateSharePerId = new HashMap<String, Double>();
        
        Integer blockCount = 0;
        while (block != null) {
                 String id1 = block.getMinedBy();
            Integer blocks = blocksPerId.get(id1);
            if (blocks == null) {
                 blocksPerId.put(id1, 1);
             } else {
                 blocksPerId.put(id1, blocks + 1);
             }
             block = block.getPreviousBlock();
             blockCount++;
             if (blockCount > 50) {
                     break;
             }
        }
        
        String largestId = "";
        double largest = -1;
        for (String key : blocksPerId.keySet()) {
                Integer numBlocks = blocksPerId.get(key);
                double hashRateShare =  (double)numBlocks / (double)blockCount;
                hashRateSharePerId.put(key, hashRateShare);
                if (hashRateShare > largest) {
                    largest = hashRateShare;
                    largestId = key;
                }
        }
        return id == largestId;   
    }

    @Override
    public void blockMined(Block block, boolean isMinerMe) {           
        if (block.getBlockValue() > this.feeThreshold && this.isLargestHashRateShare(block, getId())) { // abort anything for fee sniping
            this.feeSnipingMining(block, isMinerMe);
        } else if (this.hashRateShare >= 0.25 && ! this.busy) {
            this.selfishMining(block, isMinerMe);
        } else { // if hashrate < 0.25 and no high reward block
            this.compliantMining(block, isMinerMe);
        }
    }


    @Override
    public void initialize(Block genesis, NetworkStatistics networkStatistics) {
        this.myHead = this.mainHead = genesis;
    }

    @Override
    public void networkUpdate(NetworkStatistics statistics) {
        hashRateShare = (double)getHashRate() / (double)statistics.getTotalHashRate();
    }
}
