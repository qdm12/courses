package bitcoin.miners;

import bitcoin.blockchain.Block;
import bitcoin.blockchain.NetworkStatistics;

public class SelfishMiner extends BaseMiner implements Miner {
    private Block myHead, mainHead;
    private double hashRateShare = 1.00;
    private boolean enoughblocks = false;

    public SelfishMiner(String id, int hashRate, int connectivity) {
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

    @Override
    public void blockMined(Block block, boolean isMinerMe) {
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
            if (this.hashRateShare >= 0.25) {
                if (blocksAhead < 0) {
                    this.myHead = this.mainHead;
                } else if (blocksAhead == 0) { // only when network catches us when we're 1 ahead ONCE
                    this.mainHead = this.myHead; // we try desperately this
                } else if (blocksAhead == 1 && this.enoughblocks) {
                    this.enoughblocks = false;
                    this.mainHead = this.myHead;
                } else {
                    this.enoughblocks = true;
                }
            } else { // compliant miner
                this.mainHead = blocksAhead > 0 ? this.myHead : this.mainHead;
            }
        }
    }

    @Override
    public void initialize(Block genesis, NetworkStatistics networkStatistics) {
        this.myHead = this.mainHead = genesis;
    }

    @Override
    public void networkUpdate(NetworkStatistics statistics) {
        this.hashRateShare = (double)getHashRate() / (double)statistics.getTotalHashRate();
    }
}
