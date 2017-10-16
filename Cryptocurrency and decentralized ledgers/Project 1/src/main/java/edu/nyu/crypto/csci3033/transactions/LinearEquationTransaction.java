package edu.nyu.crypto.csci3033.transactions;

import org.bitcoinj.core.NetworkParameters;
import org.bitcoinj.core.Transaction;
import org.bitcoinj.core.Utils;
import org.bitcoinj.script.Script;
import org.bitcoinj.script.ScriptBuilder;

import java.io.File;
import java.math.BigInteger;

import static org.bitcoinj.script.ScriptOpCodes.*;

/**
 * Created by bbuenz on 24.09.15.
 */
public class LinearEquationTransaction extends ScriptTransaction {
    // TODO: Problem 2 we'll use N 12148622
    public LinearEquationTransaction(NetworkParameters parameters, File file, String password) {
        super(parameters, file, password);
    }

    @Override
    public Script createInputScript() {
    		// we want x+y=1214 and |x-y|=8622
		ScriptBuilder builder = new ScriptBuilder();
		// Stack: BOTTOM x, y TOP
		builder.op(OP_2DUP); // Stack: x, y, x, y		
		builder.op(OP_ADD); // Stack: x, y, x+y
		builder.number(1214); // Stack: x, y, x+y, 1214
		builder.op(OP_EQUALVERIFY); // Stack: x, y
		builder.op(OP_SUB); // Stack: x-y
		builder.op(OP_ABS); // Stack: |x-y|
        builder.number(8622); // Stack: |x-y|, 8622
        builder.op(OP_EQUAL); // Stack:
        return builder.build();
    }

    @Override
    public Script createRedemptionScript(Transaction unsignedScript) {
    		//  x + y = 1214  
    		// |x - y| = 8622  => |(1214 - y) - y| = 8622 => |1214 - 2y| = 8622 => y = -3704 is a solution
    		//
    		// |x - y| = 8622 => |x + 3704| = 8622 => x = 4918 is a solution
    		ScriptBuilder builder = new ScriptBuilder();
    		builder.number(4918);
    		builder.number(-3704);
    		return builder.build();
    }

    private byte[] encode(BigInteger bigInteger) {
        return Utils.reverseBytes(Utils.encodeMPI(bigInteger, false));
    }
}
