# CSCI-GA 3033-019 - Cryptocurrencies and decentralized ledgers

A project by Quentin McGaw (qm301) and Ismail Mustafa (im969)

## Project 1

- Use **Maven** to build the dependencies with:

   ```
   mvn install
   ```

### Exercise 1
- We used a multi core program we wrote in Python, but that was only processing up to 100 addresses per second
- We then used [VanityGen](https://github.com/samr7/vanitygen) to find the vanity address, which is way faster:
    - Clone it with Git:
    
      ```shell
      git clone https://github.com/samr7/vanitygen.git
      ```
      
    - Install necessary packages with:
    
      ```shell
      sudo apt-get install libssl-dev
      sudo apt-get install libpcre3-dev
      ``` 
      
    - Run it with:
    
      ```shell
      cd vanitygen
      ./vanitygen 1prefix
      ```

- The vanity address that we generated is 1imqmx9SaEVBeaonqShuDL34k9oYj8QWk with private key  5Kh5kV3uQasvcHkZyuGxYga6NvmNNqkAXTZvjNen7z64qEm4r2X.
- The prefix of the vanity address is 1imqm where im are the initials for Ismail Mustafa and qm are the initials for Quentin McGaw.
- We weren't able to get this to broadcast because bitcoinJ didn't detect the private key that we manually imported to the wallet.
      
### Exercise 2
// Locking
21:26:31.904 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Transaction hex you can directly submit this to a block explorer:
01000000029ac0b1436783cc2c18065518bd5ec77b9cb603d6e18c78cbc5352c22ee4d4110000000006a473044022070fd271e33f65502331c9d4502befeecc462a64d9fc38a2823ce6ebcab4e557502203b3c0e1837188067f1baceda5a10deadfe35d761d4063a81e3e24ebb04d09339012103083d133627217696fffd504d0c85b4203d4864fc8e994cd7cd2fdf78afc210e4ffffffff3b250f26b3453d14886aba51bce16986317eed10e02c8434249b8de9d262e28e000000006a473044022021fc70038e740d891e289da1ec38fcea75eef8eaab068add88685c5c279554a7022023b24a90ff3793e9e082c9809520bcd2b2c897ec532ab989695cae90b9dcb49b012102112189562224138133786aad949a3a80734e85f1094dbbaa527f0c6dc74b51f7ffffffff02545da003000000001976a914093c754085738b9bf0da10214876681d1d6fb61688ac40420f00000000000c6e9302be0488949002ae218700000000
21:26:31.942 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Broadcasted transaction: f8c1f5a09f5a129f69dda0ba0b0a7650dfe4f9a915890f44dc1f7021a6014ace

// Unlocking
21:26:31.942 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Transaction hex you can directly submit this to a block explorer:
0100000001ce4a01a621701fdc440f8915a9f9e4df50760a0bbaa0dd699f125a9fa0f5c1f8010000000602361302788effffffff0100350c00000000001976a91436cc8c8af4e51769dc9ebe57b2fe3758126a062988ac00000000
21:26:31.953 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Broadcasted transaction: c6790c526fd15ed18f7b0e77ceffb6f009689b46de097b9080b18752e8b34e9c

### Exercise 3
// Locking
19:11:56.096 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Transaction hex you can directly submit this to a block explorer:
0100000002273759ee3a5ab3e8390b7a65e007e187c4b1e0f4069daded4394302ba1d54869000000006b483045022100af61ad73ae9388590203b9d00581f8740f66c11470c6a8eca1fd904a043b5d3402204d02e12fa12aa01903cf77e940ca22788a6b674e5bedb8f296f05e6a313e64f50121027e29228a3d48553dbc367af637102d01159adef235c1b3cac149703c29deee55ffffffffbfe1d560193c31a300fc11bccefa6a75564b3f5b1896a38bc6e665a22f83c5b1000000006a473044022052134cb1e201bd90e603ca995758a55c0b8558955bbd14eb7004fcd74fc6f451022059311e7c224479fe7ef57da730452744e3ab483a67d9d5cb43b9f77136736e81012103dff9b33c7bb77fdb5316d6ad3bd95650eb6007c6816c3b441db1e71153d4c785ffffffff02dc6b0800000000001976a914d2b83f09837b0cd9918a73a95ad285367175787888ac40420f000000000082512103716b2e6f88ba2b0917d752981c7ff83e3551f9a6dad3ca578bf4851416f352642103c90885926d4956c118f97f780c20fa3619ce59a28ccc73ac3188d769880074c42102836028fe5fed79042be4a804f6e292597ac2be19ad346236da2c06dcad278f7e53af76a9145c0f9e55227d94ecdbce9e37ddb3244d327ca8ae88ac00000000
Broadcasted transaction: 20cf48b1e5fcc136b3439b714bafd634cabcb8b4638fbc4ca8948c203275fad8

// Unlocking
19:11:56.105 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Transaction hex you can directly submit this to a block explorer:
0100000001d8fa7532208c94a84cbc8f63b4b8bcca34d6af4b719b43b336c1fce5b148cf2001000000b44830450221009b560c79ce5efe493248929d86142bc45e2e9964d6873f16fcc6d510008979d602204c2d63a703222154a00139c41d88790b63c18bcddfd615a55bdbd0c0fcd0b910012102ad8dda8f24a91d56df95954fd69f3c610cb010221710aedda904896dad1d17820047304402207b0aeb57f65cc732558fc40a78cdfe5928834935d70d3eb3f6dc0f699a927c390220623b4659a785b48ad0dd2562544ec7ee02703780600035819e2eeafa4bf9541301ffffffff0100350c00000000001976a9149338f3aaebc5591443e14e60959a6c49b5d1a4f088ac00000000
19:11:56.108 [main] INFO  edu.nyu.crypto.csci3033.transactions.ScriptTransaction - Broadcasted transaction: 36af3d957640c4cc38719768d71e821ba23b0cf2b212f4a8947cc216e154392c

