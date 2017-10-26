package bitcoin.miners;

import bitcoin.blockchain.Block;
import bitcoin.blockchain.NetworkStatistics;

public class MajorityMiner extends BaseMiner implements Miner {
    private Block mainHead;
    private double hashRateShare = 1.00;

    public MajorityMiner(String id, int hashRate, int connectivity) {
        super(id, hashRate, connectivity);
    }

    @Override
    public Block currentlyMiningAt() {
        return this.mainHead;
    }

    @Override
    public Block currentHead() {
        return this.mainHead;
    }

    @Override
    public void blockMined(Block block, boolean isMinerMe) {
        if (block.getHeight() > this.mainHead.getHeight()) {
            if(isMinerMe) {
                this.mainHead = block;
            } else if (hashRateShare < 0.5) {
                // we only care about others' block if we have < 0.5 hashrate share
                this.mainHead = block;
            }
        }
    }


    @Override
    public void initialize(Block genesis, NetworkStatistics networkStatistics) {
        this.mainHead = genesis;
    }

    @Override
    public void networkUpdate(NetworkStatistics statistics) {
        this.hashRateShare = (double)getHashRate() / (double)statistics.getTotalHashRate();
    }
}
