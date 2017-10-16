package edu.nyu.crypto.csci3033;

import edu.nyu.crypto.csci3033.transactions.*;
import org.bitcoinj.core.*;
import org.bitcoinj.kits.WalletAppKit;
import org.bitcoinj.params.MainNetParams;
import org.bitcoinj.params.TestNet3Params;
import org.bitcoinj.script.Script;
import org.junit.Assert;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.math.BigInteger;

/**
 * Created by bbuenz on 23.09.15.
 */
// TESTNET ADDRESS: mzdrXHiUScpg8Hb1D2JNmoPQGdCmnbuP3E
// TESTNET PRIVATE: cRT4mYCCZgNBRv9JW36AtaQ2Bwp55NoJBYcdiBzjGnxoD1fMRXsG
public class ScriptTests {
    // TODO: Change this to true to use mainnet.
    private boolean useMainNet = false;
    // TODO: Change this to the address of the testnet faucet you use.
    // https://testnet.manu.backend.hamburg/faucet
    private static final String faucetAddress = "2N1Xfu1zHDShso2XkfQANQVLMoLRtFeqcF5";

    private String wallet_name;
    private NetworkParameters networkParameters;
    private WalletAppKit kit;

    private static final Logger LOGGER = LoggerFactory.getLogger(ScriptTests.class);

    public ScriptTests() {
        if (useMainNet) {
            networkParameters = new MainNetParams();
            wallet_name = "main-wallet";
            LOGGER.info("Running on mainnet.");
        } else {
            networkParameters = new TestNet3Params();
            wallet_name = "test-wallet";
            LOGGER.info("Running on testnet.");
        }
        kit = new WalletAppKit(networkParameters, new File(wallet_name), "password");   
    }
    
    public void downloadBlockchain() {
        LOGGER.info("Starting to sync blockchain. This might take a few minutes");
        kit.setAutoSave(true);
        kit.startAsync();
        kit.awaitRunning();
        kit.wallet().allowSpendingUnconfirmedTransactions();
        LOGGER.info("Synced blockchain.");
        LOGGER.info("You've got " + kit.wallet().getBalance() + " in your pocket"); 
    }
    
    public void OverwritePrivateKey(String privateKey) {
    	// creates new key
        ECKey newkey;
        if (privateKey.length() == 51 || privateKey.length() == 52) {
            DumpedPrivateKey dumpedPrivateKey = DumpedPrivateKey.fromBase58(networkParameters, privateKey);
            newkey = dumpedPrivateKey.getKey();
        } else {
            BigInteger privKey = Base58.decodeToBigInteger(privateKey);
            newkey = ECKey.fromPrivate(privKey);
        }
    	// deletes all keys in wallet
    	for(ECKey key : kit.wallet().getImportedKeys()) {
    		kit.wallet().removeKey(key);
    	}
        // Imports key
        kit.wallet().importKey(newkey);
    }

    @Test
    public void printAddress(){
        downloadBlockchain();
//        OverwritePrivateKey("5KGGiSmx1b6HVCgPyC4oAyNYffzxoH9L5m5yAjFKfYMd2LTtRjH");
//        OverwritePrivateKey("cRT4mYCCZgNBRv9JW36AtaQ2Bwp55NoJBYcdiBzjGnxoD1fMRXsG");
	    	for(ECKey key : kit.wallet().getImportedKeys()) {
	            LOGGER.info("Found address " + key.toAddress(networkParameters).toString() + 
	            		" with public key " + key.getPublicKeyAsHex() + 
	            		" and private key " + key.getPrivateKeyAsHex());
	    	}
        LOGGER.info("Your address is {}", kit.wallet().currentReceiveAddress());
        kit.stopAsync();
        kit.awaitTerminated();
    }

    private void testTransaction(ScriptTransaction scriptTransaction) throws InsufficientMoneyException {
        final Script inputScript = scriptTransaction.createInputScript();
        Transaction transaction = scriptTransaction.createOutgoingTransaction(inputScript, Coin.CENT);
        TransactionOutput relevantOutput = transaction.getOutputs().stream().filter(to -> to.getScriptPubKey().equals(inputScript)).findAny().get();
        Transaction redemptionTransaction = scriptTransaction.createUnsignedRedemptionTransaction(relevantOutput, scriptTransaction.getReceiveAddress());
        Script redeemScript = scriptTransaction.createRedemptionScript(redemptionTransaction);
        scriptTransaction.testScript(inputScript, redeemScript, redemptionTransaction);
        redemptionTransaction.getInput(0).setScriptSig(redeemScript);
        scriptTransaction.sendTransaction(transaction);
        scriptTransaction.sendTransaction(redemptionTransaction);
    }

    // TODO: Uncomment this once you have coins on mainnet or testnet to check that transactions are working as expected.
//    @Test
//    public void testPayToPubKey() throws InsufficientMoneyException {
//        try (ScriptTransaction payToPubKey = new PayToPubKey(networkParameters, new File(wallet_name), "password")) {
//            testTransaction(payToPubKey);
//
//        } catch (Exception e) {
//            e.printStackTrace();
//            Assert.fail(e.getMessage());
//        }
//    }

    // TODO: Uncomment this when you are ready to test PayToPubKeyHash.
//    @Test
//    public void testPayToPubKeyHash() throws InsufficientMoneyException {
//        try (ScriptTransaction payToPubKeyHash = new PayToPubKeyHash(networkParameters, new File(wallet_name), "password")) {
//            testTransaction(payToPubKeyHash);
//        } catch (Exception e) {
//            e.printStackTrace();
//            Assert.fail(e.getMessage());
//        }
//    }

    // TODO: Uncomment this when you are ready to test LinearEquationTransaction.
//    @Test
//    public void testLinearEquation() throws InsufficientMoneyException {
//        try (LinearEquationTransaction linEq = new LinearEquationTransaction(networkParameters, new File(wallet_name), "password")) {
//            testTransaction(linEq);
//        } catch (Exception e) {
//            e.printStackTrace();
//            Assert.fail(e.getMessage());
//        }
//    }

    // TODO: Uncomment this when you are ready to test MultiSigTransaction.
//    @Test
//    public void testMultiSig() throws InsufficientMoneyException {
//        try (ScriptTransaction multiSig = new MultiSigTransaction(networkParameters, new File(wallet_name), "password")) {
//            testTransaction(multiSig);
//        } catch (Exception e) {
//            e.printStackTrace();
//            Assert.fail(e.getMessage());
//        }
//    }

    // TODO: Uncomment this when you are ready to send money back to Faucet on testnet.
//    @Test
//    public void sendMoneyBackToFaucet() throws AddressFormatException, InsufficientMoneyException {
//        if (useMainNet) {
//            return;
//        }
//        downloadBlockchain();
//        Transaction transaction = kit.wallet().createSend(new Address(networkParameters, faucetAddress), kit.wallet().getBalance().subtract(Coin.MILLICOIN));
//        kit.wallet().commitTx(transaction);
//        kit.peerGroup().broadcastTransaction(transaction);
//        kit.stopAsync();
//        kit.awaitTerminated();
//    }
}
