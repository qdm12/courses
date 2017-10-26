package bitcoin.miners;

import bitcoin.blockchain.Block;
import bitcoin.blockchain.NetworkStatistics;

public class FeeSnipingMiner extends BaseMiner implements Miner {
    private Block myHead, mainHead;
    private double feeThreshold = 9.5;

    public FeeSnipingMiner(String id, int hashRate, int connectivity) {
        super(id, hashRate, connectivity);
    }
    
    public void debugprint(boolean debug, String s) {
        if (debug) {
            System.out.println(s);
        }
    }

    @Override
    public Block currentlyMiningAt() {
        return this.myHead;
    }

    @Override
    public Block currentHead() {
        return this.mainHead;
    }

    @Override
    public void blockMined(Block block, boolean isMinerMe) {       
        if (isMinerMe) {
            this.myHead = this.mainHead = block;
        } else if (block.getHeight() > this.mainHead.getHeight()) { //TODO: maybe >= if another fee sniper
            this.mainHead = block;
            if (this.myHead.getHeight() <= this.mainHead.getHeight()) {
                // we are 1 or more blocks behind
                // or we are not fee sniping (= 0)
                // m - h >= 0 => m >= h
                this.myHead = this.mainHead;
            }
            if (block.getBlockValue() > this.feeThreshold) {
                this.myHead = block.getPreviousBlock();
            }
        }
    }


    @Override
    public void initialize(Block genesis, NetworkStatistics networkStatistics) {
        this.myHead = this.mainHead = genesis;
    }

    @Override
    public void networkUpdate(NetworkStatistics statistics) {
    }
}
