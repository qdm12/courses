package edu.nyu.crypto.csci3033.transactions;

import org.bitcoinj.core.Base58;
import org.bitcoinj.core.DumpedPrivateKey;
import org.bitcoinj.core.ECKey;
import org.bitcoinj.core.NetworkParameters;
import org.bitcoinj.core.Transaction;
import org.bitcoinj.core.Utils;
import org.bitcoinj.crypto.TransactionSignature;
import org.bitcoinj.script.Script;
import org.bitcoinj.script.ScriptBuilder;

import java.io.File;

import static org.bitcoinj.script.ScriptOpCodes.*;

/**
 * Created by bbuenz on 24.09.15.
 */
public class MultiSigTransaction extends ScriptTransaction {
    // TODO: Problem 3
    public DumpedPrivateKey customer1, customer2, customer3, bank;

    public MultiSigTransaction(NetworkParameters parameters, File file, String password) {
        super(parameters, file, password);
        // The comments to the right are corresponding addresses
        customer1 = DumpedPrivateKey.fromBase58(parameters, "cTsinK4dtbchFq22kDLWfQpqKk72w7vZ5pp7LFLJM9eYQdSD6vTw"); // n2ifjSrNeTrJZf34RGjruETva79Ud5BsSF
        customer2 = DumpedPrivateKey.fromBase58(parameters, "cSBiCgmThhoAYWUikSmm2XuiEFhQZy46J1jgNnVm36fjuozrr8jm"); // mh5yAGm1Co9JSexh75YDyCupkvKX1ggXq5
        customer3 = DumpedPrivateKey.fromBase58(parameters, "cQJbPPLd63kVXDgqYm4jTL1sCBMHVb8mABRBntHwiz8gEFj48Yvz"); // mhFPb5n9mAGjajh3ZrsbyGh68qJTCbcFXE
        bank = DumpedPrivateKey.fromBase58(parameters, "cSU4V5JeWV9kgbZUuVjJLZwZDP4KGgVCDHDSKccTXWRstC5C1Xmf"); // n4r8gbkeehMhQwVE54QZKuYrXgFy3TuLyF
    }

    @Override
    public Script createInputScript() {      
		ScriptBuilder builder = new ScriptBuilder();
		
		// ------ MultiSig -----------
		builder.number(1);
		builder.data(customer1.getKey().getPubKey());
		builder.data(customer2.getKey().getPubKey());
		builder.data(customer3.getKey().getPubKey());
		builder.number(3);
		builder.op(OP_CHECKMULTISIGVERIFY);
		// ------ MultiSig -----------
		
		// ------- pub key hash for bank --------
		builder.op(OP_DUP);
		builder.op(OP_HASH160);
		builder.data(bank.getKey().getPubKeyHash());
		builder.op(OP_EQUALVERIFY);
		builder.op(OP_CHECKSIG);
		// ------- pub key hash for bank --------
		
        return builder.build();
    }

    @Override
    public Script createRedemptionScript(Transaction unsignedTransaction) {
    		ScriptBuilder builder = new ScriptBuilder();
    		
    		// ------- pub key hash for bank and signature --------
    		TransactionSignature txSigBank = sign(unsignedTransaction, bank.getKey());
    		builder.data(txSigBank.encodeToBitcoin());
    		builder.data(bank.getKey().getPubKey());
    		// ------- pub key hash for bank and signature --------
    		
    		// ------ MultiSig -----------
    		TransactionSignature txSigCustomer1 = sign(unsignedTransaction, customer1.getKey());
    		builder.data(new byte[] {});
    		builder.data(txSigCustomer1.encodeToBitcoin());
    		// ------ MultiSig -----------
    		
        return builder.build();
    }
}
