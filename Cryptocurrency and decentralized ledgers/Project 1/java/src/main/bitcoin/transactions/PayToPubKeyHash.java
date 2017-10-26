package bitcoin.transactions;

import org.bitcoinj.core.DumpedPrivateKey;
import org.bitcoinj.core.NetworkParameters;
import org.bitcoinj.core.Transaction;
import org.bitcoinj.crypto.TransactionSignature;
import org.bitcoinj.script.Script;
import org.bitcoinj.script.ScriptBuilder;

import java.io.File;

import static org.bitcoinj.script.ScriptOpCodes.*;

public class PayToPubKeyHash extends ScriptTransaction {
    DumpedPrivateKey vanityKey;
    
    public PayToPubKeyHash(NetworkParameters parameters, File file, String password) {
        super(parameters, file, password);
        vanityKey = DumpedPrivateKey.fromBase58(parameters, "5Kh5kV3uQasvcHkZyuGxYga6NvmNNqkAXTZvjNen7z64qEm4r2X");
    }

    @Override
    public Script createInputScript() {
        // OP_DUP OP_HASH160 <Vanity Public Key Hash> OP_EQUAL OP_CHECKSIG
        ScriptBuilder builder = new ScriptBuilder();
        builder.op(OP_DUP);
        builder.op(OP_HASH160);
        builder.data(vanityKey.getKey().getPubKeyHash());
        builder.op(OP_EQUAL);
        builder.op(OP_CHECKSIG);
        return builder.build();
    }

    @Override
    public Script createRedemptionScript(Transaction unsignedTransaction) {
        // <Vanity Signature> <Vanity Public Key>
        TransactionSignature txSig = sign(unsignedTransaction, vanityKey.getKey());
        ScriptBuilder builder = new ScriptBuilder();
        builder.data(txSig.encodeToBitcoin());
        builder.data(vanityKey.getKey().getPubKey());
        return builder.build();
    }
}
